#!/usr/bin/env python3
"""
Cryptrion Cyber – Threat Intelligence Collector
Collects publicly available threat data, generates a report,
and publishes it to threats.cryptrion-cyber.vercel.app via the API.
"""

import json
import os
import re
import time
import hashlib
import requests
import feedparser
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# ──────────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────────
VERCEL_API_URL = os.getenv("VERCEL_API_URL", "https://threats.cryptrion-cyber.vercel.app/api/posts")
VERCEL_API_SECRET = os.getenv("VERCEL_API_SECRET", "change-me-in-env")  # shared secret
OUTPUT_DIR = Path(__file__).parent.parent / "reports"
OUTPUT_DIR.mkdir(exist_ok=True)

# Public threat intelligence feeds (no auth required)
THREAT_FEEDS = [
    {
        "name": "CISA Known Exploited Vulnerabilities",
        "url": "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json",
        "type": "json",
        "parser": "cisa_kev",
    },
    {
        "name": "NIST NVD Recent CVEs",
        "url": "https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=10&startIndex=0",
        "type": "json",
        "parser": "nvd_cves",
    },
    {
        "name": "US-CERT Alerts",
        "url": "https://www.cisa.gov/cybersecurity-advisories/all.xml",
        "type": "rss",
        "parser": "rss_generic",
    },
    {
        "name": "Bleeping Computer Security News",
        "url": "https://www.bleepingcomputer.com/feed/",
        "type": "rss",
        "parser": "rss_generic",
    },
    {
        "name": "The Hacker News",
        "url": "https://feeds.feedburner.com/TheHackersNews",
        "type": "rss",
        "parser": "rss_generic",
    },
]

# ──────────────────────────────────────────────
# PARSERS
# ──────────────────────────────────────────────

def fetch_json(url: str, timeout: int = 15) -> Optional[dict]:
    try:
        r = requests.get(url, timeout=timeout, headers={"User-Agent": "CryptrionThreatBot/1.0"})
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"  [!] JSON fetch failed for {url}: {e}")
        return None


def parse_cisa_kev(data: dict) -> list[dict]:
    """Parse CISA Known Exploited Vulnerabilities catalog."""
    items = []
    vulnerabilities = data.get("vulnerabilities", [])[:10]  # latest 10
    for v in vulnerabilities:
        items.append({
            "id": v.get("cveID", "N/A"),
            "title": f"{v.get('cveID')} – {v.get('vulnerabilityName', 'Unknown')}",
            "severity": "HIGH",
            "vendor": v.get("vendorProject", "N/A"),
            "product": v.get("product", "N/A"),
            "description": v.get("shortDescription", "No description available."),
            "action": v.get("requiredAction", ""),
            "due_date": v.get("dueDate", ""),
            "published": v.get("dateAdded", ""),
            "source": "CISA KEV",
        })
    return items


def parse_nvd_cves(data: dict) -> list[dict]:
    """Parse NIST NVD CVE feed."""
    items = []
    for entry in data.get("vulnerabilities", []):
        cve = entry.get("cve", {})
        cve_id = cve.get("id", "N/A")
        descriptions = cve.get("descriptions", [])
        desc = next((d["value"] for d in descriptions if d["lang"] == "en"), "No description.")
        metrics = cve.get("metrics", {})
        score = "N/A"
        severity = "UNKNOWN"
        for metric_key in ["cvssMetricV31", "cvssMetricV30", "cvssMetricV2"]:
            metric_list = metrics.get(metric_key, [])
            if metric_list:
                cvss = metric_list[0].get("cvssData", {})
                score = cvss.get("baseScore", "N/A")
                severity = cvss.get("baseSeverity", "UNKNOWN")
                break
        items.append({
            "id": cve_id,
            "title": f"{cve_id} (CVSS {score})",
            "severity": severity,
            "score": score,
            "description": desc[:400] + ("..." if len(desc) > 400 else ""),
            "published": cve.get("published", ""),
            "source": "NIST NVD",
        })
    return items


def parse_rss_generic(url: str, feed_name: str) -> list[dict]:
    """Parse any RSS/Atom feed."""
    items = []
    try:
        feed = feedparser.parse(url)
        for entry in feed.entries[:8]:
            items.append({
                "id": hashlib.md5(entry.get("link", entry.get("title", "")).encode()).hexdigest()[:8],
                "title": entry.get("title", "No title"),
                "description": re.sub(r"<[^>]+>", "", entry.get("summary", entry.get("description", "")))[:400],
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
                "source": feed_name,
            })
    except Exception as e:
        print(f"  [!] RSS parse failed for {url}: {e}")
    return items


# ──────────────────────────────────────────────
# COLLECTION ORCHESTRATOR
# ──────────────────────────────────────────────

def collect_all_threats() -> dict:
    """Collect data from all configured feeds."""
    results = {
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "feeds": [],
    }

    for feed in THREAT_FEEDS:
        print(f"[*] Fetching: {feed['name']}")
        feed_data = {"name": feed["name"], "items": [], "error": None}

        try:
            if feed["type"] == "json":
                raw = fetch_json(feed["url"])
                if raw:
                    if feed["parser"] == "cisa_kev":
                        feed_data["items"] = parse_cisa_kev(raw)
                    elif feed["parser"] == "nvd_cves":
                        feed_data["items"] = parse_nvd_cves(raw)
            elif feed["type"] == "rss":
                feed_data["items"] = parse_rss_generic(feed["url"], feed["name"])

            print(f"  [+] Got {len(feed_data['items'])} items")
        except Exception as e:
            feed_data["error"] = str(e)
            print(f"  [!] Error: {e}")

        results["feeds"].append(feed_data)
        time.sleep(1)  # be polite

    return results


# ──────────────────────────────────────────────
# REPORT GENERATOR
# ──────────────────────────────────────────────

def generate_report(data: dict) -> dict:
    """Transform collected data into a structured report."""
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%Y-%m-%d")
    slug = f"threat-report-{date_str}"

    # Flatten all items
    all_items = []
    for feed in data["feeds"]:
        all_items.extend(feed["items"])

    # Severity counts
    severity_counts = {}
    for item in all_items:
        sev = item.get("severity", "UNKNOWN").upper()
        severity_counts[sev] = severity_counts.get(sev, 0) + 1

    # Build markdown body
    lines = [
        f"# Threat Intelligence Report — {now.strftime('%B %d, %Y')}",
        "",
        f"> **Generated:** {now.strftime('%Y-%m-%d %H:%M UTC')}  ",
        f"> **Total items collected:** {len(all_items)}  ",
        f"> **Sources:** {len(data['feeds'])}",
        "",
        "---",
        "",
        "## Summary",
        "",
    ]

    for sev, count in sorted(severity_counts.items()):
        lines.append(f"- **{sev}**: {count} item(s)")

    lines += ["", "---", ""]

    for feed in data["feeds"]:
        if not feed["items"]:
            continue
        lines.append(f"## {feed['name']}")
        lines.append("")
        for item in feed["items"]:
            lines.append(f"### {item.get('title', 'Unknown')}")
            lines.append("")
            if item.get("severity") and item["severity"] not in ("UNKNOWN", "N/A"):
                lines.append(f"**Severity:** `{item['severity']}`  ")
            if item.get("score"):
                lines.append(f"**CVSS Score:** {item['score']}  ")
            if item.get("vendor"):
                lines.append(f"**Vendor:** {item['vendor']} — **Product:** {item.get('product', 'N/A')}  ")
            if item.get("published"):
                lines.append(f"**Published:** {item['published']}  ")
            lines.append("")
            lines.append(item.get("description", ""))
            if item.get("action"):
                lines.append(f"\n> **Required Action:** {item['action']}")
            if item.get("link"):
                lines.append(f"\n[Read more →]({item['link']})")
            lines.append("")
            lines.append("---")
            lines.append("")

    report = {
        "slug": slug,
        "title": f"Threat Intelligence Report — {now.strftime('%B %d, %Y')}",
        "date": now.isoformat(),
        "summary": f"Automated threat intelligence digest covering {len(all_items)} items from {len(data['feeds'])} public sources.",
        "severity_counts": severity_counts,
        "total_items": len(all_items),
        "content_markdown": "\n".join(lines),
        "raw_data": data,
    }

    return report


# ──────────────────────────────────────────────
# SAVE REPORT LOCALLY
# ──────────────────────────────────────────────

def save_report(report: dict) -> Path:
    """Save report as JSON and Markdown files."""
    slug = report["slug"]

    # JSON (full data)
    json_path = OUTPUT_DIR / f"{slug}.json"
    json_path.write_text(json.dumps(report, indent=2, default=str), encoding="utf-8")
    print(f"[+] Saved JSON: {json_path}")

    # Markdown
    md_path = OUTPUT_DIR / f"{slug}.md"
    md_path.write_text(report["content_markdown"], encoding="utf-8")
    print(f"[+] Saved Markdown: {md_path}")

    return json_path


# ──────────────────────────────────────────────
# PUBLISH TO VERCEL CHILD SITE
# ──────────────────────────────────────────────

def publish_to_blog(report: dict) -> bool:
    """POST report to the Vercel child site API."""
    payload = {
        "slug": report["slug"],
        "title": report["title"],
        "date": report["date"],
        "summary": report["summary"],
        "content": report["content_markdown"],
        "severity_counts": report["severity_counts"],
        "total_items": report["total_items"],
    }

    headers = {
        "Content-Type": "application/json",
        "x-api-secret": VERCEL_API_SECRET,
    }

    try:
        print(f"[*] Publishing to {VERCEL_API_URL} ...")
        r = requests.post(VERCEL_API_URL, json=payload, headers=headers, timeout=20)
        r.raise_for_status()
        print(f"[+] Published! Status: {r.status_code}")
        print(f"    Response: {r.text[:200]}")
        return True
    except requests.exceptions.HTTPError as e:
        print(f"[!] HTTP error publishing: {e}")
        print(f"    Response: {e.response.text[:300] if e.response else 'N/A'}")
        return False
    except Exception as e:
        print(f"[!] Failed to publish: {e}")
        return False


# ──────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  CRYPTRION CYBER — Threat Intelligence Collector")
    print(f"  {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 60)
    print()

    # 1. Collect
    print("[STEP 1] Collecting threat data...")
    raw_data = collect_all_threats()

    # 2. Generate report
    print("\n[STEP 2] Generating report...")
    report = generate_report(raw_data)
    print(f"  Total items: {report['total_items']}")
    print(f"  Severity breakdown: {report['severity_counts']}")

    # 3. Save locally
    print("\n[STEP 3] Saving report files...")
    save_report(report)

    # 4. Publish
    print("\n[STEP 4] Publishing to blog...")
    success = publish_to_blog(report)

    print()
    print("=" * 60)
    print(f"  Done! {'Published ✓' if success else 'Saved locally only (publish failed)'}")
    print("=" * 60)


if __name__ == "__main__":
    main()

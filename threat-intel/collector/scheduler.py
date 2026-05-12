#!/usr/bin/env python3
"""
scheduler.py — Run the threat collector on a schedule.
Usage: python scheduler.py [--interval HOURS]
Default: runs every 24 hours. Can also be called by cron/Task Scheduler.
"""

import sys
import time
import logging
import argparse
from datetime import datetime, timezone

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("scheduler")

# Load .env if present
try:
    from dotenv import load_dotenv
    load_dotenv()
    log.info("Loaded .env")
except ImportError:
    pass


def run_collector():
    """Import and run the threat collector."""
    from threat_collector import main as collector_main
    try:
        collector_main()
        log.info("Collection run completed successfully.")
        return True
    except Exception as e:
        log.error(f"Collection run failed: {e}", exc_info=True)
        return False


def main():
    parser = argparse.ArgumentParser(description="Cryptrion Threat Intel Scheduler")
    parser.add_argument("--interval", type=float, default=24.0,
                        help="Hours between collection runs (default: 24)")
    parser.add_argument("--once", action="store_true",
                        help="Run once and exit (for cron/Task Scheduler)")
    args = parser.parse_args()

    log.info(f"Cryptrion Threat Intel Scheduler starting.")

    if args.once:
        log.info("Running once (--once mode).")
        run_collector()
        return

    interval_sec = args.interval * 3600
    log.info(f"Running every {args.interval}h ({interval_sec:.0f}s). Press Ctrl+C to stop.")

    while True:
        log.info(f"Starting collection run at {datetime.now(timezone.utc).isoformat()}")
        run_collector()
        next_run = datetime.now(timezone.utc).timestamp() + interval_sec
        next_str = datetime.fromtimestamp(next_run, tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        log.info(f"Next run at {next_str}. Sleeping...")
        try:
            time.sleep(interval_sec)
        except KeyboardInterrupt:
            log.info("Stopped by user.")
            sys.exit(0)


if __name__ == "__main__":
    main()

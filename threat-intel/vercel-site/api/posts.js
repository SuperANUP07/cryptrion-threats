// api/posts.js — Vercel Edge Function
// Receives threat reports from the Python collector and stores them in Upstash Redis.

export const config = { runtime: "edge" };

const API_SECRET = process.env.VERCEL_API_SECRET || "change-me";

export default async function handler(req) {
  // ── GET: list all posts ──────────────────────────────
  if (req.method === "GET") {
    try {
      const kv = getKV();
      const keys = await kv.list("post:");
      const posts = await Promise.all(keys.map(k => kv.get(k)));
      const sorted = posts
        .filter(Boolean)
        .sort((a, b) => new Date(b.date) - new Date(a.date));
      return new Response(JSON.stringify(sorted), {
        headers: corsHeaders("application/json"),
      });
    } catch (e) {
      return new Response(JSON.stringify({ error: e.message }), {
        status: 500, headers: corsHeaders("application/json"),
      });
    }
  }

  // ── POST: create/update a post ───────────────────────
  if (req.method === "POST") {
    const secret = req.headers.get("x-api-secret");
    if (secret !== API_SECRET) {
      return new Response(JSON.stringify({ error: "Unauthorized" }), {
        status: 401, headers: corsHeaders("application/json"),
      });
    }
    try {
      const body = await req.json();
      const { slug, title, date, summary, content, severity_counts, total_items } = body;
      if (!slug || !title || !content) {
        return new Response(JSON.stringify({ error: "Missing required fields" }), {
          status: 400, headers: corsHeaders("application/json"),
        });
      }
      const post = {
        slug, title,
        date: date || new Date().toISOString(),
        summary: summary || "",
        content,
        severity_counts: severity_counts || {},
        total_items: total_items || 0,
        updated_at: new Date().toISOString(),
      };
      const kv = getKV();
      await kv.set(`post:${slug}`, post);
      return new Response(
        JSON.stringify({ ok: true, slug, url: `/post/${slug}` }),
        { status: 201, headers: corsHeaders("application/json") }
      );
    } catch (e) {
      return new Response(JSON.stringify({ error: e.message }), {
        status: 500, headers: corsHeaders("application/json"),
      });
    }
  }

  if (req.method === "OPTIONS") {
    return new Response(null, { headers: corsHeaders() });
  }

  return new Response("Method Not Allowed", { status: 405 });
}

function corsHeaders(contentType) {
  const h = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, x-api-secret",
  };
  if (contentType) h["Content-Type"] = contentType;
  return h;
}

function getKV() {
  const url = process.env.UPSTASH_REDIS_REST_URL;
  const token = process.env.UPSTASH_REDIS_REST_TOKEN;

  if (url && token) {
    const call = async (cmd) => {
      const res = await fetch(`${url}/pipeline`, {
        method: "POST",
        headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
        body: JSON.stringify([cmd]),
      });
      const json = await res.json();
      return json[0]?.result ?? null;
    };

    return {
      get: async (key) => {
        const val = await call(["GET", key]);
        if (!val) return null;
        try { return JSON.parse(val); } catch { return val; }
      },
      set: async (key, val) => {
        const str = typeof val === "string" ? val : JSON.stringify(val);
        // SET with no expiry, then add to persistent index
        await fetch(`${url}/pipeline`, {
          method: "POST",
          headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
          body: JSON.stringify([
            ["SET", key, str],
            ["SADD", "post-index", key],
          ]),
        });
      },
      list: async (prefix) => {
        const members = await call(["SMEMBERS", "post-index"]);
        return (members || []).filter(k => k.startsWith(prefix));
      },
    };
  }

  // Local dev fallback
  if (!globalThis.__devStore) globalThis.__devStore = {};
  if (!globalThis.__devIndex) globalThis.__devIndex = new Set();
  const store = globalThis.__devStore;
  const index = globalThis.__devIndex;
  return {
    get: async (key) => store[key] ? JSON.parse(store[key]) : null,
    set: async (key, val) => { store[key] = JSON.stringify(val); index.add(key); },
    list: async (prefix) => [...index].filter(k => k.startsWith(prefix)),
  };
}

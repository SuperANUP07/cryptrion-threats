// api/posts.js  — Vercel Serverless Function
// Receives threat reports from the Python collector and stores them.
// Uses Upstash Redis (or falls back to in-memory for local dev).

export const config = { runtime: "edge" };   // Edge runtime = fast globally

const API_SECRET = process.env.VERCEL_API_SECRET || "change-me";

export default async function handler(req) {
  // ── GET: list all posts ──────────────────────────────
  if (req.method === "GET") {
    try {
      const kv = await getKV();
      const keys = await kv.list({ prefix: "post:" });
      const posts = await Promise.all(
        keys.keys.map(async (k) => {
          const val = await kv.get(k.name);
          return val ? JSON.parse(val) : null;
        })
      );
      const sorted = posts
        .filter(Boolean)
        .sort((a, b) => new Date(b.date) - new Date(a.date));
      return new Response(JSON.stringify(sorted), {
        headers: corsHeaders("application/json"),
      });
    } catch (e) {
      return new Response(JSON.stringify({ error: e.message }), {
        status: 500,
        headers: corsHeaders("application/json"),
      });
    }
  }

  // ── POST: create/update a post ───────────────────────
  if (req.method === "POST") {
    const secret = req.headers.get("x-api-secret");
    if (secret !== API_SECRET) {
      return new Response(JSON.stringify({ error: "Unauthorized" }), {
        status: 401,
        headers: corsHeaders("application/json"),
      });
    }

    try {
      const body = await req.json();
      const { slug, title, date, summary, content, severity_counts, total_items } = body;

      if (!slug || !title || !content) {
        return new Response(JSON.stringify({ error: "Missing required fields: slug, title, content" }), {
          status: 400,
          headers: corsHeaders("application/json"),
        });
      }

      const post = {
        slug,
        title,
        date: date || new Date().toISOString(),
        summary: summary || "",
        content,
        severity_counts: severity_counts || {},
        total_items: total_items || 0,
        updated_at: new Date().toISOString(),
      };

      const kv = await getKV();
      await kv.set(`post:${slug}`, JSON.stringify(post));

      return new Response(
        JSON.stringify({ ok: true, slug, url: `/post/${slug}` }),
        { status: 201, headers: corsHeaders("application/json") }
      );
    } catch (e) {
      return new Response(JSON.stringify({ error: e.message }), {
        status: 500,
        headers: corsHeaders("application/json"),
      });
    }
  }

  // ── OPTIONS: CORS preflight ──────────────────────────
  if (req.method === "OPTIONS") {
    return new Response(null, { headers: corsHeaders() });
  }

  return new Response("Method Not Allowed", { status: 405 });
}

// ──────────────────────────────────────────────────────────
// Helpers
// ──────────────────────────────────────────────────────────

function corsHeaders(contentType) {
  const h = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, x-api-secret",
  };
  if (contentType) h["Content-Type"] = contentType;
  return h;
}

// Thin wrapper around @upstash/redis (with in-memory fallback for local dev)
async function getKV() {
  const url = process.env.UPSTASH_REDIS_REST_URL;
  const token = process.env.UPSTASH_REDIS_REST_TOKEN;

  if (url && token) {
    // ── Production: Upstash Redis via REST ──────────────
    const call = async (body) => {
      const res = await fetch(url, {
        method: "POST",
        headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });
      const json = await res.json();
      return json.result;
    };

    return {
      get: async (key) => {
        const val = await call(["GET", key]);
        return val ?? null;
      },
      set: async (key, val) => {
        await call(["SET", key, val]);
      },
      list: async (opts) => {
        const pattern = opts?.prefix ? `${opts.prefix}*` : "*";
        const keys = await call(["KEYS", pattern]);
        return { keys: (keys || []).map((k) => ({ name: k })) };
      },
    };
  }

  // ── Local dev fallback: in-memory (data lost on restart) ──
  if (!globalThis.__devStore) globalThis.__devStore = {};
  const store = globalThis.__devStore;
  return {
    get: async (key) => store[key] ?? null,
    set: async (key, val) => { store[key] = val; },
    list: async (opts) => {
      const prefix = opts?.prefix || "";
      return { keys: Object.keys(store).filter((k) => k.startsWith(prefix)).map((k) => ({ name: k })) };
    },
  };
}
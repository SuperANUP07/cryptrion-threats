// api/post/[slug].js — Get a single post by slug (uses Upstash Redis)

export const config = { runtime: "edge" };

export default async function handler(req) {
  const url = new URL(req.url);
  const slug = url.pathname.split("/").pop();

  if (!slug) {
    return new Response(JSON.stringify({ error: "Slug required" }), {
      status: 400,
      headers: { "Content-Type": "application/json" },
    });
  }

  const upstashUrl = process.env.UPSTASH_REDIS_REST_URL;
  const upstashToken = process.env.UPSTASH_REDIS_REST_TOKEN;

  try {
    let post = null;

    if (upstashUrl && upstashToken) {
      const res = await fetch(upstashUrl, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${upstashToken}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify(["GET", `post:${slug}`]),
      });
      const json = await res.json();
      post = json.result ? JSON.parse(json.result) : null;
    } else {
      post = globalThis.__devStore?.[`post:${slug}`]
        ? JSON.parse(globalThis.__devStore[`post:${slug}`])
        : null;
    }

    if (!post) {
      return new Response(JSON.stringify({ error: "Not found" }), {
        status: 404,
        headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
      });
    }

    return new Response(JSON.stringify(post), {
      headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
    });
  } catch (e) {
    return new Response(JSON.stringify({ error: e.message }), {
      status: 500,
      headers: { "Content-Type": "application/json" },
    });
  }
}

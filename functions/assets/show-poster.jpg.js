export function onRequest() {
  return new Response("This reference image has been removed.", {
    status: 410,
    headers: {
      "Cache-Control": "no-store",
      "Content-Type": "text/plain; charset=utf-8",
      "X-Content-Type-Options": "nosniff"
    }
  });
}

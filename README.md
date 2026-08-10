# A Nightmare on 80s Street

Official website for the San Diego horror-themed 80s band.

Production: [80snightmareband.net](https://80snightmareband.net) · Cloudflare preview: [80s-nightmare-band.pages.dev](https://80s-nightmare-band.pages.dev)

## Local development

```bash
npm install
npm run dev
```

Wrangler serves the site from `public/`. No build step is required.

## Content updates

- Upcoming show: update the show card in `public/index.html`.
- Social links and booking details: search `public/index.html` for the current values.

Official dates and ticket links point to Bandsintown artist ID `15492639`. The public Bandsintown API currently rejects unauthenticated site requests, so the branded show row intentionally uses a reliable static fallback and sends visitors to the official listing.

## Deploy

```bash
npm run deploy
```

Cloudflare Pages configuration:

- Project name: `80s-nightmare-band`
- Production branch: `main`
- Build command: leave blank
- Build output directory: `public`

The custom domains should be `80snightmareband.net` and `www.80snightmareband.net`.

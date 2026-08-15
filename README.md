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

## Photo assets

- Original promotional photos are archived in `source-assets/photos/`.
- Optimized website versions live in `public/assets/photos/`.
- Source: [Just Us Productions](https://justusproductions.net/a-nightmare-on-80s-street-1).

## Approved brand system

The approved R2.1 package is archived without alteration in `source-assets/brand/anos-r2.1/`. Its source hierarchy, comparison proof, change log, production limitations, and vendor instructions travel with the artwork.

The website uses the preservation-faithful yellow-perimeter system:

- `public/assets/logo.svg`: canonical refined yellow-perimeter primary.
- `public/assets/logo-digital-magenta.svg`: optional digital alternative; never the heritage primary.
- `public/assets/logo-onecolor-light.svg`: one-color footer treatment on dark backgrounds.
- `public/assets/mark-80s.svg`: approved small-size mark for decorative interface use.
- `public/assets/social-80s-black.svg` and `social-80s-transparent.svg`: circle-safe social treatments.
- `public/assets/favicon.svg`, native favicon PNGs, `apple-touch-icon.png`, and `favicon.ico`: approved small-size system and derived platform containers.

Canonical logo colors are acid green (`#5ef605`), video yellow (`#f7e812`), black, and white. The approved optional digital magenta is `#f02bcb`. Blood red, electric cyan, and ultraviolet remain supporting website accents but are not alternate logo colors.

Do not redraw, recolor, regenerate, crop, stroke, filter, or add effects to the approved logo files. Print PDFs and EPS files are RGB vector references, not vendor-profiled CMYK masters. Embroidery and screen-print reference files still require vendor confirmation and physical testing.

## Search discoverability

- The homepage includes unique search and social metadata plus `WebSite`, `WebPage`, `ImageObject`, and `MusicGroup` JSON-LD.
- Each current show has a dedicated indexable page with visible venue details, a canonical URL, `MusicEvent` JSON-LD, and breadcrumb markup.
- `sitemap.xml` lists the homepage and current event pages; `robots.txt` advertises the sitemap.
- `404.html` returns a branded, crawlable `404` response with `noindex` to avoid soft-404 indexing noise.

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

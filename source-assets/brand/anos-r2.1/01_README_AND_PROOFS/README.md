# A Nightmare on 80s Street — logo package R2.1 candidate

Package version: R2.1 candidate
Date: 2026-08-14
Approval status: **candidate pending explicit human approval. Core logo geometry has passed technical
review, but the release package has not yet received final human approval.**

R2.1 is a documentation and proof correction. No artwork changed in this round: no paths, dimensions,
colors, or exports were altered, and the SVG files keep their "R2 candidate" metadata until approval
is explicitly provided. Comparison proof: `anos-r2-comparison-proof.png` and
`anos-r2-comparison-proof.pdf`. Numbered change log: `CHANGELOG.md`.

## Source hierarchy

1. `02_ARCHIVAL_PRESERVATION/anos-source-authority-raster-crop.png` — the packaged copy of the
   supplied original raster, cropped to the artwork. Heritage authority for silhouette, proportion,
   and character. Provenance: supplied to us as `01-ORIGINAL-LOGO-AUTHORITY.jpg`, which is not part
   of this package.
2. `02_ARCHIVAL_PRESERVATION/anos-preservation-master-r1.svg` — faithful reconstruction of that
   raster. Archival record.
3. `03_PRIMARY_YELLOW/anos-primary-yellow-r2.svg` — refined geometry, technical review passed, with
   the original yellow perimeter. Canonical production primary for this candidate.
4. Existing website treatments — secondary reference only.

## Canonical files

| Role | File |
| --- | --- |
| Primary heritage logo (canonical) | `03_PRIMARY_YELLOW/anos-primary-yellow-r2.svg` |
| Optional digital alternative | `04_DIGITAL_MAGENTA/anos-digital-magenta-r2.svg` |
| Archival preservation master | `02_ARCHIVAL_PRESERVATION/anos-preservation-master-r1.svg` |
| One-color dark ink | `05_ONE_COLOR/anos-onecolor-dark-r2.svg` |
| One-color light ink | `05_ONE_COLOR/anos-onecolor-light-r2.svg` |
| Micro mark | `06_SMALL_SIZE_AND_SOCIAL/anos-micro-80s-yellow-r2.svg` |
| Favicon masters | `06_SMALL_SIZE_AND_SOCIAL/anos-favicon-master-16-r2.svg`, `…-32-r2.svg` |
| Screen-print reference, light garments | `07_PRINT_REFERENCES/anos-screenprint-4ink-r2.svg` |
| Screen-print, dark garments | `03_PRIMARY_YELLOW/anos-primary-yellow-r2.svg` — perimeter retained |
| Social profile icon | `06_SMALL_SIZE_AND_SOCIAL/anos-social-icon-black-r2.svg`, `…-transparent-r2.svg` |
| Comparison proof | `01_README_AND_PROOFS/anos-r2-comparison-proof.png`, `.pdf` |
| Change log | `01_README_AND_PROOFS/CHANGELOG.md` |
| Embroidery shape reference | `07_PRINT_REFERENCES/anos-embroidery-reference-r2.svg` |

The primary and the digital alternative are the same geometry; they differ only in perimeter color.
There are no separate on-light and on-dark files: every logo SVG has a transparent background and
works on either ground, because the black plate and the perimeter supply their own separation.

## Geometry facts

- Lockup viewBox: `0 0 1548 510`. Micro mark: square, side 379. 16 px favicon master: square, side 404.
- Refined lockup: 1,199 nodes across 33 closed contours. Archival master: 1,255 nodes, 35 contours.
- Quadratic path segments only, even-odd compound paths, all contours closed and non-self-intersecting.
- No live fonts, no embedded or linked raster, no filters, no masks, no clip paths, no groups or
  transforms, no negative coordinates, no stroke attributes. Each color is one flat `<path>`.
- Layers stack back to front: perimeter, black plate, green lettering, white lettering, yellow 80s.
  Lower layers are drawn as full shapes and covered by upper layers, so seams cannot open at any scale.

## Color

| Ink | HEX | RGB | Provisional CMYK | Notes |
| --- | --- | --- | --- | --- |
| Green | `#5EF605` | 94 246 5 | C62 M0 Y98 K4 | sampled from the supplied raster; out of four-color gamut |
| Yellow | `#F7E812` | 247 232 18 | C0 M6 Y93 K3 | sampled from the supplied raster |
| Magenta | `#F02BCB` | 240 43 203 | C0 M82 Y15 K6 | sampled from the live site; digital alternative only; out of gamut |
| Black | `#000000` | 0 0 0 | K100 | rich black only on the printer's advice |
| White | `#FFFFFF` | 255 255 255 | knockout / substrate | never printed as opaque white without vendor confirmation |

CMYK values are provisional arithmetic conversions, not press matches, and no Pantone equivalents are
claimed. Both the green and the magenta will print noticeably duller than they appear on screen.

## Background treatments

Permitted: black, white, and near-black or near-white solids. On mid-tone solids the mark still
reads, but the black plate loses separation — place it on a solid black field instead. Over
photography, always place it on a solid black field. Do not add glow, bevel, outer stroke, or drop
shadow; the plate and perimeter are the built-in shadow system.

## Minimum reproduction sizes

**Preliminary production recommendations derived from vector measurements. Final minimum sizes must be
confirmed through physical print tests, embroidery sew-outs, and vendor specifications.** The figures
below come from measuring the artwork itself, not from experience of these materials in production;
the narrowest enclosed opening in the full-color lockup is carried by color separation, so the lockup
holds smaller than the one-color builds do.

| Build | Screen minimum | Print minimum | Limiting feature |
| --- | --- | --- | --- |
| Full-color lockup | 140 px wide | 32 mm / 1.25 in | second line closes up below this on screen |
| One-color lockup | 240 px wide | 45 mm / 1.75 in | narrowest counter is 12.8 px at 1548 px width |
| Screen-print 4-ink | — | 60 mm / 2.4 in | thinnest ink feature is 5.8 px at 1548 px width |
| Embroidery reference | — | 115 mm / 4.5 in | narrowest opening 20.8 px at 1548 px width ≈ 1.5 mm |
| Micro mark | 16 px | 8 mm | at 16 px the small `s` reads as a nub; the `80` silhouette carries recognition |

Below the lockup minimums, use the micro mark instead of shrinking the lockup.

## Garment color and the screen-print build

The four-ink reference drops the perimeter, so on a **black or very dark garment the black plate
merges with the fabric** and the lettering loses its shadow. On dark garments supply the primary
artwork, which keeps the perimeter.

The primary artwork contains black, green, yellow, and white artwork. Final separation count depends
on garment color, substrate, underbase requirements, trapping, ink system, and the selected printer's
production method. The yellow perimeter is not inherently a separate ink color — it shares the yellow
of the `80s` and may share a separation. The printer must determine whether additional underbase,
highlight, blocker, or other screens are required. We do not specify a screen count.

## Social profile safe area

Profile images are cropped to a circle on most platforms. `anos-social-icon-black-r2.svg` places the
mark inside a circular safe area at 88 percent of the square, so nothing is clipped by the crop; a
transparent-ground version is included for platforms that supply their own background. Do not scale
the mark up inside the square — the padding is the safe area.

## Clear space

Keep clear space equal to 8 percent of the placed logo width on all four sides — at 1548 px that is
124 px. Nothing enters that field: no type, rule, image edge, or crop. Favicon and social masters
already carry their own padding inside the square and need no additional margin.

## File status

- **Candidate for active use, pending approval:** everything in `03_PRIMARY_YELLOW`, `05_ONE_COLOR`,
  `06_SMALL_SIZE_AND_SOCIAL`.
- **Optional:** `04_DIGITAL_MAGENTA` — digital and creative use only, never as the heritage primary.
- **Reference:** `07_PRINT_REFERENCES` — vendor references, not production-ready separations.
- **Archival:** `02_ARCHIVAL_PRESERVATION` — do not use in production, do not overwrite.
- **Deprecated:** `02-CURRENT-VECTOR-NOT-AUTHORITY.svg`, `03-CURRENT-ONE-COLOR-REFERENCE.svg`,
  `04-CURRENT-BADGE-REFERENCE.svg`, and any logo raster embedded in the current site build. Those
  carried roughly 26,000 nodes from an automatic trace with staircase contours and a perimeter that
  dropped out at small sizes. Remove them from the site, merch templates, and shared drives.

## Known production limitations

- All files are RGB. Nothing here is ICC-profiled, Pantone-matched, PDF/X-compliant, or certified for
  any vendor. No profiles or press specifications have been supplied to us.
- PDF and EPS files are plain single-page vector exports of the same paths. They are editable vector
  masters and vendor references. Open and confirm them in your own editor before sending to a printer.
- Geometry was derived from a compressed JPEG, so sub-pixel edge detail is an interpretation of that
  source rather than a recovery of the lost original artwork.
- No `.ico` container, no stitch file, no CMYK press files, no separation films.
- The 16 px favicon is a legibility compromise by design: it prioritizes the `80` silhouette.
- The comparison proof PDF is live vector: artwork drawn from the packaged paths, labels set in
  Helvetica, and only panel 01 (the source raster) embedded as an image. The proof PNG is the 1:1
  raster equivalent. Both are review documents — use the artwork files themselves for production.
- Minimum sizes, separation counts, and stitch behaviour are untested in production. Nothing in this
  package has been physically printed, pressed, or sewn.

## Full inventory — R2.1 candidate

34 files. Every file is listed here; nothing in the package is unlisted, and every file named anywhere
in this documentation exists in the package.

### 01_README_AND_PROOFS
| File | Status |
| --- | --- |
| `README.md` | this document |
| `CHANGELOG.md` | numbered change log, sections A–F |
| `anos-r2-comparison-proof.png` | comparison proof, raster, 1:1 |
| `anos-r2-comparison-proof.pdf` | same panels as live vector paths, single page 1600 x 5208 pt; only panel 01, the source raster, is an embedded image |

### 02_ARCHIVAL_PRESERVATION
| File | Status |
| --- | --- |
| `anos-source-authority-raster-crop.png` | heritage authority, provenance record |
| `anos-preservation-master-r1.svg` | archival reconstruction — not for production |

### 03_PRIMARY_YELLOW
| File | Status |
| --- | --- |
| `anos-primary-yellow-r2.svg` | canonical primary artwork |
| `anos-primary-yellow-r2.pdf` | vector master for print vendors |
| `anos-primary-yellow-r2.eps` | vector master for older print workflows |

### 04_DIGITAL_MAGENTA
| File | Status |
| --- | --- |
| `anos-digital-magenta-r2.svg` | optional digital alternative |
| `anos-digital-magenta-r2.pdf` | optional |
| `anos-digital-magenta-r2.eps` | optional |

### 05_ONE_COLOR
| File | Status |
| --- | --- |
| `anos-onecolor-dark-r2.svg` | one ink, dark |
| `anos-onecolor-dark-r2.pdf` | one ink, dark |
| `anos-onecolor-dark-r2.eps` | one ink, dark |
| `anos-onecolor-light-r2.svg` | one ink, light |
| `anos-onecolor-light-r2.pdf` | one ink, light |
| `anos-onecolor-light-r2.eps` | one ink, light |

### 06_SMALL_SIZE_AND_SOCIAL
| File | Status |
| --- | --- |
| `anos-micro-80s-yellow-r2.svg` | micro mark, primary |
| `anos-micro-80s-yellow-r2.pdf` | micro mark, primary |
| `anos-micro-80s-yellow-r2.eps` | micro mark, primary |
| `anos-micro-80s-magenta-r2.svg` | micro mark for the digital alternative |
| `anos-micro-80s-512-r2.png` | 512 px raster of the micro mark |
| `anos-favicon-master-16-r2.svg` | 16 px favicon master, heavier keyline |
| `anos-favicon-master-32-r2.svg` | 32 px favicon master |
| `anos-favicon-16-r2.png` | native 16 px export |
| `anos-favicon-32-r2.png` | native 32 px export |
| `anos-favicon-48-r2.png` | native 48 px export |
| `anos-social-icon-black-r2.svg` | social icon, black ground, circle-safe |
| `anos-social-icon-transparent-r2.svg` | social icon, transparent ground, circle-safe |
| `anos-social-1024-r2.png` | 1024 px social export |

### 07_PRINT_REFERENCES
| File | Status |
| --- | --- |
| `anos-screenprint-4ink-r2.svg` | reference, light garments |
| `anos-embroidery-reference-r2.svg` | shape reference only, not a stitch file |

### 08_VENDOR_HANDOFF
| File | Status |
| --- | --- |
| `VENDOR-HANDOFF.md` | what to send whom, prepress disclosures, vendor requirements |

## Vendor handoff

See `08_VENDOR_HANDOFF/VENDOR-HANDOFF.md`.

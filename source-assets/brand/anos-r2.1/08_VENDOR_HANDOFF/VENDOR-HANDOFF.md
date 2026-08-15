# Vendor handoff instructions — A Nightmare on 80s Street (R2.1 candidate)

Status: candidate pending explicit human approval. Core logo geometry has passed technical review,
but the release package has not yet received final human approval. Do not treat these files as a
released brand package until that approval is given.

Give the vendor the file named below plus this page. Do not send the archival preservation master.

## What to send

| Vendor | Send | Notes |
| --- | --- | --- |
| Offset / digital print | `03_PRIMARY_YELLOW/anos-primary-yellow-r2.pdf` or `.eps` | RGB vector master; the vendor converts |
| Screen printer, light garments | `07_PRINT_REFERENCES/anos-screenprint-4ink-r2.svg` | four inks, perimeter removed |
| Screen printer, dark garments | `03_PRIMARY_YELLOW/anos-primary-yellow-r2.svg` | perimeter must stay; separation count is the printer's call |
| Single-ink print, stamps, etch | `05_ONE_COLOR/anos-onecolor-dark-r2.eps` or `-light-r2.eps` | pick by substrate |
| Embroiderer | `07_PRINT_REFERENCES/anos-embroidery-reference-r2.svg` | shape reference only |
| Web / app | `03_PRIMARY_YELLOW/anos-primary-yellow-r2.svg` + favicon PNGs | magenta build optional |

## Prepress disclosures — state these to every vendor

- The supplied SVG, PDF, and EPS files are clean RGB vector artwork. They are suitable as editable
  vector masters and as vendor references. They are not color-managed and carry no ICC profile.
- Final CMYK conversion must be performed by the printer using the selected press and paper ICC
  profile and their own specifications. Do not treat our provisional CMYK numbers as a target.
- Spot color choices remain provisional until confirmed with the production vendor. No Pantone match
  has been made and no printer certification exists for these files.
- The green `#5EF605` and the magenta `#F02BCB` are outside four-color gamut. Expect visible dulling
  in CMYK. Request spot inks and approve a physical draw-down before any run.

## Screen print

On black or very dark garments the black plate merges with the fabric and the lettering loses its
shadow. Use the primary artwork there, which keeps the perimeter. The four-ink build is for light
garments.

The primary artwork contains black, green, yellow, and white artwork. Final separation count depends
on garment color, substrate, underbase requirements, trapping, ink system, and the selected printer's
production method. The yellow perimeter is not inherently a separate ink color — it shares the yellow
of the 80s and may share a separation. The printer must determine whether additional underbase,
highlight, blocker, or other screens are required.

Confirm before separations are cut: garment or substrate color, ink system (plastisol, water-based,
discharge), whether a white underbase is required, mesh counts, and the vendor's minimum line and
gap. Our four-ink reference assumes black, green, yellow, and white screens with the perimeter
removed. Our preliminary recommendation is a 60 mm minimum reproduction width, derived from vector
measurement: below that the thinnest features fall under 0.25 mm. Confirm against your own minimums
and a physical test print. On light garments an underbase may not be needed; on dark garments it usually is, and the
underbase must be built by the printer, not by us.

## Embroidery

The embroidery file is a simplified shape reference. It is not a machine file and contains no stitch
data. The vendor must perform digitization, stitch-path engineering, underlay, pull compensation,
density and fabric allowances, and produce a physical sew-out for approval before production.
Our preliminary recommendation is a 115 mm minimum width, derived from vector measurement: the
narrowest opening in the art is about 1.5 mm at that size. This is untested in thread — confirm it
with a sew-out. Below 115 mm, use the micro mark.

## Favicons

`anos-favicon-16-r2.png`, `-32-r2.png`, and `-48-r2.png` are native-size exports — ship them as-is,
with no resampling. If your stack needs a single `.ico`, bundle those three PNGs; we have not built
the container. `anos-favicon-master-16-r2.svg` carries a deliberately heavier keyline so the mark
survives 16 px.

## What we still need from you to go further

A named printer and their profile and specification sheet; garment colors and ink system for merch;
the embroidery vendor's minimum sizes. With those we can build matched CMYK press files, confirmed
spot references, and separation-ready artwork.

# CHANGELOG — A Nightmare on 80s Street logo package

Status: **R2.1 candidate pending explicit human approval. Core logo geometry has passed technical
review, but the release package has not yet received final human approval.**

Date: 2026-08-14

Every entry below states what actually changed. Where nothing changed, that is stated too. No path
data was altered in R2.1: this round corrected documentation, added the comparison proof, and added
this changelog.

---

## A. Original raster → archival preservation master
*Faithful reconstruction*

- **A1** Raster pixels were reconstructed as closed vector contours. Silhouette, proportions, word
  hierarchy, wording, and the irregular spike and drip character are unchanged.
- **A2** The white page behind the artwork became transparency. Enclosed white letterforms of `ON`
  and `STREET` were kept as positive white shapes, not holes.
- **A3** Ink colors were sampled from raster interiors rather than matched by eye: green `#5EF605`,
  yellow `#F7E812`.
- **A4** Contour count settled at 1,255 nodes across 35 closed contours. No letterform feature was
  removed to reach that count.
- **A5** JPEG compression artifacts along ink edges were resolved into single contours. This is
  interpretation of a compressed source, not recovery of the lost original artwork.

## B. Preservation master → refined yellow-perimeter primary
*Controlled cleanup, approved in R1 review*

- **B1** Perimeter rebuilt as a constant 3 px offset of the silhouette at 1548 px width. In the raster
  it ran from roughly 0.5 px to 3 px and dropped out in places.
- **B2** One perimeter treatment now runs around the whole lockup, including the elevated `A`, which
  previously had its own keyline behaviour.
- **B3** Black plate raised to a 4 px minimum depth only where it fell below it. Measured depth began
  at 2.9 px in the lowest 5 percent of samples, with points of true tangency where green met the
  outer contour. Areas already deeper than the minimum were not touched.
- **B4** `ON` raised 6 px onto the `STREET` baseline, moved as one group. Cap heights were not
  equalised; `ON` remains smaller than `STREET`, as drawn.
- **B5** Leading `S` of `STREET` raised 3 px off its sag. The `80s` still breaks the baseline.
- **B6** Pinholes and specks removed; counters carried as even-odd compound holes. Result: 1,199 nodes
  across 33 closed contours.
- **B7** Perimeter color in this build is the original yellow `#F7E812`, matching the raster.

## C. Yellow primary → magenta digital alternative
*Color variation only*

- **C1** The perimeter fill value changed from `#F7E812` to `#F02BCB`. Nothing else differs: identical
  path data, identical node positions, identical node count, identical layer order, identical viewBox.
- **C2** Magenta was sampled from the current live site, not invented. It is documented as an optional
  digital and creative variant, never as the heritage primary.
- **C3** `#F02BCB` is outside four-color gamut and is a screen-first choice.

## D. Prior social asset → circle-safe social asset
*Production adaptation*

- **D1** In the R2 pre-release audit, the mark's `s` tail was clipped when the square was cropped to a
  circle, as most platforms do. Half the artwork diagonal measured 193.4 units against a 189.5-unit
  inscribed radius.
- **D2** The mark is now placed inside a circular safe area at 88 percent of the square: a uniform
  scale of 0.862 about the square's centre. This is placement inside the icon frame — the path data,
  proportions, and colors are unchanged, and no contour was redrawn.
- **D3** A transparent-ground version, `anos-social-icon-transparent-r2.svg`, was added for platforms
  that supply their own background.
- **D4** `anos-social-1024-r2.png` was re-exported from the repositioned artwork at the same 1024 px
  size.

## E. Prior favicon colors → yellow-primary favicon colors
*Alignment with the primary, no geometry change*

- **E1** In the earlier package the small-size marks carried the magenta perimeter, because the magenta
  build was then the primary. With the yellow build promoted to heritage primary, the micro mark,
  favicon masters, favicon PNGs, and social icon carry the yellow perimeter `#F7E812`.
- **E2** Only the perimeter fill value changed. Path data, node counts, square viewBoxes, and padding
  are identical between the yellow and magenta small-size marks.
- **E3** A magenta micro mark, `anos-micro-80s-magenta-r2.svg`, is retained so the digital alternative
  has a matching small-size mark.
- **E4** The 16 px favicon master keeps its heavier keyline. That is a deliberate legibility
  compromise: at 16 px the small `s` reads as a nub and the `80` silhouette carries recognition.

## F. R2 package → R2.1 candidate
*Documentation only*

- **F1** All statements describing the package as approved, released, or final on a date were removed,
  including the word used previously to describe frozen geometry. The package is a candidate pending
  explicit human approval.
- **F2** `anos-r2-comparison-proof.png` and `anos-r2-comparison-proof.pdf` were added to
  `01_README_AND_PROOFS`. Both reproduce the packaged artwork without modification. The PDF is live
  vector — every logo panel is drawn from the packaged path data, labels are Helvetica text, and only
  panel 01, the source raster, is an embedded image. The PNG is the 1:1 raster equivalent. Structural
  check on the PDF: header, eight objects, xref offsets, stream lengths, and trailer all verified.
- **F3** This changelog was added.
- **F4** The source-hierarchy reference now points to the packaged file
  `02_ARCHIVAL_PRESERVATION/anos-source-authority-raster-crop.png`. The supplied handoff filename
  `01-ORIGINAL-LOGO-AUTHORITY.jpg` is not part of this package and is cited as provenance only.
- **F5** Screen-print guidance rewritten to be vendor-neutral. The earlier claim that dark garments
  require a five-screen job was wrong: the perimeter and the `80s` share the same yellow and may share
  a separation. Separation count is the printer's determination.
- **F6** Minimum sizes relabelled as preliminary recommendations derived from vector measurement,
  requiring confirmation by physical print tests and sew-outs.
- **F7** SVG `<title>` metadata continues to say "R2 candidate"; the two social files, which lacked
  that wording, now carry it. Text metadata only — no path data touched.
- **F8** Inventory reconciled: every file named in the README, manifest, changelog, and vendor handoff
  exists in the package, and every packaged file is referenced.

# String logo reference

## Contents

- [Two shapes](#two-shapes)
- [File inventory](#file-inventory)
- [Which file for which background](#which-file-for-which-background)
- [Sizing and clear space](#sizing-and-clear-space)
- [Embedding on the web](#embedding-on-the-web)
- [Favicons, app icons, social cards](#favicons-app-icons-social-cards)
- [Misuse](#misuse)

## Two shapes

**Primary** — the interlocking mark followed by the `String` logotype, set as one locked-up
group. `viewBox="0 0 371 135"`, aspect ratio 2.75:1. This is the default; use it anywhere
the brand needs to be named.

**Mark** — the standalone glyph: two interlocking hooks forming an S/knot, drawn as a single
monoline stroke with rounded caps. `viewBox="0 0 264 264"`, square. Use it when the name is
already present or when the space is square and small — favicons, avatars, app icons,
loading states, watermarks, a repeated pattern.

The logotype is drawn as outlines, not set in a font, so there is no "type the logo" option.
When you need the word String in running text, set it in Space Grotesk and do not attempt to
mimic the logotype's custom `S`.

## File inventory

```
1. Vector Masters/
    Ai.ai      Adobe Illustrator master — hand off to designers
    Eps.eps    EPS master (5.7 MB) — legacy print workflows
    Pdf.pdf    PDF master — print, embedding in documents
    Svg.svg    Full guide board, 1280×1024 — not a logo file, it's a layout

2. Jpegs/
    1.jpg … 12.jpg    The rendered guide boards, 1280×1024 each.
                      Odd = mark, even = logotype. See the pairing table below.

3. Png Transparent Files/
    mark_dark.png     mark_green.png     mark_white.png       264×264 RGBA
    primary_dark.png  primary_green.png  primary_white.png    372×136 RGBA

4. Svg Separate Files/
    mark_dark.svg     mark_green.svg     mark_white.svg       viewBox 0 0 264 264
    primary_dark.svg  primary_green.svg  primary_white.svg    viewBox 0 0 371 135
```

The separate SVGs are the ones to use for essentially all screen work. They are small
(≈2–5 KB), have no root `width`/`height` so they scale to whatever box you give them, and
carry their fill as a `.cls-1` class inside a `<defs><style>` block.

The PNGs are only 264px and 372px wide — fine for a header or a favicon source, too small
for a hero or anything printed. If you need a large raster, render it from the SVG rather
than upscaling the PNG.

## Which file for which background

| Board | Background | Use |
|---|---|---|
| 1, 2 | `#FFFFFF` | `mark_green` / `primary_green` |
| 3, 4 | `#33373B` | `mark_green` / `primary_green` |
| 5, 6 | `#FFFFFF` | `mark_dark` / `primary_dark` |
| 7, 8 | `#33373B` | `mark_white` / `primary_white` |
| 9, 10 | `#C0F4FB` | `mark_dark` / `primary_dark` |
| 11, 12 | `#75F8CC` | `mark_dark` / `primary_dark` |

Reading it the other way round, as a decision rule:

- **On white** → `*_dark` is the safe default (12.0:1). `*_green` is sanctioned but sits at
  1.31:1 — see below.
- **On `#33373B`** → `*_green` for impact (9.17:1), `*_white` for restraint (12.0:1). Green
  on dark is the signature pairing; use it when the logo is the point.
- **On `#C0F4FB` or `#75F8CC`** → `*_dark`. These are light backgrounds; only the dark
  colorway reads.
- **On a photo** → put the logo over a genuinely dark or genuinely light region and use
  `*_white` or `*_dark` accordingly, or place a solid `#33373B` bar behind it. Green over
  photography is unpredictable.

**About green-on-white.** It's on boards 1 and 2, so it's approved, but 1.31:1 means it is
close to invisible for anyone with reduced contrast sensitivity and will vanish on a
projector or a printed page. Use it only large, on screens you control, where the logo is
decorative rather than functional. For anything a person needs to *find* — a site header, a
favicon, a document footer, a business card — use `*_dark`.

## Sizing and clear space

Minimum sizes below which the monoline strokes start to break up:

| | Screen | Print |
|---|---|---|
| Primary | 100px wide (≈36px tall) | 25mm wide |
| Mark | 24px | 8mm |

Clear space: reserve a margin equal to the stroke weight of the mark — roughly 1/8 of the
mark's height, or about 33px in the mark's 264-unit coordinate space — on all four sides.
Nothing crosses into it: no text, no rules, no image edges, no adjacent logos. In CSS this is
just `padding: 12.5%` around the mark or `padding: 0.09em` scaled off the primary's height.

Scale by the height of the primary or the width of the mark; never scale the two axes
independently.

## Embedding on the web

**Inline SVG** when you want to control the color from CSS or animate the logo. The fill is
a class, so you can override it:

```html
<!-- paste the contents of primary_dark.svg, then: -->
<style>
  .site-logo .cls-1 { fill: currentColor; }
</style>
```

Setting `fill: currentColor` lets one copy of the markup serve light and dark themes, which
is usually cleaner than shipping two files and toggling them.

**`<img>`** when the logo is static and you'd rather keep the markup small:

```html
<img src="/brand/primary_dark.svg" alt="String" width="222" height="81">
```

Always give `width` and `height` (or an aspect-ratio box) to avoid layout shift, and keep
them in the file's ratio — 371:135 for primary, 1:1 for mark.

**Alt text**: `alt="String"` when the logo is the site's name or a link home. `alt=""` when
the wordmark sits next to the word "String" in text, so screen readers don't say it twice.

**Theme switching**: prefer one inline SVG with `currentColor` over two `<img>` tags. If you
do ship both, `<picture>` with `media="(prefers-color-scheme: dark)"` handles it without JS.

## Favicons, app icons, social cards

Use the **mark**, not the primary — the logotype is illegible below about 100px.

| Output | Source | Notes |
|---|---|---|
| `favicon.svg` | `mark_dark.svg` | Modern browsers; add a `prefers-color-scheme` media query inside the SVG to swap to `#75F8CC` on dark |
| `favicon.ico` | `mark_dark.png` | 32×32 and 16×16; check the strokes still read at 16 |
| `apple-touch-icon.png` | `mark_dark.svg` | 180×180 on a solid `#FFFFFF` background — iOS doesn't honor transparency |
| Android / maskable | `mark_green.svg` | 512×512 on `#33373B`, with the mark at ~66% to survive the safe-zone crop |
| Social card (OG) | `primary_green.svg` | 1200×630 on `#33373B`, logo about 1/3 the width, centered |
| Avatar | `mark_green.svg` | On `#33373B`, mark at ~60% of the frame |

The mark on `#33373B` is the strongest small-size treatment — the dark field gives the
monoline strokes something to separate from, which a white field does not.

## Misuse

Each of these breaks something specific rather than just being against the rules:

- **Recoloring** outside the three colorways — the three exist because they're the ones that
  hold contrast against the sanctioned backgrounds. A custom color is untested against all of
  them.
- **Stretching or squashing** — the monoline is a constant stroke weight; non-uniform scaling
  makes it variable, which reads as a rendering bug.
- **Rotating** — the mark's asymmetry is directional; rotated, it stops reading as an S.
- **Effects** — drop shadows, glows, gradients, bevels, outlines. The mark is defined by flat
  fill and negative space; anything added competes with the counters.
- **Reconstructing the lockup** — moving the mark relative to the logotype, changing the gap,
  or re-setting `String` in a font. Use `primary_*` as shipped.
- **Placing on a busy background** without a solid backing shape.
- **Boxing it in** — a border or container inside the clear-space margin.
- **Using the mark as a letter** in a word, or the logotype inside a sentence.

When a request genuinely can't be met within these constraints, say so and propose the
closest sanctioned alternative rather than quietly bending one.

# String typography reference

## Contents

- [The two families](#the-two-families)
- [Font files in this repo](#font-files-in-this-repo)
- [Roles](#roles)
- [Type scale](#type-scale)
- [Weights and pairings](#weights-and-pairings)
- [Loading the fonts](#loading-the-fonts)
- [Type on brand colors](#type-on-brand-colors)
- [Non-web output](#non-web-output)

## The two families

**Space Grotesk** — a geometric grotesque with squared terminals, tight apertures, and
distinctive alternates. Designed as a proportional companion to Space Mono, so it carries a
slightly technical feel. Five weights, **no italics**. Variable font available upstream.
Open Font License, on Google Fonts.

**Montserrat** — a geometric sans based on Buenos Aires signage. Wide, round, generous
x-height, very readable at text sizes. Nine weights with matching italics. Open Font
License, on Google Fonts.

Both are free to use and embed, including commercially, under the OFL. The one restriction
worth remembering: if you modify a font file, the modified version can't be sold on its own
and must keep the OFL — which never comes up in practice for normal use.

## Font files in this repo

`5. Fonts/Space Grotesk/` — 5 files, no italics:

```
SpaceGrotesk-Light.ttf      300
SpaceGrotesk-Regular.ttf    400
SpaceGrotesk-Medium.ttf     500
SpaceGrotesk-SemiBold.ttf   600
SpaceGrotesk-Bold.ttf       700
```

`5. Fonts/Montserrat/` — 18 files, 9 weights × roman/italic:

```
Thin 100  ExtraLight 200  Light 300  Regular 400  Medium 500
SemiBold 600  Bold 700  ExtraBold 800  Black 900
…each with a matching -Italic
```

Space Grotesk having no italic is a real constraint, not an oversight in the bundle — the
family genuinely ships without one. Never let a renderer synthesize an oblique from it; the
sheared result fights the squared terminals badly. For emphasis in display text, change
weight or color instead, or set the emphasized run in Montserrat Italic.

## Roles

**Space Grotesk for display**: headings (h1–h3), the logotype's typographic neighbors,
large numerals and stats, buttons, nav items, labels, tables of figures, code-adjacent UI.

**Montserrat for body**: paragraphs, long-form articles, documentation, captions, form
fields, anything a person reads more than a sentence of.

This split is a convention this skill establishes — the source brand guide names both
families but assigns no roles. The reasoning: the String logotype is geometric and monoline
with squared, tightly-spaced forms, and Space Grotesk echoes that, so a heading set in it
feels continuous with the mark. Montserrat is wider and rounder with a taller x-height,
which makes it the more comfortable reader at 16px over many lines. Following the reverse
split would work too, just less well — so if a project has already committed to it, stay
consistent with the project.

A single-family fallback, when only one font can be loaded: use **Montserrat throughout**
and get display feel from weight (700–900) and tight tracking. Montserrat covers both jobs
adequately; Space Grotesk alone at body sizes is tiring.

## Type scale

A 1.25 (major third) scale off a 16px base. Space Grotesk runs slightly small on the body,
so display sizes are set generously.

| Role | Family | Size | Weight | Line height | Tracking |
|---|---|---|---|---|---|
| Display | Space Grotesk | 61px / 3.8rem | 700 | 1.05 | −0.02em |
| H1 | Space Grotesk | 49px / 3.05rem | 700 | 1.1 | −0.02em |
| H2 | Space Grotesk | 39px / 2.44rem | 600 | 1.15 | −0.015em |
| H3 | Space Grotesk | 31px / 1.95rem | 600 | 1.25 | −0.01em |
| H4 | Space Grotesk | 25px / 1.56rem | 500 | 1.3 | 0 |
| Body large | Montserrat | 20px / 1.25rem | 400 | 1.6 | 0 |
| Body | Montserrat | 16px / 1rem | 400 | 1.65 | 0 |
| Small | Montserrat | 14px / 0.875rem | 400 | 1.5 | 0 |
| Caption | Montserrat | 12px / 0.75rem | 500 | 1.4 | 0.01em |
| Overline | Space Grotesk | 12px / 0.75rem | 600 | 1.2 | 0.12em, uppercase |
| Button | Space Grotesk | 16px / 1rem | 500 | 1 | 0.01em |

Negative tracking on the large sizes matters more than usual here. Both families are
geometric, and geometric letterforms at display size open up visibly; tightening pulls them
back toward the density of the logotype.

Measure: 60–75 characters for Montserrat body. Wider than that and the generous x-height
that makes it readable starts working against you on the line return.

## Weights and pairings

Use the extremes sparingly. Montserrat Thin/ExtraLight (100/200) are display-only and
disappear below 32px; Black (900) is heavy enough to look like a different brand at body
sizes. The working range is 400–700 for Montserrat and 400–700 for Space Grotesk.

Reliable combinations:

- **Space Grotesk 700 + Montserrat 400** — the default. Editorial, clear hierarchy.
- **Space Grotesk 500 + Montserrat 400** — quieter, good for dense product UI.
- **Montserrat 700 + Montserrat 400** — the single-family fallback.
- **Space Grotesk 600 uppercase, 0.12em tracking** — eyebrows, labels, nav.

Avoid mixing weights closer than 200 apart in the same hierarchy (600 next to 700 reads as a
rendering inconsistency, not a distinction), and avoid Montserrat headings directly above
Space Grotesk body — the roles inverted looks like a mistake rather than a choice.

## Loading the fonts

### Google Fonts (preferred for web)

Both families are on Google Fonts, so linking or self-hosting from there gives you WOFF2,
subsetting, and the variable versions — all better than the bundled TTFs.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
```

`display=swap` matters: both families are geometric with unusual proportions, so a blocking
load produces a long invisible-text flash on slow connections.

### Self-hosting the bundled TTFs

Use this when the project can't reach Google Fonts. Convert to WOFF2 first — TTF is roughly
4× the size over the wire:

```bash
# pip install fonttools brotli
fonttools ttLib.woff2 compress "5. Fonts/Space Grotesk/SpaceGrotesk-Bold.ttf"
```

```css
@font-face {
  font-family: "Space Grotesk";
  src: url("/fonts/SpaceGrotesk-Bold.woff2") format("woff2");
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: "Montserrat";
  src: url("/fonts/Montserrat-Regular.woff2") format("woff2");
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}
```

Declare one `@font-face` per weight with the correct `font-weight`, rather than one block
with `font-weight: 100 900`, unless you're using the variable versions. Ship only the weights
the design actually uses — five weights of Montserrat plus three of Space Grotesk is already
a meaningful chunk of a page budget.

### Stacks

```css
--font-display: "Space Grotesk", "Montserrat", ui-sans-serif, system-ui, sans-serif;
--font-body: "Montserrat", ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif;
```

Space Grotesk falls back to Montserrat before the system font, so a partial load degrades
within the brand rather than jumping to Helvetica.

## Type on brand colors

Text color follows from the background, and the palette's three light values make this
easy to get wrong. See `colors.md` for the full matrix; the short version:

| Background | Body text | Heading | Accent text |
|---|---|---|---|
| `#FFFFFF` | `#33373B` | `#33373B` | `#4B7C6F` (green-800) |
| `#33373B` | `#FFFFFF` | `#FFFFFF` or `#75F8CC` | `#75F8CC` |
| `#C0F4FB` | `#33373B` | `#33373B` | `#33373B` |
| `#75F8CC` | `#33373B` | `#33373B` | `#33373B` |

`#75F8CC` and `#C0F4FB` are never text colors on white — 1.31:1 and 1.19:1. When a design
calls for "green text" on a light background, use `#4B7C6F`.

At weights below 400, bump one contrast step: light-weight text at the AA minimum reads worse
than the ratio suggests because the strokes are thinner than what the formula assumes.

## Non-web output

**Slides, PDFs, documents** — install both families locally from the `5. Fonts/` TTFs.
Embed fonts when exporting a PDF; both licenses permit it.

**Email** — neither family is web-safe and most clients block webfonts. Use
`font-family: Montserrat, 'Helvetica Neue', Helvetica, Arial, sans-serif` and design for the
fallback, since that's what most recipients will see.

**Images and social cards** — render text into the image rather than relying on the viewer
having the fonts.

**Terminal, code blocks, monospace** — the guide specifies no mono. Space Mono is the natural
choice, since Space Grotesk was drawn as its proportional companion and they share
proportions and terminals. Flag it as outside the guide when you use it.

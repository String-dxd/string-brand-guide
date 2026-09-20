---
name: string-brand
# Folded block scalar, not a plain scalar. A bare " #" in YAML starts a comment, so an
# unquoted description containing hex values silently truncates at the first one.
description: >-
  The String brand system — the official color palette (#75F8CC mint, #33373B dark,
  #C0F4FB sky), the Montserrat + Space Grotesk typefaces, and the logo/mark asset files
  with their approved background pairings. Use this skill whenever you are producing
  anything that carries String's identity or picking colors, fonts, or a logo file for it:
  websites, landing pages, web apps, UI components, CSS/Tailwind themes, design tokens,
  slide decks, PDFs, social images, README banners, favicons, email templates, diagrams,
  or charts. Trigger it even when the request never says "brand" or "style guide" —
  "build a landing page for String", "make the dashboard match our colors", "what's our
  green?", "add the logo to the header", and "set up the fonts" all need it. Consult it
  before inventing a hex value, choosing a font stack, or referencing a logo path, so the
  output matches the real guide instead of a plausible guess.
---

# String Brand System

This skill is the machine-readable version of the String brand guide that lives in this
repository. Its job is to keep anything you build on-brand without you having to open the
JPEG boards or eyedropper a PNG.

Everything here was read directly out of the source assets (`1. Vector Masters/Svg.svg`,
the six separate SVGs, and the twelve JPEG boards), so the values are the real ones rather
than approximations. Where the source guide is silent and this skill establishes a
convention instead, it says so explicitly — that distinction matters, because a convention
is something you may reasonably deviate from with a reason, while a palette value is not.

## The 30-second version

| | Value | Use for |
|---|---|---|
| **String Green** | `#75F8CC` | The brand color. Logos, accents, highlights, CTAs, large fills. |
| **String Dark** | `#33373B` | Ink and dark surfaces. All body text. The default logo color on light backgrounds. |
| **String Sky** | `#C0F4FB` | Secondary accent. Section backgrounds, cards, chart fills. |
| **White** | `#FFFFFF` | Primary light surface. |
| **Display type** | Space Grotesk | Headings, logotype-adjacent text, numerals, UI labels. |
| **Body type** | Montserrat | Paragraphs, long-form copy, dense UI. |

The single most important rule: **`#75F8CC` and `#C0F4FB` are not text colors on white.**
They sit at 1.31:1 and 1.19:1 against white, which is effectively invisible. They are fill
colors. Text is `#33373B` on light, `#FFFFFF` or `#75F8CC` on dark.

## Choosing a logo file

Assets live at the repo root. Two shapes, three colorways, four formats:

- **Primary** — the full `String` logotype with the mark. `viewBox="0 0 371 135"`. Default choice.
- **Mark** — the standalone knot glyph, square. `viewBox="0 0 264 264"`. Use when space is
  tight or square: favicons, avatars, app icons, watermarks.

```
4. Svg Separate Files/{primary,mark}_{green,dark,white}.svg    ← use these for web/UI
3. Png Transparent Files/{primary,mark}_{green,dark,white}.png ← raster, transparent
1. Vector Masters/{Ai.ai,Eps.eps,Pdf.pdf}                      ← print + handoff to designers
1. Vector Masters/Svg.svg                                      ← NOT a logo, see below
2. Jpegs/1..12.jpg                                             ← the rendered guide boards
```

`1. Vector Masters/Svg.svg` is a 1280×1024 guide board — a page layout containing a logo, not
an asset you can drop into a design. Reaching for it because the name looks right is the easy
mistake here. For print or a designer handoff use `Ai.ai`, `Eps.eps`, or `Pdf.pdf`; for
anything on screen use the separate SVGs.

Pick the colorway from the background, not from taste. The guide sanctions exactly these
six pairings (boards 1–12 are these six, each shown as mark then logotype):

| Background | Logo file | Contrast |
|---|---|---|
| `#FFFFFF` white | `*_green.svg` | 1.31 — sanctioned, but see below |
| `#FFFFFF` white | `*_dark.svg` | 12.0 |
| `#33373B` dark | `*_green.svg` | 9.17 |
| `#33373B` dark | `*_white.svg` | 12.0 |
| `#C0F4FB` sky | `*_dark.svg` | 10.04 |
| `#75F8CC` green | `*_dark.svg` | 9.17 |

Green-on-white is in the official guide, so it is not wrong — but at 1.31:1 it disappears
at small sizes and on projectors. Reach for it only at generous scale on screens you
control (a hero, a splash), and use `primary_dark.svg` for favicons, headers, docs, and
anything printed. When you are unsure, dark-on-light and green-on-dark are the two pairings
that always work.

The combinations the guide does *not* show — white on green, white on sky, green on sky —
are unsanctioned and all fail contrast anyway. Don't improvise them.

Clear space: keep at least the height of the mark's stroke (roughly 1/8 of the mark's
height) free on all sides. Never recolor, rotate, stretch, add effects to, or re-letter the
logo; if you need a color that isn't in the three colorways, you need a different design,
not a recolored logo.

## Using the type

Both families ship as TTFs under `5. Fonts/`. Montserrat has the full Thin→Black range with
matching italics (18 files); Space Grotesk has Light, Regular, Medium, SemiBold, and Bold,
with **no italics** — so never fake an italic Space Grotesk, switch to Montserrat Italic or
find another emphasis.

Both are on Google Fonts, so for web work prefer linking or self-hosting from there over
converting the bundled TTFs.

```css
font-family: "Space Grotesk", "Montserrat", system-ui, sans-serif; /* display */
font-family: "Montserrat", system-ui, -apple-system, sans-serif;   /* body */
```

The display/body split is this skill's convention, not something the source guide states —
the guide only names the two families. The reasoning: the String logotype is geometric and
monoline, and Space Grotesk's squared terminals and tight apertures echo it, so headings set
in it feel continuous with the mark, while Montserrat's wider, rounder forms are the more
comfortable reader at paragraph sizes. If a project has already committed to the opposite
split, follow the project — consistency within a product beats consistency with this file.

## Reaching for more detail

The tables above cover most work. Read further when the task needs it:

- **`references/colors.md`** — every color in RGB/HSL, the full contrast matrix, tints and
  shades for hover/border/disabled states, dark-mode and light-mode surface recipes, and
  chart palettes. Read this whenever you need a color that is *not* one of the four, since
  inventing one off-palette is the most common way work drifts off-brand.
- **`references/logo.md`** — per-file inventory, favicon and social-card sizing, embedding
  SVG inline vs. `<img>`, and the misuse list in full.
- **`references/typography.md`** — the type scale, weight pairings, `@font-face` blocks for
  self-hosting the bundled TTFs, Google Fonts links, and the exact font files present.

Two drop-in files save you from retyping values:

- **`assets/tokens.css`** — CSS custom properties plus a light/dark theme block. Copy it into
  a project and reference `var(--string-green)` rather than pasting hex codes around.
- **`assets/tokens.json`** — the same values as data, for Tailwind configs, design-token
  pipelines, or any script that needs to read the palette.

And one tool:

- **`scripts/contrast.py`** — checks any foreground/background pair against WCAG. Run it
  before shipping a color combination you invented:

  ```bash
  python3 .claude/skills/string-brand/scripts/contrast.py '#33373B' '#C0F4FB'
  python3 .claude/skills/string-brand/scripts/contrast.py --matrix   # whole palette
  python3 .claude/skills/string-brand/scripts/contrast.py --audit    # re-verify these docs
  ```

  `--audit` re-checks every foreground/background pairing this skill documents and exits
  non-zero if any has drifted. Run it after editing a color anywhere in the skill — the
  ratios in these files are hand-written, and an earlier version shipped status colors that
  sat at 3.0:1 on their own tint backgrounds.

## Working on-brand

A few habits that keep output consistent, in rough order of how often they matter:

**Let dark and white carry the layout; let green punctuate it.** The guide's boards are
overwhelmingly one flat background with one logo — the brand's character comes from
restraint and a lot of empty space, not from spreading `#75F8CC` everywhere. Green reads as
brand precisely because it is scarce. A page that is 90% white or dark with green on the one
thing that matters looks like String; a page washed in mint does not.

**Never invent a hex value silently.** If you need a hover state, a border, or a fifth chart
series, take it from `references/colors.md` rather than nudging a channel by eye. If nothing
there fits, derive it from a palette color, say in your response which one you derived and
why, and check it with `contrast.py`.

**Check contrast on any pairing not in the table above.** The palette has two very light
accents, which makes it unusually easy to produce something that looks fine on your screen
and is unreadable on someone else's.

**Prefer SVG.** The separate SVGs are small, single-path, and already have their fill baked
in as a class — they scale to any size and drop straight into HTML. Use PNG only where SVG
isn't accepted, and reach for the vector masters only for print or when handing off to a
designer.

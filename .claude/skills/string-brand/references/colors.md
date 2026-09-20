# String color reference

Everything in this file is either read directly from the source assets (the four core
colors) or derived from them by straight-line mixing toward white/dark (the ramps). Every
contrast number was computed with the WCAG 2.1 relative-luminance formula and is repeatable
via `scripts/contrast.py`.

## Contents

- [The four core colors](#the-four-core-colors)
- [Contrast matrix](#contrast-matrix)
- [Green ramp](#green-ramp)
- [Neutral / ink ramp](#neutral--ink-ramp)
- [Sky ramp](#sky-ramp)
- [Semantic recipes](#semantic-recipes) — light theme, dark theme, states
- [Charts and data viz](#charts-and-data-viz)
- [Status colors](#status-colors)
- [Where the values came from](#where-the-values-came-from)

## The four core colors

| Name | Hex | RGB | HSL | Role |
|---|---|---|---|---|
| String Green | `#75F8CC` | `117, 248, 204` | `160°, 90%, 72%` | The brand color |
| String Dark | `#33373B` | `51, 55, 59` | `210°, 7%, 22%` | Ink, dark surfaces |
| String Sky | `#C0F4FB` | `192, 244, 251` | `187°, 88%, 87%` | Secondary accent |
| White | `#FFFFFF` | `255, 255, 255` | `0°, 0%, 100%` | Primary light surface |

String Dark is a *cool* near-black — 210° hue, 7% saturation. That slight blue cast is what
makes it sit correctly next to the mint and the sky. Substituting `#333` or `#000` breaks
the relationship subtly but visibly, especially in large flat fills, so use the real value.

## Contrast matrix

| | Green | Dark | Sky | White |
|---|---|---|---|---|
| **Green** `#75F8CC` | — | **9.17** | 1.09 | 1.31 |
| **Dark** `#33373B` | **9.17** | — | **10.04** | **12.00** |
| **Sky** `#C0F4FB` | 1.09 | **10.04** | — | 1.19 |
| **White** `#FFFFFF` | 1.31 | **12.00** | 1.19 | — |

Bold = passes WCAG AA for body text (≥4.5:1). The pattern is simple and worth internalizing:
**Dark is the only core color that pairs with anything.** Green, sky, and white are all
light, so they never pair with each other for text. Three of the four core colors are light,
which is exactly why off-brand-looking, unreadable output is easy to produce here if you
pick by eye.

Thresholds, for reference: 4.5:1 body text (AA), 3:1 large text ≥24px or bold ≥18.66px (AA)
and UI components/graphics, 7:1 body text (AAA).

## Green ramp

Derived by mixing `#75F8CC` toward white (lighter) and toward `#33373B` (darker), so every
step stays in the brand's hue family rather than drifting toward a generic teal.

| Token | Hex | On white | On dark | Use |
|---|---|---|---|---|
| `green-50` | `#EAFEF7` | 1.05 | 11.44 | Faintest tint — hover rows, subtle section fills |
| `green-100` | `#CFFDED` | 1.11 | 10.81 | Badge and callout backgrounds |
| `green-200` | `#A5FADE` | 1.21 | 9.90 | Borders on light, chart fills |
| `green-300` | `#8AF9D4` | 1.27 | 9.47 | Hover state for a green surface |
| **`green-500`** | **`#75F8CC`** | **1.31** | **9.17** | **Base — the brand color** |
| `green-600` | `#69D5B2` | 1.79 | 6.72 | Pressed/active state for a green surface |
| `green-700` | `#5DB398` | 2.51 | 4.78 | Borders on dark, secondary green |
| `green-800` | `#4B7C6F` | 4.76 | — | **Green text on light backgrounds** (AA) |
| `green-900` | `#44675F` | 6.27 | — | Green text needing near-AAA, green icons on white |

`green-800` is the one to reach for when a designer asks for "the green" in a link or a
label on a white page. `green-500` in that position is unreadable; `green-800` keeps the hue
relationship and passes AA.

One caveat on reading the "On white" column: it means `#FFFFFF` exactly, and the margin is
thin enough that a tinted light surface eats it. `green-800` measures 4.76 on white but 4.44
on `ink-50 #F7F7F7` and 3.99 on `ink-100 #EBEBEB` — so green link text sitting on a card
rather than the page background quietly drops below AA. On any surface that isn't pure white,
step down to `green-900 #44675F`. The same thinness applies to `ink-500` and `sky-800`; when
the background isn't `#FFFFFF`, check the real pair with `scripts/contrast.py`.

## Neutral / ink ramp

Built from `#33373B`, so the whole scale carries the same cool cast. Note the base sits at
**600**, not 500 — `#33373B` is darker than a conventional 500 step, and shifting it to keep
the usual numbering would have meant either lying about the brand color or compressing the
light end into uselessness.

| Token | Hex | On white | On dark | Use |
|---|---|---|---|---|
| `ink-50` | `#F7F7F7` | 1.07 | 11.20 | Page background alternate, table stripes |
| `ink-100` | `#EBEBEB` | 1.19 | 10.06 | Card backgrounds, dividers on white |
| `ink-200` | `#D2D3D4` | 1.50 | 8.00 | Borders, input outlines |
| `ink-300` | `#B1B3B5` | 2.10 | 5.70 | Disabled text on dark, placeholder on dark |
| `ink-400` | `#8D8F91` | 3.25 | 3.70 | Disabled text, large secondary text |
| `ink-500` | `#64676A` | 5.69 | 2.11 | **Secondary/muted text on light** (AA) |
| **`ink-600`** | **`#33373B`** | **12.00** | — | **Base — body text on light, dark surfaces** |
| `ink-700` | `#26292C` | 14.62 | — | Elevated dark surface, dark-mode cards |
| `ink-800` | `#1A1C1E` | 17.09 | — | Deepest dark surface |
| `ink-900` | `#0E0F11` | 19.18 | — | Near-black, use sparingly |

On dark surfaces, layer *upward* from `ink-600`: page at `#33373B`, cards at `ink-700`
`#26292C`, and so on. The guide's dark boards are flat `#33373B`, so keep elevation
differences small — a heavy multi-layer dark UI reads as someone else's brand.

## Sky ramp

| Token | Hex | On white | On dark | Use |
|---|---|---|---|---|
| `sky-50` | `#E3FAFD` | 1.03 | 11.06 | Faint section wash |
| `sky-100` | `#D3F7FC` | 1.09 | 10.56 | Callout and info backgrounds |
| **`sky-300`** | **`#C0F4FB`** | **1.19** | **10.04** | **Base — section backgrounds, cards** |
| `sky-400` | `#A1CAD1` | 1.77 | 6.79 | Borders on sky fills |
| `sky-500` | `#819FA5` | 2.82 | 4.25 | Icons on dark, secondary marks |
| `sky-800` | `#556469` | 6.15 | — | **Sky-tinted text on light** (AA) |

Sky is the least-used of the three brand colors in the source guide — it appears as a
background on two boards and nowhere else. Treat it as a supporting surface color that gives
a page a second "mood" without introducing a new hue, not as a co-equal accent to green.

## Semantic recipes

Rather than picking from the ramps every time, start from these and adjust.

### Light theme

```
page background      #FFFFFF
surface / card       #F7F7F7  (ink-50)
surface alternate    #C0F4FB  (sky-300)   — for a section that should feel different
border               #D2D3D4  (ink-200)
text primary         #33373B  (ink-600)   12.00:1
text secondary       #64676A  (ink-500)    5.69:1
text disabled        #8D8F91  (ink-400)    3.25:1 — large text only
link / accent text   #4B7C6F  (green-800)  4.76:1
focus ring           #33373B  (ink-600)   — or green-800 on a dark control
```

### Dark theme

```
page background      #33373B  (ink-600)
surface / card       #26292C  (ink-700)
border               #4B7C6F  (green-800) or a 12% white overlay
text primary         #FFFFFF                          12.00:1
text secondary       #B1B3B5  (ink-300)                5.70:1
text disabled        #8D8F91  (ink-400)                3.70:1
link / accent text   #75F8CC  (green-500)              9.17:1
focus ring           #75F8CC  (green-500)
```

Dark theme is where the brand is most itself: `#75F8CC` on `#33373B` is both the highest-
impact and highest-contrast pairing in the system. When a project could go either way,
dark-first is the more on-brand choice.

### Primary button

| | Light theme | Dark theme |
|---|---|---|
| Background | `#33373B` | `#75F8CC` |
| Label | `#FFFFFF` | `#33373B` |
| Hover bg | `#26292C` | `#8AF9D4` |
| Active bg | `#1A1C1E` | `#69D5B2` |
| Disabled bg | `#D2D3D4` | `#4B7C6F` |

A green button with dark text is the loudest thing the palette can do — one per screen. On a
light page, the dark button is the primary and green is reserved for the one action that
matters most, if any.

### Secondary / ghost button

Transparent background, `#33373B` text and 1px `#D2D3D4` border on light; `#FFFFFF` text and
a 20% white border on dark. Hover fills with `ink-50` / `ink-700`.

## Charts and data viz

The palette only supplies three hues, which is not enough for a categorical series. Extend by
walking the green and sky ramps at spaced luminance steps, which keeps everything on-brand
and stays distinguishable in grayscale:

```
1  #33373B   ink-600      2  #75F8CC   green-500
3  #819FA5   sky-500      4  #4B7C6F   green-800
5  #C0F4FB   sky-300      6  #B1B3B5   ink-300
```

Beyond six categories, prefer a different chart form (small multiples, a sorted bar chart)
over inventing a seventh color — the palette has no seventh color that stays on-brand.

For sequential scales, run `#EAFEF7 → #75F8CC → #4B7C6F → #33373B`. For diverging, use sky
on one end and green on the other with `ink-100` at the midpoint, and label it clearly since
mint and cyan are close in hue and easy to confuse at small sizes.

Gridlines `ink-200` on light / 10% white on dark; axis labels `ink-500` on light /
`ink-300` on dark.

## Status colors

The brand guide has no error/warning/success colors, so these are outside the brand and you
should not pretend otherwise. Two things worth knowing when you need them:

**Do not use green for success.** `#75F8CC` is the brand color and reads as "String," not as
"this worked." Using it for success states means every success message shouts brand and
every brand accent implies success. Use a separate, clearly different green (or better, a
checkmark plus neutral text).

Pick status colors tuned to sit next to `#33373B` — cool and slightly desaturated rather than
pure hues. These defaults are darker than the usual web palette on purpose: a status color is
almost always set on its own pale tint, and the familiar mid-tone versions
(`#D64545`, `#2E9E6B`, and friends) land around 3:1 there, which fails AA for the small text
status messages are usually set in.

Every foreground below clears 4.5:1 against its own tint, against `#FFFFFF`, and against
`ink-50 #F7F7F7`, so it holds up on any light surface in this system:

| | Foreground | Tint background | On tint | On white |
|---|---|---|---|---|
| Error | `#C13E3E` | `#FDECEC` | 4.57 | 5.22 |
| Warning | `#9F6212` | `#FDF3E3` | 4.52 | 4.96 |
| Success | `#247D55` | `#E8F6EF` | 4.56 | 5.07 |
| Info | `#367399` | `#E9F2F8` | 4.55 | 5.16 |

On dark surfaces those foregrounds are far too dark (all around 2.3:1 on `#33373B`), so flip
to the light variants. Each clears 4.5:1 on both the `ink-600` page and the `ink-700` card:

| | Foreground | On `#33373B` | On `#26292C` |
|---|---|---|---|
| Error | `#D98989` | 4.51 | 5.49 |
| Warning | `#C19965` | 4.58 | 5.58 |
| Success | `#73AC92` | 4.60 | 5.60 |
| Info | `#7CA4BD` | 4.51 | 5.50 |

Flag in your response that these are outside the brand guide so the choice can be reviewed.

## Where the values came from

- `#75F8CC`, `#33373B`, `#FFFFFF` — the `fill` values in `4. Svg Separate Files/*.svg` and
  the `.st*` classes in `1. Vector Masters/Svg.svg`.
- `#C0F4FB` — the fourth class in `1. Vector Masters/Svg.svg`, confirmed as the dominant
  color of boards `2. Jpegs/9.jpg` and `10.jpg` (JPEG compression renders it `#BFF4FA`; the
  vector value is authoritative).
- Ramps, semantic recipes, chart palettes, and status colors are derived, not from the guide.
  They are here so that work stays consistent instead of each project inventing its own
  hover state — but they are conventions, and a project with a good reason may differ.

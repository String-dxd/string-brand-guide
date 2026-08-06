# string-brand-guide
brand guide and assets for String

What is included:
## 1 Vector Masters
<img width="451" alt="Screenshot 2023-01-20 at 1 59 49 AM" src="https://user-images.githubusercontent.com/44336310/213523711-fae878eb-cca6-418b-924c-0ee48f10c084.png">

## 2 JPEG!
![4](https://user-images.githubusercontent.com/44336310/213523775-7fe455e3-861b-4c7f-b00f-6dd19165d9c8.jpg)

## 3 Transparent PNG
![primary_green](https://user-images.githubusercontent.com/44336310/213523824-d64d9661-b9f6-4353-a5e5-7854ffc51da2.png)

## 4 SVG
![primary_green](https://user-images.githubusercontent.com/44336310/213523871-41f78dae-c168-45c9-a05b-9fc579c33df0.svg)

## 5 Fonts
Montserrat
Space Grotesk

## 6 Agent Skill

`.claude/skills/string-brand/` packages this guide as a [Claude Code skill](https://code.claude.com/docs/en/skills),
so coding agents apply the brand correctly without being told the hex codes every time.
It covers the palette, the typefaces, and which logo file goes on which background.

**Quick reference**

| | |
|---|---|
| String Green | `#75F8CC` |
| String Dark | `#33373B` |
| String Sky | `#C0F4FB` |
| Display type | Space Grotesk |
| Body type | Montserrat |

Note that `#75F8CC` and `#C0F4FB` are fill colors, not text colors — both sit near 1.2:1
against white. Body text is `#33373B` on light and `#FFFFFF` or `#75F8CC` on dark.

**Using it**

Working inside this repo, Claude Code picks the skill up automatically. To use it elsewhere:

```bash
# for one project
cp -r path/to/string-brand-guide/.claude/skills/string-brand your-project/.claude/skills/

# or for every project on your machine
cp -r path/to/string-brand-guide/.claude/skills/string-brand ~/.claude/skills/
```

**What's inside**

```
SKILL.md                    palette, type, logo pairings — the everyday reference
references/colors.md        ramps, contrast matrix, themes, chart palettes
references/logo.md          file inventory, sizing, favicons, misuse
references/typography.md    type scale, weights, @font-face, loading
assets/tokens.css           CSS custom properties, light + dark themes
assets/tokens.json          the same values as data, for Tailwind/token pipelines
scripts/contrast.py         WCAG checker for any pair, plus on-brand substitutes
```

```bash
python3 .claude/skills/string-brand/scripts/contrast.py --matrix
python3 .claude/skills/string-brand/scripts/contrast.py --find '#75F8CC' --on '#FFFFFF'
```

The palette values, logo pairings, and font list come straight from the assets in this repo.
The tint/shade ramps, type scale, and the Space Grotesk / Montserrat display-body split are
conventions the skill adds on top, and it flags them as such where they appear.

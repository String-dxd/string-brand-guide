#!/usr/bin/env python3
"""WCAG contrast checker for the String palette.

Three of String's four core colors are light (#75F8CC, #C0F4FB, #FFFFFF), which makes it
unusually easy to produce a pairing that looks fine on a bright laptop and is unreadable
elsewhere. Run this before shipping any combination that isn't already in
references/colors.md.

    contrast.py '#33373B' '#C0F4FB'     ratio + pass/fail for one pair
    contrast.py --matrix                 the full core-palette matrix
    contrast.py --on '#33373B'           every named token against one background
    contrast.py --find '#75F8CC' --on '#FFFFFF'
                                         nearest on-brand substitute that passes AA

No dependencies beyond the standard library.
"""

import argparse
import sys
from pathlib import Path

# Core palette, read from the official logo vectors.
CORE = {
    "green": "#75F8CC",
    "dark": "#33373B",
    "sky": "#C0F4FB",
    "white": "#FFFFFF",
}

# Derived ramps — see references/colors.md.
TOKENS = {
    "green-50": "#EAFEF7", "green-100": "#CFFDED", "green-200": "#A5FADE",
    "green-300": "#8AF9D4", "green-500": "#75F8CC", "green-600": "#69D5B2",
    "green-700": "#5DB398", "green-800": "#4B7C6F", "green-900": "#44675F",
    "ink-50": "#F7F7F7", "ink-100": "#EBEBEB", "ink-200": "#D2D3D4",
    "ink-300": "#B1B3B5", "ink-400": "#8D8F91", "ink-500": "#64676A",
    "ink-600": "#33373B", "ink-700": "#26292C", "ink-800": "#1A1C1E",
    "ink-900": "#0E0F11",
    "sky-50": "#E3FAFD", "sky-100": "#D3F7FC", "sky-300": "#C0F4FB",
    "sky-400": "#A1CAD1", "sky-500": "#819FA5", "sky-800": "#556469",
    "white": "#FFFFFF",
}


def parse_hex(value):
    """Accept '#abc', 'abc', '#aabbcc', 'aabbcc', or a token/core name."""
    key = value.strip().lower()
    if key in TOKENS:
        value = TOKENS[key]
    elif key in CORE:
        value = CORE[key]
    h = value.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"not a color: {value!r}")
    try:
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        raise ValueError(f"not a color: {value!r}") from None


def to_hex(rgb):
    return "#%02X%02X%02X" % rgb


def luminance(rgb):
    """WCAG 2.1 relative luminance."""
    def channel(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg):
    a, b = luminance(fg), luminance(bg)
    hi, lo = max(a, b), min(a, b)
    return (hi + 0.05) / (lo + 0.05)


def grade(r):
    """Which WCAG thresholds this ratio clears."""
    return {
        "AAA body (7:1)": r >= 7,
        "AA body (4.5:1)": r >= 4.5,
        "AA large / UI (3:1)": r >= 3,
    }


def cmd_pair(fg_arg, bg_arg):
    fg, bg = parse_hex(fg_arg), parse_hex(bg_arg)
    r = ratio(fg, bg)
    print(f"\n  {to_hex(fg)} on {to_hex(bg)}   ratio {r:.2f}:1\n")
    for label, ok in grade(r).items():
        print(f"    {'PASS' if ok else 'FAIL'}  {label}")
    print()
    if r < 4.5:
        print("  Below AA for body text. See references/colors.md for on-brand")
        print("  alternatives, or run with --find to search the token set:")
        print(f"    contrast.py --find '{to_hex(fg)}' --on '{to_hex(bg)}'\n")
    return 0 if r >= 4.5 else 1


def cmd_matrix():
    names = list(CORE)
    width = max(len(n) for n in names) + 2
    print("\n  Core palette contrast matrix (* = 4.5:1 or better, passes AA body)\n")
    print(" " * (width + 2) + "".join(f"{n:>10}" for n in names))
    for a in names:
        row = f"  {a:<{width}}"
        for b in names:
            if a == b:
                row += f"{'—':>10}"
            else:
                r = ratio(parse_hex(CORE[a]), parse_hex(CORE[b]))
                mark = "*" if r >= 4.5 else " "
                row += f"{r:>9.2f}{mark}"
        print(row)
    print("\n  " + "  ".join(f"{n}={CORE[n]}" for n in names))
    print("\n  Dark is the only core color that pairs with anything — the other")
    print("  three are all light, so they never pair with each other for text.\n")
    return 0


def cmd_on(bg_arg):
    bg = parse_hex(bg_arg)
    print(f"\n  Every token against {to_hex(bg)}\n")
    rows = sorted(
        ((n, h, ratio(parse_hex(h), bg)) for n, h in TOKENS.items()),
        key=lambda t: -t[2],
    )
    for name, hexv, r in rows:
        if r >= 7:
            tag = "AAA"
        elif r >= 4.5:
            tag = "AA "
        elif r >= 3:
            tag = "AA-large"
        else:
            tag = "-"
        print(f"    {name:<11} {hexv}  {r:6.2f}:1   {tag}")
    print()
    return 0


def cmd_find(fg_arg, bg_arg, threshold):
    """Nearest token by hue family that clears the threshold against bg."""
    fg, bg = parse_hex(fg_arg), parse_hex(bg_arg)
    current = ratio(fg, bg)
    print(f"\n  {to_hex(fg)} on {to_hex(bg)} is {current:.2f}:1", end="")
    print(" — already passes.\n" if current >= threshold else f" — below {threshold}:1.\n")
    if current >= threshold:
        return 0

    def distance(a, b):
        return sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5

    options = []
    for name, hexv in TOKENS.items():
        rgb = parse_hex(hexv)
        r = ratio(rgb, bg)
        if r >= threshold:
            options.append((distance(rgb, fg), name, hexv, r))
    if not options:
        print("  No token in the palette clears that threshold against this background.")
        print("  Change the background instead — see the semantic recipes in colors.md.\n")
        return 1
    options.sort()
    print("  Closest on-brand substitutes:\n")
    for _, name, hexv, r in options[:5]:
        print(f"    {name:<11} {hexv}  {r:6.2f}:1")
    print()
    return 0


def cmd_audit():
    """Re-verify every fg/bg pairing this skill documents.

    The docs are hand-written and the ratios in them are easy to get wrong or to
    let drift — an earlier version shipped status colors that sat at 3.0:1 on
    their own tint backgrounds. Run this after editing any color.
    """
    import json
    here = Path(__file__).resolve().parent.parent
    tokens = json.loads((here / "assets" / "tokens.json").read_text())
    failures = []
    print("\n  Auditing documented pairings\n")

    def check(label, fg, bg, need):
        r = ratio(parse_hex(fg), parse_hex(bg))
        ok = r >= need
        if not ok:
            failures.append(f"{label}: {fg} on {bg} = {r:.2f} (needs {need})")
        print(f"    {'PASS' if ok else 'FAIL'}  {label:<34} {r:5.2f}:1  (needs {need})")

    sem = tokens["semantic"]
    for theme in ("light", "dark"):
        s = sem[theme]
        check(f"{theme}: body text on page", s["text"], s["bg"], 4.5)
        check(f"{theme}: body text on surface", s["text"], s["bgSurface"], 4.5)
        check(f"{theme}: muted text on page", s["textMuted"], s["bg"], 4.5)
        check(f"{theme}: accent text on page", s["textAccent"], s["bg"], 4.5)
        check(f"{theme}: button label on button", s["buttonFg"], s["buttonBg"], 4.5)

    for name, v in tokens["color"]["status"].items():
        if name.startswith("$"):
            continue
        check(f"status {name} on tint", v["fg"], v["bg"], 4.5)
        check(f"status {name} on white", v["fg"], "#FFFFFF", 4.5)
        check(f"status {name} on ink-50", v["fg"], "#F7F7F7", 4.5)
        if "fgOnDark" in v:
            check(f"status {name} on ink-600", v["fgOnDark"], "#33373B", 4.5)
            check(f"status {name} on ink-700", v["fgOnDark"], "#26292C", 4.5)

    for pair in tokens["logo"]["approvedPairings"]:
        stated = pair["contrast"]
        r = ratio(parse_hex("#" + {"green": "75F8CC", "dark": "33373B",
                                   "white": "FFFFFF"}[pair["colorway"]]),
                  parse_hex(pair["background"]))
        ok = abs(r - stated) < 0.05
        if not ok:
            failures.append(f"logo {pair['colorway']} on {pair['background']}: "
                            f"stated {stated}, actual {r:.2f}")
        print(f"    {'PASS' if ok else 'FAIL'}  logo {pair['colorway']:<5} on "
              f"{pair['background']:<9} stated {stated:>5}  actual {r:5.2f}")

    print()
    if failures:
        print(f"  {len(failures)} FAILED:")
        for f in failures:
            print(f"    - {f}")
        print()
        return 1
    print("  All documented pairings verified.\n")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(
        description="WCAG contrast checker for the String brand palette.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Colors may be hex ('#75F8CC', '75f8cc', '#abc') or token names "
               "('green-800', 'ink-500', 'dark').",
    )
    p.add_argument("colors", nargs="*", metavar="COLOR",
                   help="foreground and background, e.g. '#33373B' '#FFFFFF'")
    p.add_argument("--matrix", action="store_true",
                   help="print the core palette contrast matrix")
    p.add_argument("--audit", action="store_true",
                   help="re-verify every fg/bg pairing documented in this skill")
    p.add_argument("--on", metavar="BG",
                   help="rank every token against this background")
    p.add_argument("--find", metavar="FG",
                   help="find on-brand substitutes for FG that pass against --on")
    p.add_argument("--threshold", type=float, default=4.5,
                   help="target ratio for --find (default 4.5, AA body text)")
    args = p.parse_args(argv)

    try:
        if args.audit:
            return cmd_audit()
        if args.matrix:
            return cmd_matrix()
        if args.find:
            if not args.on:
                p.error("--find requires --on BACKGROUND")
            return cmd_find(args.find, args.on, args.threshold)
        if args.on and not args.colors:
            return cmd_on(args.on)
        if len(args.colors) == 2:
            return cmd_pair(args.colors[0], args.colors[1])
        p.print_help()
        return 2
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    except BrokenPipeError:
        # Piping into `head` closes stdout early; that's not an error.
        try:
            sys.stdout.close()
        finally:
            return 0


if __name__ == "__main__":
    sys.exit(main())

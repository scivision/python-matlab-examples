#!/usr/bin/env python
"""
prints matplotlib colors so you can copy and paste, unlike
https://matplotlib.org/3.1.0/gallery/color/named_colors.html
"""
import argparse
import typing
import matplotlib.colors as mplcolors


def get_colors(sel: str = None) -> typing.List[str]:
    base = list(mplcolors.BASE_COLORS.keys())
    tableau = list(mplcolors.TABLEAU_COLORS.keys())
    css = list(mplcolors.CSS4_COLORS.keys())
    xkcd = list(mplcolors.XKCD_COLORS.keys())

    if sel:
        matches = [c for c in (base + tableau + css + xkcd) if sel in c]
        for m in matches:
            print(m)
        return matches

    print("\n Matplotlib colors")
    print("\n base:")
    print(" ".join(base))

    print("\n tableau:")
    print(" ".join(tableau))

    print("\n CSS:")
    print(" ".join(css))

    print("\n XKCD:")
    print(" ".join(xkcd))

    return None


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("sel", help="find colors containing this word", nargs="?")
    P = p.parse_args()

    colors = get_colors(P.sel)

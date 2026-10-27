# The Offworld Nexus owl

The organization's mark is a **Eurasian eagle-owl** (*Bubo bubo*), a stylized
nod to the artificial owl of *Blade Runner*: the one bird that was built. It is
drawn in the house style of the Offworld Nexus birds — flat, geometric, Saul
Bass airline poster, a handful of silkscreen colours — and sits before a
setting sun, with glowing amber eyes as its only bright colour.

Tagline: **Small birds in the cloud.**

## Files

| File | Use |
| --- | --- |
| [`owl.svg`](owl.svg) | Master artwork, 1024 × 1024, on night blue |
| [`avatar.png`](avatar.png) | 1024 px render, the GitHub organization avatar |
| [`header-light.svg`](header-light.svg), [`header-dark.svg`](header-dark.svg) | 960 × 260 profile README headers |
| [`owl-reference.png`](owl-reference.png) | The reference bitmap the artwork was drawn from |
| [`build_owl.py`](build_owl.py) | Source of the artwork; regenerates all three SVGs |

Regenerate with `uv run python build_owl.py`, then re-render the avatar with
`inkscape owl.svg -w 1024 -o avatar.png`.

## Drawing

The owl is hand-authored in the reference's 1024 × 1024 space by reading
coordinates off a gridded copy, not auto-traced: 21 shapes plus the sun, no gradients,
filters or strokes. The face is symmetric, so `build_owl.py` holds the left
half and mirrors it around x = 512. Every mirrored shape runs 8 units past the
axis so the two halves overlap instead of meeting on a seam.

## Palette

| Token | Hex | Where |
| --- | --- | --- |
| night | `#0B111C` | Background |
| sun | `#B14D1C` | Setting-sun disc |
| umber | `#3D2719` | Crown, collar, wings |
| tawny | `#9C6429` | Facial disc |
| ochre | `#CB9040` | Ear tufts, mantle, breast |
| buff | `#E2CDA0` | Brows, eye surround |
| grey | `#B19D82` | Feathers beside the bill |
| white | `#F4F1EA` | Throat |
| black | `#05070B` | Facial rim, streaks, bill, pupils |
| iris | `#FFA20F` | Eyes |
| iris-deep | `#F0700A` | Upper iris |

## Reference

Generated with **Nano Banana Pro** (`gemini-3-pro-image-preview`, aspect ratio
1:1). A first hand-drawn, front-facing version read as a children's cartoon
and was dropped. Two prompt rounds, eight images; the frontal candidate of
round 2 was kept because it reads best inside a small circle. The prompt:

> Flat geometric illustration of a Eurasian eagle-owl (Bubo bubo), in the
> style of a 1960s Saul Bass airline travel poster and mid-century silkscreen
> prints. Head-and-shoulders portrait, three-quarter profile facing right,
> head slightly turned toward the viewer, still and watchful, regal and a
> little unsettling — the artificial owl in a corporate tower at dusk.
>
> Anatomy must be unmistakably an eagle-owl: large powerful head, long angled
> ear tufts swept back, a broad tawny facial disc edged with a dark rim, heavy
> pale brow above each eye, short hooked dark bill partly hidden in feathers,
> white throat patch, tawny-ochre breast with bold dark vertical streaks. The
> eyes are the focal point: large, perfectly round, intense glowing
> amber-orange irises with a black pupil — the only bright colour in the
> image — like the eye-shine of an animal caught in a light.
>
> Style: bold Saul Bass poster geometry — the owl is built from a few large
> shapes cut from circles, arcs and straight diagonal cuts, like cut paper;
> confident, angular, serious, iconic, simple enough to read as a logo at
> small size. Not cute, not cartoon, not a children's illustration, no
> smiling, no big round baby eyes. Big flat colour shapes with crisp hard
> edges, exactly six flat colours: deep night blue-black, dark umber, tawny
> ochre, pale buff, black, and the glowing amber; very few shapes — about
> fifteen in total — with the breast streaks reduced to four or five long
> sharp wedges. No gradients, no texture, no shading, no outlines, no
> strokes, no text, no border. Background: flat deep night blue-black, with
> one large flat burnt-orange setting-sun disc behind the head, partly hidden
> by it. Owl centred, filling about two thirds of the square with a generous
> margin.

The artwork deliberately borrows nothing from the film beyond the idea: no
Tyrell pyramid, name or frames.

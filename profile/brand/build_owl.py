# Build the owl from left-half shapes mirrored around x=512.
C = dict(night="#0b111c", sun="#b14d1c", umber="#3d2719", tawny="#9c6429", ochre="#cb9040",
         buff="#e2cda0", grey="#b19d82", white="#f4f1ea", black="#05070b", iris="#ffa20f",
         iris_d="#f0700a", glint="#fff3d6")
# (colour, path, mirror?)
L = [
 ("umber", "M90 1024 L150 760 L200 600 L260 1024 Z", True),
 ("ochre", "M520 258 L345 288 L262 330 L205 420 L170 560 L166 720 L190 1024 L520 1024 Z", True),
 ("tawny", "M282 728 C300 820 316 920 330 1024 L196 1024 C210 930 240 820 282 728 Z", True),
 ("black", "M150 122 L352 284 L520 270 L520 790 L350 730 C260 690 212 610 212 520 C212 430 240 380 268 345 C230 300 190 230 150 122 Z", True),
 ("tawny", "M520 300 L380 318 C300 350 246 420 246 520 C246 600 290 660 350 700 L520 760 Z", True),
 ("buff", "M300 470 C300 418 342 398 388 400 C440 404 474 440 474 478 C474 522 436 550 388 550 C338 550 300 518 300 470 Z", True),
 ("black", "M150 122 L346 288 L372 392 L330 410 L296 430 L276 404 L262 350 C226 290 188 220 150 122 Z", True),
 ("ochre", "M150 122 L306 190 L314 212 L346 288 L330 300 C290 250 222 186 150 122 Z", True),
 ("black", "M390 406 A60 60 0 1 1 389.9 406 Z", True),
 ("iris", "M390 412 A54 54 0 1 1 389.9 412 Z", True),
 ("iris_d", "M390 412 A54 54 0 0 1 444 466 C430 446 410 436 388 436 C366 436 348 444 336 458 A54 54 0 0 1 390 412 Z", True),
 ("black", "M392 436 A32 32 0 1 1 391.9 436 Z", True),
 ("glint", "M366 438 A9 9 0 1 1 365.9 438 Z", True),
 ("black", "M296 432 L338 410 L380 402 L384 410 L344 420 Z", True),
 ("buff", "M342 284 L520 470 L520 545 L482 545 L464 502 L450 456 L380 398 L372 392 Z", True),
 ("umber", "M346 290 Q430 254 520 250 L520 500 L512 506 L452 444 L400 360 Z", True),
 ("grey", "M520 520 L486 528 L420 556 L462 584 L500 616 L520 620 Z", True),
 ("white", "M316 630 Q392 566 482 600 L520 650 L520 716 Q420 664 316 630 Z", True),
 ("umber", "M268 692 Q384 630 520 716 L520 778 L512 778 L344 716 Z", True),
 ("black", "M340 730 L394 760 L392 1010 Z M428 768 L478 795 L474 1010 Z", True),
 ("black", "M492 514 L512 506 L532 514 L522 600 L512 670 L502 600 Z", False),
]
def svg(bg=True, size=1024, extra=""):
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 1024 1024">']
    if bg: out.append(f'  <rect width="1024" height="1024" fill="{C["night"]}"/>')
    out.append(f'  <circle cx="512" cy="512" r="408" fill="{C["sun"]}"/>')
    for col, d, mir in L:
        out.append(f'  <path fill="{C[col]}" d="{d}"/>')
        if mir: out.append(f'  <path fill="{C[col]}" transform="matrix(-1 0 0 1 1024 0)" d="{d}"/>')
    out.append(extra + "</svg>")
    return "\n".join(out)

inner = "\n".join(l for l in svg(bg=False).splitlines()[1:-1])
D = str(__import__("pathlib").Path(__file__).parent) + "/"
open(D + "owl.svg", "w").write(
 '<svg xmlns="http://www.w3.org/2000/svg" width="1024" height="1024" viewBox="0 0 1024 1024" role="img" aria-labelledby="title desc">\n'
 '  <title id="title">Offworld Nexus</title>\n'
 '  <desc id="desc">A geometric Eurasian eagle-owl with glowing amber eyes before a setting sun, on night blue.</desc>\n'
 f'  <rect width="1024" height="1024" fill="{C["night"]}"/>\n' + inner + "\n</svg>\n")
for scheme, bg, ink, acc, mut, d in [("light", "#f4efe3", "#161a20", "#b14d1c", "#56616b", "on warm paper"),
                                     ("dark", C["night"], "#f1ece0", "#ffa20f", "#a5acb8", "on night blue")]:
    art = "\n".join("    " + l for l in inner.splitlines())
    open(D + f"header-{scheme}.svg", "w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="260" viewBox="0 0 960 260" role="img" aria-labelledby="title desc">
  <title id="title">Offworld Nexus</title>
  <desc id="desc">Small birds in the cloud. A geometric eagle-owl with glowing amber eyes {d}.</desc>
  <defs><clipPath id="frame"><rect width="960" height="260" rx="8"/></clipPath></defs>
  <rect width="960" height="260" rx="8" fill="{bg}"/>
  <path fill="{acc}" d="M40 38h40v4H40Z"/>
  <text x="40" y="110" fill="{ink}" font-family="system-ui, sans-serif" font-size="54" font-weight="800" letter-spacing="-2">Offworld Nexus</text>
  <text x="42" y="153" fill="{acc}" font-family="system-ui, sans-serif" font-size="22">Small birds in the cloud.</text>
  <text x="42" y="210" fill="{mut}" font-family="ui-monospace, monospace" font-size="14" letter-spacing="0.5">LIBRARIES · HOME ASSISTANT · INFRASTRUCTURE</text>
  <g clip-path="url(#frame)">
    <svg x="630" y="10" width="300" height="250" viewBox="60 80 920 767">
{art}
    </svg>
  </g>
</svg>
''')

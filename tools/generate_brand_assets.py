from __future__ import annotations

import base64
import shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "assets" / "branding"
SVG = BRAND / "logos" / "svg"
RASTER = BRAND / "logos" / "raster"
EXPORTS = BRAND / "logos" / "exports"
REFS = BRAND / "logos" / "references"

BLUE = "#3054CD"
GOLD = "#CD8A30"
DARK = "#1A1A1A"

GLYPHS = {
    "A":("01110","10001","10001","11111","10001","10001","10001"),
    "C":("01111","10000","10000","10000","10000","10000","01111"),
    "E":("11111","10000","10000","11110","10000","10000","11111"),
    "G":("01111","10000","10000","10111","10001","10001","01111"),
    "H":("10001","10001","10001","11111","10001","10001","10001"),
    "I":("11111","00100","00100","00100","00100","00100","11111"),
    "L":("10000","10000","10000","10000","10000","10000","11111"),
    "M":("10001","11011","10101","10101","10001","10001","10001"),
    "N":("10001","11001","10101","10011","10001","10001","10001"),
    "O":("01110","10001","10001","10001","10001","10001","01110"),
    "P":("11110","10001","10001","11110","10000","10000","10000"),
    "R":("11110","10001","10001","11110","10100","10010","10001"),
    "S":("01111","10000","10000","01110","00001","00001","11110"),
    "T":("11111","00100","00100","00100","00100","00100","00100"),
    "W":("10001","10001","10001","10101","10101","10101","01010"),
    "&":("01100","10010","10100","01000","10101","10010","01101"),
}


def pixel_path(text: str, x: float, y: float, cell: float, gap: float = 2.0) -> tuple[str, float]:
    cmds: list[str] = []
    cursor = x
    for ch in text:
        if ch == " ":
            cursor += cell * 3.5
            continue
        rows = GLYPHS[ch]
        for row, bits in enumerate(rows):
            for col, bit in enumerate(bits):
                if bit == "1":
                    px, py = cursor + col * cell, y + row * cell
                    cmds.append(f"M{px:g} {py:g}h{cell:g}v{cell:g}h-{cell:g}z")
        cursor += cell * (5 + gap)
    return "".join(cmds), cursor - x


LINE_GLYPHS = {
    "A": "M0 1L.5 0L1 1M.2 .62H.8", "C": "M1 0H.2L0 .2V.8L.2 1H1",
    "E": "M1 0H0V1H1M0 .5H.78", "G": "M1 0H.2L0 .2V.8L.2 1H1V.55H.58",
    "H": "M0 0V1M1 0V1M0 .5H1", "I": "M0 0H1M.5 0V1M0 1H1",
    "L": "M0 0V1H1", "M": "M0 1V0L.5 .55L1 0V1", "N": "M0 1V0L1 1V0",
    "O": "M.2 0H.8L1 .2V.8L.8 1H.2L0 .8V.2Z", "P": "M0 1V0H.75L1 .2V.42L.75 .58H0",
    "R": "M0 1V0H.75L1 .2V.42L.75 .58H0M.58 .58L1 1", "S": "M1 .08L.8 0H.2L0 .2V.42L.2 .5H.8L1 .58V.8L.8 1H.2L0 .92",
    "T": "M0 0H1M.5 0V1", "W": "M0 0L.2 1L.5 .45L.8 1L1 0", "&": "M.9 .25L.75 .05H.3L.1 .25L.75 1H1M.55 .55L.2 1H0",
}


def line_path(text: str, height: float, tracking: float) -> tuple[str, float]:
    import re
    width = height * .62
    cursor = 0.0
    parts: list[str] = []
    for ch in text:
        if ch == " ":
            cursor += width * .65
            continue
        raw = LINE_GLYPHS[ch]
        tokens = re.findall(r"[A-Za-z]|-?(?:\d+(?:\.\d*)?|\.\d+)", raw)
        out: list[str] = []
        command = ""
        axis = 0
        for token in tokens:
            if token.isalpha():
                command, axis = token, 0
                out.append(token)
                continue
            value = float(token)
            if command.upper() == "H": value = cursor + value * width
            elif command.upper() == "V": value = value * height
            else:
                value = cursor + value * width if axis % 2 == 0 else value * height
                axis += 1
            out.append(f"{value:g}")
        parts.append(" ".join(out))
        cursor += width + tracking
    return " ".join(parts), cursor - tracking


def defs() -> str:
    return f'''<defs>
  <linearGradient id="blueMetal" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#87D7FF"/><stop offset=".34" stop-color="#368DFF"/><stop offset=".72" stop-color="{BLUE}"/><stop offset="1" stop-color="#16328E"/></linearGradient>
  <linearGradient id="goldMetal" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#FFF0A5"/><stop offset=".35" stop-color="#F2C44B"/><stop offset=".72" stop-color="{GOLD}"/><stop offset="1" stop-color="#72450B"/></linearGradient>
  <linearGradient id="silver" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#FFFFFF"/><stop offset=".30" stop-color="#DDEBFA"/><stop offset=".58" stop-color="#8DB6DF"/><stop offset=".82" stop-color="#F1F6FB"/><stop offset="1" stop-color="#6C94BE"/></linearGradient>
  <radialGradient id="void"><stop stop-color="#02040A"/><stop offset=".7" stop-color="#070B16"/><stop offset="1" stop-color="{DARK}"/></radialGradient>
  <linearGradient id="vortex" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#55E8FF"/><stop offset=".32" stop-color="#116EFF"/><stop offset=".62" stop-color="{BLUE}"/><stop offset=".78" stop-color="#F7C44A"/><stop offset="1" stop-color="{GOLD}"/></linearGradient>
  <filter id="glow" x="-35%" y="-35%" width="170%" height="170%"><feGaussianBlur stdDeviation="10" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <clipPath id="coreClip"><circle cx="512" cy="512" r="356"/></clipPath>
</defs>'''


def vector_core() -> str:
    curves = [
        ("M180 524C240 252 548 140 768 292C930 404 852 720 620 830C392 938 154 764 202 552", 72, .78),
        ("M252 646C126 430 354 192 602 226C864 262 920 548 750 716C558 904 282 820 252 646", 46, .72),
        ("M306 426C454 212 766 280 822 504C866 682 678 842 494 760C310 678 250 536 306 426", 30, .88),
        ("M742 368C904 526 766 800 530 794C318 788 234 560 350 414C456 282 634 278 742 368", 18, .94),
    ]
    paths = "".join(f'<path d="{d}" fill="none" stroke="url(#vortex)" stroke-width="{w}" stroke-linecap="round" opacity="{o}"/>' for d,w,o in curves)
    return f'''<g clip-path="url(#coreClip)"><circle cx="512" cy="512" r="350" fill="{DARK}" opacity=".96"/>
  <g filter="url(#glow)">{paths}</g><circle cx="512" cy="512" r="148" fill="url(#void)" stroke="#07132A" stroke-width="8"/></g>'''


def frame() -> str:
    return f'''<g aria-label="vector compass and orbital frame">
  <path d="M208 442A322 322 0 0 1 812 390" fill="none" stroke="#8A5A14" stroke-width="38" stroke-linecap="round"/>
  <path d="M208 442A322 322 0 0 1 812 390" fill="none" stroke="url(#goldMetal)" stroke-width="27" stroke-linecap="round"/>
  <path d="M198 500A322 322 0 0 0 824 500" fill="none" stroke="#10255E" stroke-width="38" stroke-linecap="round"/>
  <path d="M198 500A322 322 0 0 0 824 500" fill="none" stroke="url(#blueMetal)" stroke-width="27" stroke-linecap="round"/>
  <path d="M512 42l22 118-22 62-22-62z" fill="url(#goldMetal)" stroke="#70450A" stroke-width="5"/>
  <path d="M512 982l22-118-22-62-22 62z" fill="url(#blueMetal)" stroke="#10255E" stroke-width="5"/>
  <circle cx="512" cy="166" r="34" fill="url(#goldMetal)" stroke="#70450A" stroke-width="6"/>
  <circle cx="512" cy="858" r="34" fill="url(#blueMetal)" stroke="#10255E" stroke-width="6"/>
  <circle cx="203" cy="443" r="25" fill="url(#goldMetal)" stroke="#70450A" stroke-width="5"/>
  <circle cx="821" cy="392" r="25" fill="url(#blueMetal)" stroke="#10255E" stroke-width="5"/>
  <circle cx="512" cy="512" r="378" fill="none" stroke="{GOLD}" stroke-width="5" stroke-dasharray="4 14" opacity=".75"/>
  <circle cx="512" cy="512" r="392" fill="none" stroke="{BLUE}" stroke-width="4" stroke-dasharray="2 18" opacity=".8"/>
</g>'''


def wordmark_paths() -> str:
    # Custom geometric letterforms: 150-unit cells, 20-unit tracking.
    parts = [
        "M45 250V20H82L168 170V20H205V250H168L82 100V250Z",  # N
        "M235 250L315 20H390L470 250H425L406 192H299L280 250ZM312 153H393L352 61Z", # A
        "M500 250V20H660V62H545V118H648V160H545V250Z",
        "M690 250V20H850V62H735V118H838V160H735V250Z",
        "M880 250V20H925V250Z",
        "M955 250V20H992L1078 170V20H1115V250H1078L992 100V250Z",
    ]
    paths = "".join(f'<path d="{p}"/>' for p in parts)
    return f'''<g fill="url(#silver)" stroke="#B9D9F3" stroke-width="4" stroke-linejoin="round">{paths}</g>
<path d="M331 173l21-62 22 62z" fill="url(#goldMetal)" stroke="{GOLD}" stroke-width="3"/>'''


def embedded_core() -> str:
    payload = base64.b64encode((RASTER / "wormhole-core-2048.png").read_bytes()).decode("ascii")
    return f"data:image/png;base64,{payload}"


def lockup_svg(hybrid: bool) -> str:
    enterprise, ew = line_path("ENTERPRISES", 64, 19)
    tagline, tw = line_path("WORMHOLE LOGISTICS & OPERATIONS", 30, 9)
    core = f'<image href="{embedded_core()}" x="156" y="156" width="712" height="712" preserveAspectRatio="xMidYMid meet" clip-path="url(#coreClip)"/>' if hybrid else vector_core()
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1254 1254" role="img" aria-labelledby="title desc">
<title id="title">Naffin Enterprises logo</title><desc id="desc">Blue and gold wormhole compass emblem with Naffin Enterprises wordmark and Wormhole Logistics and Operations tagline.</desc>
{defs()}
<g transform="translate(227 18) scale(.78)">{core}{frame()}</g>
<g transform="translate(17 810) scale(1.095 .68)">{wordmark_paths()}</g>
<path d="{enterprise}" fill="none" stroke="url(#silver)" stroke-width="9" stroke-linejoin="miter" transform="translate({(1254-ew)/2:g} 1002)"/>
<path d="M92 1110H580" stroke="{BLUE}" stroke-width="8"/><circle cx="627" cy="1110" r="13" fill="{GOLD}"/><path d="M674 1110H1162" stroke="{GOLD}" stroke-width="8"/>
<path d="{tagline}" fill="none" stroke="#C9D8E7" stroke-width="4" stroke-linejoin="round" transform="translate({(1254-tw)/2:g} 1145)"/>
</svg>'''


def emblem_svg(hybrid: bool) -> str:
    core = f'<image href="{embedded_core()}" x="156" y="156" width="712" height="712" preserveAspectRatio="xMidYMid meet" clip-path="url(#coreClip)"/>' if hybrid else vector_core()
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" role="img" aria-labelledby="title desc">
<title id="title">Naffin Enterprises emblem</title><desc id="desc">Stylized vector wormhole surrounded by blue and gold navigation geometry.</desc>
{defs()}{core}{frame()}</svg>'''


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    names = ["bahnschrift.ttf", "seguisb.ttf" if bold else "segoeui.ttf", "arialbd.ttf" if bold else "arial.ttf"]
    for name in names:
        p = Path("C:/Windows/Fonts") / name
        if p.exists():
            return ImageFont.truetype(str(p), size=size)
    return ImageFont.load_default(size=size)


def draw_frame(canvas: Image.Image, scale: int) -> None:
    d = ImageDraw.Draw(canvas)
    b = (48,84,205,255); g = (205,138,48,255); pale=(130,210,255,255)
    box = [int(.185*scale), int(.17*scale), int(.815*scale), int(.80*scale)]
    d.arc(box, 202, 345, fill=g, width=max(2,int(.035*scale)))
    d.arc(box, 15, 158, fill=b, width=max(2,int(.035*scale)))
    d.ellipse([int(.477*scale),int(.105*scale),int(.523*scale),int(.151*scale)], fill=g)
    d.polygon([(scale//2,int(.02*scale)),(int(.515*scale),int(.14*scale)),(scale//2,int(.205*scale)),(int(.485*scale),int(.14*scale))], fill=g)
    d.ellipse([int(.477*scale),int(.845*scale),int(.523*scale),int(.891*scale)], fill=pale)
    d.polygon([(scale//2,int(.98*scale)),(int(.515*scale),int(.87*scale)),(scale//2,int(.805*scale)),(int(.485*scale),int(.87*scale))], fill=b)


def render_emblem(core: Image.Image, size: int) -> Image.Image:
    ss = max(4, 512 // size)
    big = size * ss
    canvas = Image.new("RGBA", (big,big), (0,0,0,0))
    core_size = int(big*.70)
    c = core.resize((core_size,core_size), Image.Resampling.LANCZOS)
    canvas.alpha_composite(c, ((big-core_size)//2, (big-core_size)//2))
    draw_frame(canvas,big)
    return canvas.resize((size,size), Image.Resampling.LANCZOS)


def tracked_text(draw: ImageDraw.ImageDraw, xy: tuple[int,int], text: str, font: ImageFont.FreeTypeFont, fill, tracking: int) -> int:
    x,y=xy
    for ch in text:
        draw.text((x,y),ch,font=font,fill=fill,stroke_width=max(1,font.size//70),stroke_fill=(70,100,135,255))
        x += int(draw.textlength(ch,font=font))+tracking
    return x


def render_lockup(core: Image.Image, width: int=1600) -> Image.Image:
    h=1600
    out=Image.new("RGBA",(width,h),(0,0,0,0))
    emblem=render_emblem(core,1060)
    out.alpha_composite(emblem,((width-1060)//2,0))
    d=ImageDraw.Draw(out)
    word=load_font(250,True); silver=(220,235,248,255)
    label="NAFFIN"; tracking=20
    lengths=[d.textlength(c,font=word) for c in label]; total=int(sum(lengths)+tracking*(len(label)-1))
    tracked_text(d,((width-total)//2,1010),label,word,silver,tracking)
    # Approved triangular gold counter/accent inside the A.
    ax=(width-total)//2+int(lengths[0])+tracking
    d.polygon([(ax+74,1223),(ax+118,1145),(ax+160,1223)],fill=(205,138,48,255))
    sub=load_font(92,False); subtext="ENTERPRISES"; sw=int(d.textlength(subtext,font=sub)+14*(len(subtext)-1))
    tracked_text(d,((width-sw)//2,1240),subtext,sub,(205,220,235,255),14)
    tag=load_font(45,True); t="WORMHOLE LOGISTICS & OPERATIONS"; tw=int(d.textlength(t,font=tag)+5*(len(t)-1))
    tracked_text(d,((width-tw)//2,1432),t,tag,(190,205,220,255),5)
    d.line((125,1390,710,1390),fill=(48,84,205,255),width=8); d.ellipse((788,1378,812,1402),fill=(205,138,48,255)); d.line((890,1390,1475,1390),fill=(205,138,48,255),width=8)
    return out


def main() -> None:
    for p in (SVG,RASTER,EXPORTS,REFS): p.mkdir(parents=True,exist_ok=True)
    shutil.copy2(Path(r"C:\Users\insai\Downloads\Naffin Enterprises Logo Transparent BG No Text.png"), REFS/"naffin-emblem-approved-reference.png")
    shutil.copy2(Path(r"C:\Users\insai\Downloads\Naffin Enterprises Logo Transparent BG.png"), REFS/"naffin-full-lockup-approved-reference.png")
    stored_core = RASTER / "wormhole-core-2048.png"
    generated=Path(r"C:\Users\insai\.codex\generated_images\01a0b088-27c2-73d0-b14e-c3ac701b1e7a\exec-b98eba7d-b152-451b-a50e-3a67ba8c571c.png")
    core_source = stored_core if stored_core.exists() else generated
    core=Image.open(core_source).convert("RGBA").resize((2048,2048),Image.Resampling.LANCZOS)
    core.save(RASTER/"wormhole-core-2048.png",optimize=True)
    # Approved transparent artwork is canonical. SVG experiments are retained
    # for design history, but are intentionally not regenerated.
    approved_emblem = Image.open(REFS/"naffin-emblem-approved-reference.png").convert("RGBA")
    approved_lockup = Image.open(REFS/"naffin-full-lockup-approved-reference.png").convert("RGBA")
    shutil.copy2(REFS/"naffin-emblem-approved-reference.png", RASTER/"naffin-emblem-master.png")
    shutil.copy2(REFS/"naffin-full-lockup-approved-reference.png", EXPORTS/"naffin-lockup-master.png")
    for size in (64,128,256,512):
        img=approved_emblem.resize((size,size), Image.Resampling.LANCZOS)
        img.save(RASTER/f"naffin-emblem-{size}.png",optimize=True)
        img.save(RASTER/f"naffin-emblem-{size}.webp",format="WEBP",lossless=True,method=6)
    lock=approved_lockup.resize((1600,1600), Image.Resampling.LANCZOS)
    lock.save(EXPORTS/"naffin-lockup-1600.png",optimize=True)
    lock.save(EXPORTS/"naffin-lockup-1600.webp",format="WEBP",lossless=True,method=6)


if __name__ == "__main__": main()

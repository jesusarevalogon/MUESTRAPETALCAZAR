#!/usr/bin/env python3
"""
Professional wireframe mockup generator for web development proposal.
Generates 9 PNG wireframe images using PIL/Pillow.
"""

from PIL import Image, ImageDraw, ImageFont
import os

# ── Color palette ──────────────────────────────────────────────────────────────
BG         = "#F8F9FA"
WHITE      = "#FFFFFF"
NAVY       = "#1a1a2e"
GOLD       = "#e8a020"
TEXT_DARK  = "#1a1a2e"
TEXT_MED   = "#555555"
TEXT_LIGHT = "#999999"
BORDER     = "#E0E0E0"
GREEN      = "#27ae60"
LIGHT_BLUE = "#EBF5FF"
LIGHT_GOLD = "#FFF8E7"
LIGHT_GRAY = "#E8E8E8"
PURPLE     = "#7c5cbf"
LIGHT_PURP = "#F5F0FF"
LIGHT_GRN  = "#F0FFF4"
GRAY_MED   = "#D5D5D5"

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Font loader ────────────────────────────────────────────────────────────────
def load_fonts():
    fonts = {}
    win_fonts = "C:/Windows/Fonts/"
    try:
        fonts["regular_sm"] = ImageFont.truetype(win_fonts + "arial.ttf", 11)
        fonts["regular"]    = ImageFont.truetype(win_fonts + "arial.ttf", 13)
        fonts["regular_md"] = ImageFont.truetype(win_fonts + "arial.ttf", 15)
        fonts["regular_lg"] = ImageFont.truetype(win_fonts + "arial.ttf", 18)
        fonts["bold_sm"]    = ImageFont.truetype(win_fonts + "arialbd.ttf", 11)
        fonts["bold"]       = ImageFont.truetype(win_fonts + "arialbd.ttf", 13)
        fonts["bold_md"]    = ImageFont.truetype(win_fonts + "arialbd.ttf", 16)
        fonts["bold_lg"]    = ImageFont.truetype(win_fonts + "arialbd.ttf", 22)
        fonts["bold_xl"]    = ImageFont.truetype(win_fonts + "arialbd.ttf", 28)
        fonts["bold_xxl"]   = ImageFont.truetype(win_fonts + "arialbd.ttf", 36)
        fonts["bold_hero"]  = ImageFont.truetype(win_fonts + "arialbd.ttf", 32)
        fonts["italic"]     = ImageFont.truetype(win_fonts + "ariali.ttf", 13)
    except Exception:
        default = ImageFont.load_default()
        for k in ["regular_sm","regular","regular_md","regular_lg",
                  "bold_sm","bold","bold_md","bold_lg","bold_xl","bold_xxl","bold_hero","italic"]:
            fonts[k] = default
    return fonts

FONTS = load_fonts()

# ── Drawing helpers ────────────────────────────────────────────────────────────
def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def draw_rect(draw, x, y, w, h, fill, outline=None, outline_width=1):
    draw.rectangle([x, y, x+w, y+h], fill=fill, outline=outline, width=outline_width)

def draw_rounded_rect(img_draw, x, y, w, h, radius, fill, outline=None, outline_width=1):
    """Simulate rounded corners."""
    d = img_draw
    # main body
    d.rectangle([x+radius, y, x+w-radius, y+h], fill=fill)
    d.rectangle([x, y+radius, x+w, y+h-radius], fill=fill)
    # corners
    d.ellipse([x, y, x+radius*2, y+radius*2], fill=fill)
    d.ellipse([x+w-radius*2, y, x+w, y+radius*2], fill=fill)
    d.ellipse([x, y+h-radius*2, x+radius*2, y+h], fill=fill)
    d.ellipse([x+w-radius*2, y+h-radius*2, x+w, y+h], fill=fill)
    if outline:
        d.arc([x, y, x+radius*2, y+radius*2], 180, 270, fill=outline, width=outline_width)
        d.arc([x+w-radius*2, y, x+w, y+radius*2], 270, 360, fill=outline, width=outline_width)
        d.arc([x, y+h-radius*2, x+radius*2, y+h], 90, 180, fill=outline, width=outline_width)
        d.arc([x+w-radius*2, y+h-radius*2, x+w, y+h], 0, 90, fill=outline, width=outline_width)
        d.line([x+radius, y, x+w-radius, y], fill=outline, width=outline_width)
        d.line([x+radius, y+h, x+w-radius, y+h], fill=outline, width=outline_width)
        d.line([x, y+radius, x, y+h-radius], fill=outline, width=outline_width)
        d.line([x+w, y+radius, x+w, y+h-radius], fill=outline, width=outline_width)

def shadow_card(draw, x, y, w, h, radius=6):
    """Draw a card shadow then white fill."""
    # shadow
    draw_rounded_rect(draw, x+3, y+3, w, h, radius, fill="#CCCCCC")
    # white card
    draw_rounded_rect(draw, x, y, w, h, radius, fill=WHITE, outline=BORDER, outline_width=1)

def draw_text_center(draw, text, cx, y, font, fill=TEXT_DARK):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text((cx - tw//2, y), text, font=font, fill=fill)

def draw_text(draw, text, x, y, font, fill=TEXT_DARK):
    draw.text((x, y), text, font=font, fill=fill)

def draw_button(draw, x, y, w, h, label, bg=GOLD, fg=WHITE, font=None, radius=5):
    if font is None:
        font = FONTS["bold"]
    draw_rounded_rect(draw, x, y, w, h, radius, fill=bg)
    bbox = draw.textbbox((0,0), label, font=font)
    tw, th = bbox[2]-bbox[0], bbox[3]-bbox[1]
    draw.text((x + (w-tw)//2, y + (h-th)//2 - 1), label, font=font, fill=fg)

def draw_pill(draw, x, y, label, bg, fg=WHITE, font=None):
    if font is None:
        font = FONTS["bold_sm"]
    bbox = draw.textbbox((0,0), label, font=font)
    tw = bbox[2]-bbox[0]
    pw, ph = tw + 16, 20
    draw_rounded_rect(draw, x, y, pw, ph, 10, fill=bg)
    draw.text((x+8, y+4), label, font=font, fill=fg)
    return pw

def draw_navbar(draw, img_w, title_text=None):
    """Standard navy top navbar 60px."""
    draw_rect(draw, 0, 0, img_w, 60, fill=NAVY)
    # logo placeholder box
    draw_rect(draw, 16, 12, 120, 36, fill=WHITE)
    draw_text(draw, "LOGO", 42, 22, FONTS["bold"], fill=NAVY)
    # nav links
    nav = "Inicio  |  Seguros  |  Quienes Somos  |  Contacto"
    bbox = draw.textbbox((0,0), nav, font=FONTS["regular"])
    tw = bbox[2]-bbox[0]
    draw.text((img_w - tw - 20, 22), nav, font=FONTS["regular"], fill=WHITE)

def draw_form_field(draw, x, y, w, label, h=34):
    """Gray form field with label."""
    draw_rect(draw, x, y, w, h, fill="#F2F2F2", outline=BORDER, outline_width=1)
    draw_text(draw, label, x+10, y+(h-14)//2, FONTS["regular"], fill=TEXT_LIGHT)

def draw_sidebar(draw, active_item="Dashboard"):
    """Navy left sidebar 220px."""
    draw_rect(draw, 0, 0, 220, 700, fill=NAVY)
    # logo area
    draw_rect(draw, 20, 15, 130, 35, fill=WHITE)
    draw_text(draw, "LOGO", 55, 23, FONTS["bold"], fill=NAVY)
    # menu items
    items = ["Dashboard","Prospectos","Clientes","Seguimiento","Reportes","Configuracion"]
    for i, item in enumerate(items):
        y = 80 + i * 48
        if item == active_item:
            draw_rect(draw, 0, y-8, 220, 38, fill="#2a2a4e")
            draw_rect(draw, 0, y-8, 4, 38, fill=GOLD)
            draw_text(draw, item, 28, y+5, FONTS["bold"], fill=GOLD)
        else:
            draw_text(draw, item, 28, y+5, FONTS["regular"], fill="#AAAACC")

def draw_topbar(draw, img_w, title, sidebar_w=220):
    """White topbar 60px."""
    draw_rect(draw, sidebar_w, 0, img_w-sidebar_w, 60, fill=WHITE, outline=BORDER, outline_width=1)
    draw_text(draw, title, sidebar_w+20, 20, FONTS["bold_lg"], fill=TEXT_DARK)
    # avatar
    av_x, av_y = img_w-70, 15
    draw.ellipse([av_x, av_y, av_x+32, av_y+32], fill=NAVY)
    draw_text(draw, "AG", av_x+7, av_y+8, FONTS["bold_sm"], fill=WHITE)
    draw_text(draw, "Agente", img_w-52, av_y+8, FONTS["regular_sm"], fill=TEXT_MED)

def draw_arrow_right(draw, x, y, length=40, color=NAVY, thickness=2):
    """Horizontal right arrow."""
    draw.line([x, y, x+length-8, y], fill=color, width=thickness)
    draw.polygon([(x+length-10, y-5), (x+length, y), (x+length-10, y+5)], fill=color)

# ─────────────────────────────────────────────────────────────────────────────
# FILE 1: Homepage
# ─────────────────────────────────────────────────────────────────────────────
def make_01_homepage():
    W, H = 1200, 700
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Navbar
    draw_navbar(d, W)

    # Hero section y=60, h=220
    draw_rect(d, 0, 60, W, 220, fill=LIGHT_GRAY)
    # Left half text
    draw_text(d, "Tu proteccion, en manos expertas", 50, 90, FONTS["bold_hero"], fill=NAVY)
    draw_text(d, "Seguros de Vida, Medico, Autos y Empresarial", 50, 140, FONTS["regular_lg"], fill=TEXT_MED)
    draw_button(d, 50, 185, 200, 44, "Solicitar informacion", bg=GOLD, fg=WHITE, font=FONTS["bold_md"])
    # Right half image placeholder
    draw_rounded_rect(d, 680, 75, 460, 190, 10, fill=GRAY_MED)
    draw_text_center(d, "[ Imagen ]", 910, 155, FONTS["regular_lg"], fill=TEXT_LIGHT)

    # Services strip y=280, h=120
    draw_rect(d, 0, 280, W, 120, fill=WHITE)
    draw_text_center(d, "Nuestros Servicios", W//2, 290, FONTS["bold_md"], fill=NAVY)
    services = [("Seguro Medico", "M"), ("Seguro de Vida", "V"), ("Autos", "A"), ("Empresarial", "E")]
    card_w = W // 4
    for i, (name, icon) in enumerate(services):
        cx = i * card_w + card_w // 2
        # icon circle
        ix, iy = cx - 20, 308
        d.ellipse([ix, iy, ix+36, iy+36], fill=NAVY)
        draw_text_center(d, icon, cx, iy+10, FONTS["bold"], fill=WHITE)
        draw_text_center(d, name, cx, iy+46, FONTS["bold_sm"], fill=NAVY)
        if i < 3:
            d.line([i*card_w+card_w, 295, i*card_w+card_w, 390], fill=BORDER, width=1)

    # Contact teaser y=400, h=100
    draw_rect(d, 0, 400, W, 100, fill=LIGHT_BLUE)
    draw_text_center(d, "Tienes dudas? Escribenos ahora", W//2, 418, FONTS["bold_lg"], fill=NAVY)
    draw_button(d, W//2 - 190, 455, 170, 38, "WhatsApp", bg=GREEN, fg=WHITE, font=FONTS["bold"])
    draw_button(d, W//2 + 20, 455, 140, 38, "Email", bg="#888888", fg=WHITE, font=FONTS["bold"])

    # Footer y=500
    draw_rect(d, 0, 500, W, 200, fill=NAVY)
    draw_text_center(d, "PUBLICIDAD ENFOQUE Y TALENTO", W//2, 575, FONTS["bold_md"], fill=WHITE)
    draw_text_center(d, "contacto@enfoqueytalento.com  |  www.enfoqueytalento.com", W//2, 610, FONTS["regular"], fill="#AAAACC")

    img.save(os.path.join(OUTPUT_DIR, "mockup_01_homepage.png"))
    print("  mockup_01_homepage.png saved")

# ─────────────────────────────────────────────────────────────────────────────
# FILE 2: Landing page seguro
# ─────────────────────────────────────────────────────────────────────────────
def make_02_landing_seguro():
    W, H = 1200, 700
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    draw_navbar(d, W)

    # Hero navy y=60 h=200
    draw_rect(d, 0, 60, W, 200, fill=NAVY)
    draw_text_center(d, "Seguro de Gastos Medicos Mayores", W//2, 90, FONTS["bold_xl"], fill=WHITE)
    draw_text_center(d, "Cobertura que cuida a tu familia cuando mas lo necesita", W//2, 130, FONTS["regular_lg"], fill="#CCCCDD")
    draw_button(d, W//2-90, 165, 180, 42, "Cotizar ahora", bg=GOLD, fg=WHITE, font=FONTS["bold_md"])

    # Two column section y=260, h=340
    draw_rect(d, 0, 260, W, 340, fill=WHITE)

    # Left col 55%
    lw = int(W * 0.55)
    draw_text(d, "Que incluye?", 50, 278, FONTS["bold_lg"], fill=NAVY)
    benefits = [
        "Cobertura en hospitales privados",
        "Atencion de urgencias 24/7",
        "Medicamentos incluidos",
        "Red nacional de medicos especializados",
    ]
    for i, b in enumerate(benefits):
        by = 318 + i * 50
        # checkmark circle
        d.ellipse([50, by, 74, by+24], fill=GREEN)
        draw_text(d, "v", 59, by+4, FONTS["bold_sm"], fill=WHITE)
        draw_text(d, b, 85, by+4, FONTS["regular_md"], fill=TEXT_DARK)

    # Right col 45% — white card
    rx = lw + 30
    rw = W - rx - 30
    shadow_card(d, rx, 268, rw, 310, radius=8)
    draw_text(d, "Solicita informacion", rx+20, 288, FONTS["bold_md"], fill=NAVY)
    fields = ["Nombre completo", "Telefono", "Correo electronico", "Tipo de seguro"]
    for i, f in enumerate(fields):
        fy = 320 + i * 52
        draw_form_field(d, rx+20, fy, rw-40, f)
    draw_button(d, rx+20, 548, rw-40, 38, "Enviar solicitud", bg=GOLD, fg=WHITE, font=FONTS["bold_md"])

    # Testimonial strip
    draw_rect(d, 0, 600, W, 100, fill=LIGHT_GOLD)
    draw_text_center(d, '"El tramite fue muy sencillo y la atencion excelente. Totalmente recomendado."', W//2, 632, FONTS["italic"], fill=TEXT_MED)
    draw_text_center(d, "— Maria G., cliente desde 2023", W//2, 658, FONTS["regular_sm"], fill=TEXT_LIGHT)

    img.save(os.path.join(OUTPUT_DIR, "mockup_02_landing_seguro.png"))
    print("  mockup_02_landing_seguro.png saved")

# ─────────────────────────────────────────────────────────────────────────────
# FILE 3: Mobile view
# ─────────────────────────────────────────────────────────────────────────────
def make_03_mobile():
    W, H = 400, 700
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Navy header 50px
    draw_rect(d, 0, 0, W, 50, fill=NAVY)
    draw_text(d, "ET Seguros", 14, 15, FONTS["bold"], fill=WHITE)
    # hamburger
    for i in range(3):
        draw_rect(d, W-40, 14+i*9, 24, 3, fill=WHITE)

    # Hero navy 180px
    draw_rect(d, 0, 50, W, 180, fill=NAVY)
    draw_text_center(d, "Tu seguro ideal", W//2, 80, FONTS["bold_xl"], fill=WHITE)
    draw_text_center(d, "Proteccion para ti y tu familia", W//2, 120, FONTS["regular"], fill="#CCCCDD")
    draw_button(d, W//2-80, 152, 160, 40, "Cotizar ahora", bg=GOLD, fg=WHITE, font=FONTS["bold"])

    # Service cards
    services = ["Seguro Medico", "Seguro de Vida", "Autos", "Empresarial"]
    icons = ["M", "V", "A", "E"]
    for i, (s, ic) in enumerate(zip(services, icons)):
        cy = 230 + i * 64
        bg_c = WHITE if i % 2 == 0 else "#F8F9FA"
        draw_rect(d, 0, cy, W, 62, fill=bg_c, outline=BORDER, outline_width=1)
        d.ellipse([16, cy+13, 46, cy+43], fill=NAVY)
        draw_text_center(d, ic, 31, cy+20, FONTS["bold_sm"], fill=WHITE)
        draw_text(d, s, 60, cy+20, FONTS["bold"], fill=NAVY)
        # arrow right indicator
        draw_text(d, ">", W-28, cy+20, FONTS["bold_md"], fill=TEXT_LIGHT)

    # CTA strip
    cta_y = 490
    draw_rect(d, 0, cta_y, W, 80, fill=GOLD)
    draw_text_center(d, "Contactanos ahora", W//2, cta_y+12, FONTS["bold_md"], fill=WHITE)
    # outlined button
    draw_rounded_rect(d, W//2-70, cta_y+40, 140, 30, 5, fill=GOLD, outline=WHITE, outline_width=2)
    draw_text_center(d, "WhatsApp", W//2, cta_y+46, FONTS["bold"], fill=WHITE)

    # Footer
    draw_rect(d, 0, 570, W, 130, fill=NAVY)
    draw_text_center(d, "PUBLICIDAD", W//2, 610, FONTS["bold_sm"], fill=WHITE)
    draw_text_center(d, "ENFOQUE Y TALENTO", W//2, 630, FONTS["bold_sm"], fill=GOLD)

    img.save(os.path.join(OUTPUT_DIR, "mockup_03_mobile.png"))
    print("  mockup_03_mobile.png saved")

# ─────────────────────────────────────────────────────────────────────────────
# FILE 4: Contact form page
# ─────────────────────────────────────────────────────────────────────────────
def make_04_formulario():
    W, H = 1200, 700
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    draw_navbar(d, W)

    # Page title
    draw_text_center(d, "Solicita tu cotizacion", W//2, 80, FONTS["bold_xl"], fill=NAVY)
    draw_text_center(d, "Completa el formulario y nos pondremos en contacto contigo", W//2, 120, FONTS["regular_lg"], fill=TEXT_MED)

    # White card 800px centered
    cx = (W - 800) // 2
    shadow_card(d, cx, 148, 800, 480, radius=10)

    # Form title
    draw_text(d, "Datos de contacto", cx+30, 168, FONTS["bold_lg"], fill=NAVY)

    # Two column fields
    fw = (800 - 90) // 2  # field width
    row1 = [(cx+30, "Nombre completo"), (cx+30+fw+30, "Empresa (opcional)")]
    row2 = [(cx+30, "Telefono"), (cx+30+fw+30, "Correo electronico")]

    for fx, label in row1:
        draw_form_field(d, fx, 210, fw, label)
    for fx, label in row2:
        draw_form_field(d, fx, 270, fw, label)

    # Dropdown full width
    draw_rect(d, cx+30, 330, 740, 34, fill="#F2F2F2", outline=BORDER, outline_width=1)
    draw_text(d, "Tipo de seguro", cx+40, 340, FONTS["regular"], fill=TEXT_LIGHT)
    draw_text(d, "v", cx+30+740-20, 342, FONTS["regular_sm"], fill=TEXT_MED)

    # Textarea full width
    draw_rect(d, cx+30, 390, 740, 80, fill="#F2F2F2", outline=BORDER, outline_width=1)
    draw_text(d, "Mensaje o consulta", cx+40, 400, FONTS["regular"], fill=TEXT_LIGHT)

    # Privacy note
    draw_text_center(d, "Al enviar aceptas nuestra politica de privacidad.", W//2, 488, FONTS["regular_sm"], fill=TEXT_LIGHT)

    # Gold button centered
    draw_button(d, W//2-100, 510, 200, 44, "Enviar solicitud", bg=GOLD, fg=WHITE, font=FONTS["bold_md"])

    img.save(os.path.join(OUTPUT_DIR, "mockup_04_formulario.png"))
    print("  mockup_04_formulario.png saved")

# ─────────────────────────────────────────────────────────────────────────────
# FILE 5: Admin dashboard
# ─────────────────────────────────────────────────────────────────────────────
def make_05_dashboard():
    W, H = 1200, 700
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    draw_sidebar(d, "Dashboard")
    draw_topbar(d, W, "Panel de Gestion")

    # Stat cards row
    cw, ch = 290, 110
    cards = [
        ("24", "Prospectos activos", NAVY),
        ("11", "Clientes activos", GREEN),
        ("7",  "Seguimientos hoy",  GOLD),
    ]
    for i, (num, label, color) in enumerate(cards):
        cx = 240 + i * (cw + 18)
        shadow_card(d, cx, 80, cw, ch, radius=8)
        draw_text(d, num, cx+20, 96, FONTS["bold_xxl"], fill=color)
        draw_text(d, label, cx+20, 148, FONTS["regular"], fill=TEXT_MED)

    # Activity table
    tx = 240
    tw = W - tx - 20
    draw_text(d, "Actividad reciente", tx, 215, FONTS["bold_lg"], fill=NAVY)

    # Table header
    draw_rect(d, tx, 240, tw, 36, fill=NAVY)
    cols = ["Nombre", "Seguro", "Estatus", "Fecha"]
    col_w = [tw//4] * 4
    for i, col in enumerate(cols):
        draw_text(d, col, tx + sum(col_w[:i]) + 14, 250, FONTS["bold_sm"], fill=WHITE)

    # Table rows
    rows = [
        ("Juan Perez",  "Medico", ("Contactado", GREEN,   WHITE), "Hoy"),
        ("Ana Ruiz",    "Autos",  ("Nuevo",       "#3498db", WHITE), "Ayer"),
        ("Carlos M.",   "Vida",   ("Propuesta",   GOLD,    WHITE), "22 abr"),
    ]
    for i, (name, seg, (status, sc, sf), fecha) in enumerate(rows):
        ry = 276 + i * 44
        bg = WHITE if i % 2 == 0 else "#F8F9FA"
        draw_rect(d, tx, ry, tw, 43, fill=bg, outline=BORDER, outline_width=1)
        draw_text(d, name,  tx+14,            ry+14, FONTS["regular"], fill=TEXT_DARK)
        draw_text(d, seg,   tx+col_w[0]+14,   ry+14, FONTS["regular"], fill=TEXT_MED)
        draw_pill(d, tx+col_w[0]+col_w[1]+14, ry+12, status, bg=sc, fg=sf)
        draw_text(d, fecha, tx+col_w[0]+col_w[1]+col_w[2]+14, ry+14, FONTS["regular"], fill=TEXT_MED)

    # Quick actions
    qa_y = 440
    draw_text(d, "Acciones rapidas", tx, qa_y, FONTS["bold_lg"], fill=NAVY)
    actions = ["+ Nuevo prospecto", "Registrar seguimiento", "Ver reportes"]
    for i, a in enumerate(actions):
        ax = tx + i * 210
        draw_button(d, ax, qa_y+30, 190, 38, a, bg=NAVY if i==0 else "#666666", fg=WHITE, font=FONTS["bold_sm"])

    img.save(os.path.join(OUTPUT_DIR, "mockup_05_dashboard.png"))
    print("  mockup_05_dashboard.png saved")

# ─────────────────────────────────────────────────────────────────────────────
# FILE 6: Prospects list
# ─────────────────────────────────────────────────────────────────────────────
def make_06_prospectos():
    W, H = 1200, 700
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    draw_sidebar(d, "Prospectos")
    draw_topbar(d, W, "Prospectos")

    # "Nuevo prospecto" button in topbar
    draw_button(d, W-200, 14, 180, 34, "+ Nuevo prospecto", bg=GOLD, fg=WHITE, font=FONTS["bold"])

    tx = 240
    tw = W - tx - 20

    # Search & filters
    draw_form_field(d, tx, 74, 320, "Buscar...", h=32)
    draw_form_field(d, tx+340, 74, 200, "Todos los seguros", h=32)
    draw_form_field(d, tx+560, 74, 200, "Todos los estatus", h=32)

    # Table
    ty = 120
    # Header
    draw_rect(d, tx, ty, tw, 36, fill=NAVY)
    hcols = ["#", "Nombre", "Telefono", "Seguro", "Estatus", "Ultima accion", "Ver"]
    hwidths = [40, 180, 160, 120, 140, 150, 70]
    hx = tx
    for col, cw in zip(hcols, hwidths):
        draw_text(d, col, hx+10, ty+10, FONTS["bold_sm"], fill=WHITE)
        hx += cw

    prospectos = [
        ("1","Juan Perez",  "55-1234-5678","Medico",     ("Contactado", GREEN,    WHITE)),
        ("2","Ana Ruiz",    "81-9876-5432","Autos",      ("Nuevo",      "#3498db",WHITE)),
        ("3","Carlos M.",   "33-5555-0011","Vida",       ("Propuesta",  GOLD,     WHITE)),
        ("4","Sofia L.",    "81-4444-7890","Empresarial",("En espera",  "#888888",WHITE)),
        ("5","Roberto V.",  "55-7777-3322","Medico",     ("Cerrado",    GREEN,    WHITE)),
    ]
    for i, (num, name, tel, seg, (status, sc, sf)) in enumerate(prospectos):
        ry = ty + 36 + i * 42
        bg = WHITE if i % 2 == 0 else "#F8F9FA"
        draw_rect(d, tx, ry, tw, 41, fill=bg, outline=BORDER, outline_width=1)
        vals = [num, name, tel, seg]
        rx = tx
        for val, cw2 in zip(vals, hwidths[:4]):
            draw_text(d, val, rx+10, ry+13, FONTS["regular"], fill=TEXT_DARK)
            rx += cw2
        # pill
        draw_pill(d, rx+10, ry+11, status, bg=sc, fg=sf)
        rx += hwidths[4]
        # date placeholder
        from datetime import datetime
        dates = ["24 abr","23 abr","22 abr","20 abr","18 abr"]
        draw_text(d, dates[i], rx+10, ry+13, FONTS["regular"], fill=TEXT_MED)
        rx += hwidths[5]
        # ver button
        draw_button(d, rx+10, ry+8, 44, 26, "Ver", bg=NAVY, fg=WHITE, font=FONTS["bold_sm"])

    img.save(os.path.join(OUTPUT_DIR, "mockup_06_prospectos.png"))
    print("  mockup_06_prospectos.png saved")

# ─────────────────────────────────────────────────────────────────────────────
# FILE 7: Client detail card
# ─────────────────────────────────────────────────────────────────────────────
def make_07_ficha_cliente():
    W, H = 1200, 700
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    draw_sidebar(d, "Clientes")
    draw_topbar(d, W, "Ficha de Cliente")

    tx = 240
    # White card
    shadow_card(d, tx+10, 74, W-tx-30, 600, radius=10)

    # Avatar + name
    ax, ay = tx+30, 90
    d.ellipse([ax, ay, ax+64, ay+64], fill=NAVY)
    draw_text_center(d, "JP", ax+32, ay+18, FONTS["bold_lg"], fill=WHITE)
    draw_text(d, "Juan Perez", ax+82, ay+8, FONTS["bold_xl"], fill=NAVY)
    draw_text(d, "Cliente activo  |  Seguro Medico GMM", ax+82, ay+44, FONTS["regular_md"], fill=TEXT_MED)

    # Divider
    d.line([tx+20, ay+80, W-20, ay+80], fill=BORDER, width=1)

    # Two columns
    ly = ay+100
    lx = tx+30
    rx = tx + (W-tx)//2 + 10

    # Left: Contact info
    draw_text(d, "Datos de contacto", lx, ly, FONTS["bold_md"], fill=NAVY)
    contacts = [
        ("Tel:", "55-1234-5678"),
        ("Email:", "juan@email.com"),
        ("Desde:", "Enero 2025"),
    ]
    for i, (label, val) in enumerate(contacts):
        iy = ly+32+i*34
        draw_text(d, label, lx, iy, FONTS["bold_sm"], fill=TEXT_MED)
        draw_text(d, val, lx+55, iy, FONTS["regular"], fill=TEXT_DARK)

    # Right: Insurance info
    draw_text(d, "Seguro activo", rx, ly, FONTS["bold_md"], fill=NAVY)
    insurance = [
        ("Tipo:", "GMM Familiar"),
        ("Renovacion:", "Enero 2026"),
    ]
    for i, (label, val) in enumerate(insurance):
        iy = ly+32+i*34
        draw_text(d, label, rx, iy, FONTS["bold_sm"], fill=TEXT_MED)
        draw_text(d, val, rx+100, iy, FONTS["regular"], fill=TEXT_DARK)
    # gold badge
    draw_pill(d, rx, ly+100, "Al corriente", bg=GREEN, fg=WHITE, font=FONTS["bold_sm"])

    # History table
    hy = ly+150
    draw_text(d, "Historial de seguimiento", lx, hy, FONTS["bold_md"], fill=NAVY)
    draw_rect(d, lx, hy+28, W-tx-50, 32, fill=NAVY)
    th_cols = ["Fecha", "Accion", "Notas", "Agente"]
    th_widths = [120, 220, 350, 120]
    hx2 = lx
    for col, cw in zip(th_cols, th_widths):
        draw_text(d, col, hx2+8, hy+37, FONTS["bold_sm"], fill=WHITE)
        hx2 += cw

    hist_rows = [
        ("24 abr", "Llamada de seguimiento", "Confirmo renovacion sin cambios", "Agente 1"),
        ("10 mar", "Envio cotizacion", "Solicito incluir cobertura dental", "Agente 1"),
        ("15 ene", "Registro inicial", "Captacion via referido", "Agente 2"),
    ]
    for i, row in enumerate(hist_rows):
        ry2 = hy+60+i*36
        bg = WHITE if i%2==0 else "#F8F9FA"
        draw_rect(d, lx, ry2, W-tx-50, 35, fill=bg, outline=BORDER, outline_width=1)
        rx2 = lx
        for val, cw in zip(row, th_widths):
            draw_text(d, val, rx2+8, ry2+10, FONTS["regular_sm"], fill=TEXT_DARK)
            rx2 += cw

    # Buttons
    btn_y = hy+60+3*36+16
    draw_button(d, lx, btn_y, 220, 38, "Registrar seguimiento", bg=GOLD, fg=WHITE, font=FONTS["bold"])
    draw_button(d, lx+238, btn_y, 160, 38, "Exportar ficha", bg="#888888", fg=WHITE, font=FONTS["bold"])

    img.save(os.path.join(OUTPUT_DIR, "mockup_07_ficha_cliente.png"))
    print("  mockup_07_ficha_cliente.png saved")

# ─────────────────────────────────────────────────────────────────────────────
# FILE 8: Flow diagram
# ─────────────────────────────────────────────────────────────────────────────
def make_08_flujo():
    W, H = 1200, 500
    img = Image.new("RGB", (W, H), WHITE)
    d = ImageDraw.Draw(img)

    draw_text_center(d, "Flujo de seguimiento comercial", W//2, 22, FONTS["bold_xl"], fill=NAVY)

    stages = [
        ("NUEVO",       "Registro inicial\ndel prospecto",   LIGHT_BLUE, NAVY,   NAVY),
        ("CONTACTADO",  "Primer contacto\nrealizado",        LIGHT_GOLD, GOLD,   GOLD),
        ("PROPUESTA",   "Cotizacion\nenviada",               LIGHT_PURP, PURPLE, PURPLE),
        ("NEGOCIACION", "En proceso\nde cierre",             LIGHT_GRN,  GREEN,  GREEN),
        ("CERRADO",     "Cliente\nactivo",                   GREEN,      WHITE,  WHITE),
    ]

    box_w, box_h = 170, 140
    total_w = len(stages)*box_w + (len(stages)-1)*50
    start_x = (W - total_w) // 2
    box_y = 70

    for i, (title, desc, bg, title_color, txt_color) in enumerate(stages):
        bx = start_x + i*(box_w+50)
        # box
        draw_rounded_rect(d, bx, box_y, box_w, box_h, 10,
                          fill=bg, outline=title_color, outline_width=2)
        # title
        draw_text_center(d, title, bx+box_w//2, box_y+18, FONTS["bold_md"], fill=title_color)
        # desc lines
        lines = desc.split("\n")
        for li, line in enumerate(lines):
            draw_text_center(d, line, bx+box_w//2, box_y+52+li*22, FONTS["regular_sm"], fill=txt_color if bg==GREEN else TEXT_MED)
        # step number
        d.ellipse([bx+box_w//2-14, box_y+100, bx+box_w//2+14, box_y+128], fill=title_color)
        draw_text_center(d, str(i+1), bx+box_w//2, box_y+107, FONTS["bold_sm"], fill=WHITE if title_color!=WHITE else NAVY)

        # Arrow between boxes
        if i < len(stages)-1:
            ax = bx + box_w + 5
            ay = box_y + box_h//2
            draw_arrow_right(d, ax, ay, length=42, color=NAVY, thickness=2)

    # Note box
    note_y = box_y + box_h + 40
    draw_rounded_rect(d, 80, note_y, W-160, 60, 8, fill="#F8F9FA", outline=BORDER, outline_width=1)
    draw_text_center(d, "Cada etapa registra: fecha, agente, notas y proxima accion programada.",
                     W//2, note_y+20, FONTS["regular_md"], fill=TEXT_MED)

    img.save(os.path.join(OUTPUT_DIR, "mockup_08_flujo.png"))
    print("  mockup_08_flujo.png saved")

# ─────────────────────────────────────────────────────────────────────────────
# FILE 9: Cover thumbnail
# ─────────────────────────────────────────────────────────────────────────────
def make_09_cover_thumb():
    W, H = 600, 400
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # Background accent stripe
    d.polygon([(0, H), (W//2, 0), (W, 0), (W, H)], fill="#242444")

    # Gold accent bar top
    draw_rect(d, 0, 0, W, 6, fill=GOLD)

    # Logo / brand area
    draw_rounded_rect(d, 30, 28, 120, 36, 5, fill=WHITE)
    draw_text(d, "LOGO", 60, 36, FONTS["bold_md"], fill=NAVY)

    # Main title
    draw_text_center(d, "Sistema de Gestion de Seguros", W//2, 82, FONTS["bold_xl"], fill=WHITE)
    draw_text_center(d, "Propuesta Web — Publicidad Enfoque y Talento", W//2, 120, FONTS["regular_lg"], fill=GOLD)

    # Mini mockup previews (3 small frames)
    frames = [
        (30,  155, 160, 110, "Homepage"),
        (215, 155, 160, 110, "Dashboard"),
        (400, 155, 160, 110, "Clientes"),
    ]
    for fx, fy, fw, fh, label in frames:
        shadow_card(d, fx, fy, fw, fh, radius=6)
        # mini navbar
        draw_rect(d, fx+2, fy+2, fw-4, 20, fill=NAVY)
        draw_text(d, label, fx+8, fy+6, FONTS["regular_sm"], fill=WHITE)
        # content lines
        for li in range(3):
            lx2 = fx+10
            lw2 = (fw-20) if li == 0 else (fw-20)*[0.8, 0.6, 0.7][li-1] if li>0 else fw-20
            draw_rect(d, lx2, fy+34+li*22, int(lw2), 10, fill=LIGHT_GRAY)
        # mini button
        draw_rect(d, fx+10, fy+fh-28, 70, 16, fill=GOLD)

    # Stat row
    stats = [("8", "Mockups"), ("3", "Modulos"), ("100%", "Responsivo")]
    for i, (num, label) in enumerate(stats):
        sx = 60 + i * 180
        draw_text_center(d, num, sx, 294, FONTS["bold_xl"], fill=GOLD)
        draw_text_center(d, label, sx, 328, FONTS["regular"], fill="#AAAACC")

    # Footer bar
    draw_rect(d, 0, H-40, W, 40, fill="#111120")
    draw_text_center(d, "PUBLICIDAD ENFOQUE Y TALENTO  —  Propuesta profesional de desarrollo web", W//2, H-26, FONTS["regular_sm"], fill="#888888")

    img.save(os.path.join(OUTPUT_DIR, "mockup_09_cover_thumb.png"))
    print("  mockup_09_cover_thumb.png saved")

# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(f"Generating mockups in: {OUTPUT_DIR}\n")
    make_01_homepage()
    make_02_landing_seguro()
    make_03_mobile()
    make_04_formulario()
    make_05_dashboard()
    make_06_prospectos()
    make_07_ficha_cliente()
    make_08_flujo()
    make_09_cover_thumb()

    print("\nVerification:")
    files = [
        "mockup_01_homepage.png",
        "mockup_02_landing_seguro.png",
        "mockup_03_mobile.png",
        "mockup_04_formulario.png",
        "mockup_05_dashboard.png",
        "mockup_06_prospectos.png",
        "mockup_07_ficha_cliente.png",
        "mockup_08_flujo.png",
        "mockup_09_cover_thumb.png",
    ]
    all_ok = True
    for f in files:
        path = os.path.join(OUTPUT_DIR, f)
        if os.path.exists(path):
            size = os.path.getsize(path)
            img = Image.open(path)
            print(f"  OK  {f:45s}  {img.size[0]}x{img.size[1]}  {size:,} bytes")
        else:
            print(f"  MISSING: {f}")
            all_ok = False
    print("\nAll done!" if all_ok else "\nSome files missing!")

"""
Generador de mockups UI profesionales para propuesta web - Corredora de Seguros
PUBLICIDAD ENFOQUE Y TALENTO, S.A. DE C.V.
"""
from PIL import Image, ImageDraw, ImageFont
import os

# ── Paleta ──────────────────────────────────────────────────────────────
NAVY      = (26,  26,  46)
NAVY_L    = (35,  35,  65)
GOLD      = (232, 160,  32)
GOLD_L    = (255, 195,  70)
WHITE     = (255, 255, 255)
OFF_WHITE = (248, 249, 250)
GRAY_LIGHT= (235, 237, 240)
GRAY_MID  = (180, 184, 191)
GRAY_DARK = (100, 105, 115)
TEXT_DARK = (30,  32,  40)
TEXT_MED  = (80,  85,  95)
GREEN     = (39, 174,  96)
ORANGE    = (230, 126,  34)
BLUE      = (52, 152, 219)
RED       = (231,  76,  60)
TEAL      = (26, 188, 156)

OUT = os.path.dirname(os.path.abspath(__file__))

def font(size, bold=False):
    """Retorna fuente disponible."""
    try:
        name = "arialbd.ttf" if bold else "arial.ttf"
        return ImageFont.truetype(name, size)
    except:
        try:
            b = "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"
            return ImageFont.truetype(b, size)
        except:
            return ImageFont.load_default()

def rounded_rect(draw, xy, radius, fill, outline=None, outline_w=2):
    x0,y0,x1,y1 = xy
    r = radius
    draw.rectangle([x0+r,y0,x1-r,y1], fill=fill)
    draw.rectangle([x0,y0+r,x1,y1-r], fill=fill)
    draw.pieslice([x0,y0,x0+2*r,y0+2*r], 180, 270, fill=fill)
    draw.pieslice([x1-2*r,y0,x1,y0+2*r], 270, 360, fill=fill)
    draw.pieslice([x0,y1-2*r,x0+2*r,y1], 90, 180, fill=fill)
    draw.pieslice([x1-2*r,y1-2*r,x1,y1], 0, 90, fill=fill)
    if outline:
        draw.arc([x0,y0,x0+2*r,y0+2*r], 180, 270, fill=outline, width=outline_w)
        draw.arc([x1-2*r,y0,x1,y0+2*r], 270, 360, fill=outline, width=outline_w)
        draw.arc([x0,y1-2*r,x0+2*r,y1], 90, 180, fill=outline, width=outline_w)
        draw.arc([x1-2*r,y1-2*r,x1,y1], 0, 90, fill=outline, width=outline_w)
        draw.line([x0+r,y0,x1-r,y0], fill=outline, width=outline_w)
        draw.line([x0+r,y1,x1-r,y1], fill=outline, width=outline_w)
        draw.line([x0,y0+r,x0,y1-r], fill=outline, width=outline_w)
        draw.line([x1,y0+r,x1,y1-r], fill=outline, width=outline_w)

def badge(draw, x, y, text, color, fw, fh, padding=8):
    w = fw + padding*2
    h = fh + padding
    rounded_rect(draw, [x, y, x+w, y+h], 6, color)
    draw.text((x+padding, y+padding//2), text, font=font(11, True), fill=WHITE)
    return w

def draw_browser_chrome(draw, img_w, y=0, h=44):
    draw.rectangle([0, y, img_w, y+h], fill=(245, 246, 248))
    draw.rectangle([0, y+h, img_w, y+h+1], fill=GRAY_MID)
    for i,c in enumerate([(220,80,60),(240,180,40),(50,180,80)]):
        draw.ellipse([12+i*22, y+14, 26+i*22, y+28], fill=c)
    rounded_rect(draw, [80, y+10, img_w-80, y+34], 12, WHITE, GRAY_MID, 1)
    txt = "corredoradeseguros.com"
    draw.text((img_w//2 - 80, y+16), txt, font=font(12), fill=GRAY_DARK)

def draw_mobile_chrome(draw, x, y, w, h):
    rounded_rect(draw, [x, y, x+w, y+h], 18, (50,50,60), (30,30,40), 3)
    draw.rectangle([x+3, y+30, x+w-3, y+h-20], fill=WHITE)
    draw.ellipse([x+w//2-15, y+8, x+w//2+15, y+22], fill=(80,80,90))

# ──────────────────────────────────────────────────────────────────────
# MOCKUP 1 — HOME PAGE
# ──────────────────────────────────────────────────────────────────────
def mockup_homepage():
    W, H = 1100, 780
    img = Image.new("RGB", (W, H), WHITE)
    d   = ImageDraw.Draw(img)

    draw_browser_chrome(d, W)

    # NAV
    d.rectangle([0, 44, W, 90], fill=NAVY)
    d.text((24, 58), "CorredoraSeguros", font=font(16, True), fill=WHITE)
    for i,t in enumerate(["Inicio","Seguros","Nosotros","Contacto"]):
        d.text((W-480+i*110, 62), t, font=font(13), fill=GRAY_LIGHT)
    rounded_rect(d, [W-115,54,W-15,82], 8, GOLD)
    d.text((W-105,62), "Cotizar ahora", font=font(12, True), fill=WHITE)

    # HERO
    d.rectangle([0, 90, W, 360], fill=NAVY_L)
    for i in range(15):
        alpha = 8 + i*2
        d.rectangle([0, 90+i*18, W, 108+i*18], fill=(*NAVY_L, alpha))
    d.text((60, 140), "Tu tranquilidad,", font=font(42, True), fill=WHITE)
    d.text((60, 192), "nuestra prioridad.", font=font(42, True), fill=GOLD)
    d.text((60, 252), "Seguros médicos, de vida, autos y más.", font=font(18), fill=GRAY_LIGHT)
    d.text((60, 282), "Asesoría personalizada para ti y tu familia.", font=font(16), fill=GRAY_MID)
    rounded_rect(d, [60, 318, 240, 352], 10, GOLD)
    d.text((80, 326), "Solicitar información", font=font(14, True), fill=WHITE)
    rounded_rect(d, [256, 318, 400, 352], 10, None, WHITE, 2)
    d.text((276, 326), "Ver servicios", font=font(14), fill=WHITE)
    # hero image placeholder
    rounded_rect(d, [W-370, 100, W-20, 350], 12, (40,42,65))
    d.text((W-280, 200), "[ Imagen ]", font=font(20), fill=GRAY_MID)
    d.text((W-270, 230), "Familia feliz", font=font(14), fill=(120,125,135))

    # SERVICIOS
    d.text((W//2-90, 378), "Nuestros Servicios", font=font(22, True), fill=TEXT_DARK)
    d.rectangle([W//2-30, 408, W//2+30, 411], fill=GOLD)

    cards = [("Seguro Médico","Cobertura GMM\ncompleta",BLUE), ("Seguro de Vida","Protege a los\nque más quieres",TEAL), ("Seguro de Autos","Cobertura total\nen carretera",NAVY), ("Empresarial","Protege tu\nnegocio",GREEN)]
    cw = 220; gap=20; total = len(cards)*cw+(len(cards)-1)*gap; sx=(W-total)//2
    for i,(title,desc,col) in enumerate(cards):
        cx = sx + i*(cw+gap)
        rounded_rect(d, [cx,420,cx+cw,620], 12, WHITE, GRAY_LIGHT, 1)
        d.rectangle([cx, 420, cx+cw, 465], fill=col)
        d.text((cx+cw//2-35, 435), title, font=font(14, True), fill=WHITE)
        for j,line in enumerate(desc.split("\n")):
            d.text((cx+20, 478+j*22), line, font=font(12), fill=TEXT_MED)
        rounded_rect(d, [cx+30, 575, cx+cw-30, 605], 8, col)
        d.text((cx+40, 582), "Ver más  →", font=font(12, True), fill=WHITE)

    # FOOTER strip
    d.rectangle([0, 720, W, 780], fill=NAVY)
    d.text((60, 742), "© 2026 Corredora de Seguros  |  Tel: _______  |  contacto@ejemplo.com", font=font(12), fill=GRAY_MID)

    img.save(os.path.join(OUT, "mockup_01_homepage.png"), dpi=(150,150))
    print("OK mockup_01_homepage.png")


# ──────────────────────────────────────────────────────────────────────
# MOCKUP 2 — LANDING SEGURO MÉDICO
# ──────────────────────────────────────────────────────────────────────
def mockup_landing_seguro():
    W, H = 1100, 780
    img = Image.new("RGB", (W, H), OFF_WHITE)
    d   = ImageDraw.Draw(img)

    draw_browser_chrome(d, W)

    # NAV
    d.rectangle([0, 44, W, 86], fill=NAVY)
    d.text((24, 58), "CorredoraSeguros", font=font(16, True), fill=WHITE)
    d.text((W-200, 62), "Inicio  |  Seguros  |  Contacto", font=font(12), fill=GRAY_LIGHT)

    # HERO seguro
    d.rectangle([0, 86, W//2+80, 260], fill=BLUE)
    d.text((40, 104), "Seguro de Gastos", font=font(30, True), fill=WHITE)
    d.text((40, 142), "Médicos Mayores (GMM)", font=font(24, True), fill=(180, 220, 255))
    d.text((40, 182), "Atención médica de calidad cuando", font=font(14), fill=GRAY_LIGHT)
    d.text((40, 202), "más lo necesitas, sin preocuparte", font=font(14), fill=GRAY_LIGHT)
    d.text((40, 222), "por los costos.", font=font(14), fill=GRAY_LIGHT)

    # Beneficios
    d.rectangle([0, 260, W//2+80, H], fill=WHITE)
    d.text((40, 278), "¿Qué incluye?", font=font(18, True), fill=TEXT_DARK)
    benefits = ["Red de hospitales y médicos", "Sin deducibles elevados", "Urgencias y hospitalización", "Medicamentos cubiertos", "Atención a nivel nacional", "Cobertura familiar disponible"]
    for i, b in enumerate(benefits):
        y = 310 + i * 40
        d.ellipse([40, y+6, 56, y+22], fill=BLUE)
        d.text((60, y+4), "✓", font=font(14, True), fill=WHITE)
        d.text((70, y+4), b, font=font(14), fill=TEXT_DARK)

    # FORM
    rounded_rect(d, [W//2+100, 94, W-20, 700], 12, WHITE, GRAY_LIGHT, 1)
    d.text((W//2+140, 114), "Solicita tu cotización", font=font(18, True), fill=TEXT_DARK)
    d.text((W//2+140, 140), "Sin costo, sin compromiso.", font=font(13), fill=GRAY_DARK)
    d.rectangle([W//2+100, 162, W-20, 163], fill=GOLD)

    fields = [("Nombre completo",""), ("Teléfono",""), ("Correo electrónico",""), ("Edad",""), ("¿Para quién es?","Individual / Familiar")]
    for i,(lbl, ph) in enumerate(fields):
        fy = 180 + i*90
        d.text((W//2+140, fy), lbl, font=font(12, True), fill=TEXT_DARK)
        rounded_rect(d, [W//2+140, fy+20, W-60, fy+56], 8, OFF_WHITE, GRAY_MID, 1)
        if ph:
            d.text((W//2+158, fy+30), ph, font=font(12), fill=GRAY_MID)

    rounded_rect(d, [W//2+140, 640, W-60, 676], 10, GOLD)
    d.text((W//2+200, 650), "Quiero mi cotización  →", font=font(14, True), fill=WHITE)
    d.text((W//2+155, 686), "* Tus datos están seguros con nosotros.", font=font(11), fill=GRAY_MID)

    img.save(os.path.join(OUT, "mockup_02_landing_seguro.png"), dpi=(150,150))
    print("OK mockup_02_landing_seguro.png")


# ──────────────────────────────────────────────────────────────────────
# MOCKUP 3 — VISTA MÓVIL
# ──────────────────────────────────────────────────────────────────────
def mockup_mobile():
    W, H = 420, 780
    img = Image.new("RGB", (W, H), (240, 242, 245))
    d   = ImageDraw.Draw(img)

    draw_mobile_chrome(d, 0, 0, W, H)

    # Content area inside phone
    cx, cw = 6, W-12

    # NAV
    d.rectangle([cx, 32, cx+cw, 66], fill=NAVY)
    d.text((cx+12, 44), "CorredoraSeguros", font=font(14, True), fill=WHITE)
    d.text((cx+cw-36, 44), "≡", font=font(22, True), fill=WHITE)

    # HERO
    d.rectangle([cx, 66, cx+cw, 200], fill=NAVY_L)
    d.text((cx+16, 82), "Tu tranquilidad,", font=font(18, True), fill=WHITE)
    d.text((cx+16, 108), "nuestra prioridad.", font=font(18, True), fill=GOLD)
    d.text((cx+16, 140), "Seguros para ti y tu familia.", font=font(12), fill=GRAY_LIGHT)
    rounded_rect(d, [cx+16, 162, cx+cw-16, 192], 8, GOLD)
    d.text((cx+55, 170), "Solicitar información", font=font(12, True), fill=WHITE)

    # Servicios cards (2 col)
    d.text((cx+cw//2-50, 210), "Servicios", font=font(16, True), fill=TEXT_DARK)
    services = [("Médico", BLUE), ("Vida", TEAL), ("Autos", NAVY), ("Empresarial", GREEN)]
    for i,(name, col) in enumerate(services):
        row, col_i = divmod(i, 2)
        sx = cx + 8 + col_i * (cw//2 - 4)
        sy = 238 + row * 90
        rounded_rect(d, [sx, sy, sx+cw//2-16, sy+78], 10, WHITE, GRAY_LIGHT, 1)
        d.rectangle([sx, sy, sx+cw//2-16, sy+30], fill=col)
        d.text((sx+10, sy+8), name, font=font(13, True), fill=WHITE)
        d.text((sx+10, sy+38), "Ver cobertura →", font=font(11), fill=col)

    # Contacto
    d.rectangle([cx, 430, cx+cw, 480], fill=OFF_WHITE)
    d.text((cx+20, 444), "¿Tienes dudas?  Escríbenos ahora", font=font(12), fill=TEXT_DARK)
    rounded_rect(d, [cx+20, 460, cx+cw-20, 492], 8, (37,211,102))
    d.text((cx+40, 468), "💬  Contactar por WhatsApp", font=font(12, True), fill=WHITE)

    # Footer
    d.rectangle([cx, 720, cx+cw, 760], fill=NAVY)
    d.text((cx+20, 734), "© 2026 Corredora de Seguros", font=font(11), fill=GRAY_MID)

    img.save(os.path.join(OUT, "mockup_03_mobile.png"), dpi=(150,150))
    print("OK mockup_03_mobile.png")


# ──────────────────────────────────────────────────────────────────────
# MOCKUP 4 — FORMULARIO DE CONTACTO
# ──────────────────────────────────────────────────────────────────────
def mockup_formulario():
    W, H = 900, 620
    img = Image.new("RGB", (W, H), OFF_WHITE)
    d   = ImageDraw.Draw(img)

    draw_browser_chrome(d, W)

    d.rectangle([0, 44, W, 88], fill=NAVY)
    d.text((24, 58), "CorredoraSeguros  —  Contacto", font=font(15, True), fill=WHITE)

    # Left info panel
    d.rectangle([0, 88, 320, H], fill=NAVY_L)
    d.text((30, 110), "Hablemos.", font=font(24, True), fill=WHITE)
    d.text((30, 148), "Estamos listos para", font=font(14), fill=GRAY_LIGHT)
    d.text((30, 168), "asesorarte sin costo.", font=font(14), fill=GRAY_LIGHT)
    d.rectangle([30, 196, 280, 198], fill=GOLD)
    info = [("📍", "Ciudad de México"), ("📞", "+52 (55) ___-____"), ("✉", "contacto@ejemplo.com"), ("🕐", "Lun–Vie  9am – 6pm")]
    for i,(ico,txt) in enumerate(info):
        d.text((30, 216+i*44), ico, font=font(14), fill=GOLD)
        d.text((60, 218+i*44), txt, font=font(13), fill=GRAY_LIGHT)
    rounded_rect(d, [30, 420, 200, 454], 8, (37,211,102))
    d.text((48, 429), "💬  WhatsApp", font=font(13, True), fill=WHITE)

    # Right form
    d.rectangle([320, 88, W, H], fill=WHITE)
    d.text((360, 106), "Envíanos un mensaje", font=font(20, True), fill=TEXT_DARK)
    d.text((360, 134), "Te respondemos en menos de 24 horas.", font=font(13), fill=GRAY_DARK)

    fields = [("Nombre completo", 166, 320, W-40), ("Correo electrónico", 254, 320, 600), ("Teléfono", 254, 620, W-40), ("¿En qué seguro estás interesado?", 342, 320, W-40)]
    for label, y, x0, x1 in fields:
        d.text((x0, y-22), label, font=font(12, True), fill=TEXT_DARK)
        rounded_rect(d, [x0, y, x1, y+36], 8, OFF_WHITE, GRAY_MID, 1)

    d.text((360, 390), "Mensaje (opcional)", font=font(12, True), fill=TEXT_DARK)
    rounded_rect(d, [360, 412, W-40, 510], 8, OFF_WHITE, GRAY_MID, 1)
    d.text((375, 425), "Escribe tu consulta aquí...", font=font(12), fill=GRAY_MID)

    rounded_rect(d, [360, 528, 560, 564], 10, GOLD)
    d.text((390, 538), "Enviar mensaje  →", font=font(13, True), fill=WHITE)
    d.text((360, 572), "* Tu información es confidencial y no se comparte con terceros.", font=font(11), fill=GRAY_MID)

    img.save(os.path.join(OUT, "mockup_04_formulario.png"), dpi=(150,150))
    print("OK mockup_04_formulario.png")


# ──────────────────────────────────────────────────────────────────────
# MOCKUP 5 — DASHBOARD INTERNO
# ──────────────────────────────────────────────────────────────────────
def mockup_dashboard():
    W, H = 1100, 740
    img = Image.new("RGB", (W, H), (236, 239, 244))
    d   = ImageDraw.Draw(img)

    # Sidebar
    d.rectangle([0, 0, 220, H], fill=NAVY)
    d.text((20, 24), "CRM Seguros", font=font(16, True), fill=WHITE)
    d.rectangle([0, 58, 220, 59], fill=(50,52,70))
    menu = [("🏠  Dashboard", True), ("👥  Prospectos", False), ("✅  Clientes", False), ("📋  Seguimientos", False), ("⚙️   Configuración", False)]
    for i,(item,active) in enumerate(menu):
        y = 72 + i*52
        if active:
            d.rectangle([0, y, 220, y+42], fill=GOLD)
            d.text((20, y+10), item, font=font(13, True), fill=WHITE)
        else:
            d.text((20, y+10), item, font=font(13), fill=GRAY_MID)

    # Top bar
    d.rectangle([220, 0, W, 56], fill=WHITE)
    d.rectangle([220, 56, W, 57], fill=GRAY_LIGHT)
    d.text((244, 18), "Dashboard", font=font(20, True), fill=TEXT_DARK)
    d.text((W-200, 20), "María González  ▾", font=font(13), fill=TEXT_MED)
    d.ellipse([W-240, 14, W-218, 36], fill=GOLD)

    # KPI Cards
    kpis = [("Prospectos activos","24","↑ 3 nuevos hoy", BLUE, "B"), ("Clientes activos","11","↑ 1 este mes", GREEN, "C"), ("Seguimientos pend.","7","Próximas 48 hrs", ORANGE, "S"), ("Cotizaciones env.","16","Este mes", TEAL, "Q")]
    cw = 196; gap = 12; sx = 238
    for i,(title,val,sub,col,letter) in enumerate(kpis):
        cx = sx + i*(cw+gap)
        rounded_rect(d, [cx, 74, cx+cw, 168], 10, WHITE, GRAY_LIGHT, 1)
        d.rectangle([cx, 74, cx+6, 168], fill=col)
        rounded_rect(d, [cx+cw-50, 84, cx+cw-10, 120], 8, col)
        d.text((cx+cw-38, 90), letter, font=font(20, True), fill=WHITE)
        d.text((cx+16, 86), title, font=font(11), fill=TEXT_MED)
        d.text((cx+16, 110), val, font=font(28, True), fill=TEXT_DARK)
        d.text((cx+16, 148), sub, font=font(10), fill=col)

    # Recent activity table
    rounded_rect(d, [238, 184, W-18, 480], 10, WHITE, GRAY_LIGHT, 1)
    d.text((258, 200), "Actividad reciente", font=font(15, True), fill=TEXT_DARK)
    rounded_rect(d, [W-160, 196, W-38, 222], 6, NAVY)
    d.text((W-148, 202), "+ Nuevo prospecto", font=font(11, True), fill=WHITE)

    headers = ["Nombre", "Teléfono", "Tipo de seguro", "Estatus", "Última acción"]
    widths = [180, 120, 160, 120, 220]
    hx = 258
    d.rectangle([238, 228, W-18, 254], fill=(245,247,252))
    for i,(h,w) in enumerate(zip(headers,widths)):
        d.text((hx, 236), h, font=font(11, True), fill=NAVY)
        hx += w

    rows = [("Juan Pérez","55-1234-5678","Médico GMM","Contactado","Llamar esta semana"), ("Ana Ruiz","81-8765-4321","Vida","Nuevo","Enviar propuesta"), ("Carlos Mendoza","33-9876-5432","Autos","Propuesta enviada","Dar seguimiento"), ("Laura Torres","55-2222-3333","Empresarial","Cerrado ✓","—"), ("Roberto García","81-4444-5555","Médico GMM","Nuevo","Agendar llamada")]
    status_colors = {"Contactado": BLUE, "Nuevo": ORANGE, "Propuesta enviada": TEAL, "Cerrado ✓": GREEN, "Nuevo": ORANGE}
    for ri,(name,phone,tipo,status,action) in enumerate(rows):
        y = 262 + ri*42
        if ri % 2 == 0:
            d.rectangle([238, y, W-18, y+38], fill=(249,250,253))
        cols_data = [name, phone, tipo, status, action]
        rx = 258
        for ci,(text,w) in enumerate(zip(cols_data, widths)):
            if ci == 3:
                sc = {"Contactado": BLUE, "Nuevo": ORANGE, "Propuesta enviada": TEAL, "Cerrado ✓": GREEN}.get(text, GRAY_DARK)
                badge(d, rx, y+9, text, sc, *d.textsize(text, font=font(11, True)) if hasattr(d,'textsize') else (len(text)*7, 14))
            else:
                d.text((rx, y+12), text, font=font(12), fill=TEXT_DARK)
            rx += w

    # Mini chart placeholder
    rounded_rect(d, [238, 494, 620, 720], 10, WHITE, GRAY_LIGHT, 1)
    d.text((258, 510), "Prospectos por tipo de seguro", font=font(14, True), fill=TEXT_DARK)
    bars = [("Médico", 0.72, BLUE), ("Vida", 0.44, GREEN), ("Autos", 0.56, ORANGE), ("Empresarial", 0.28, TEAL)]
    for i,(lbl,pct,col) in enumerate(bars):
        by = 546 + i*42
        d.text((258, by+6), lbl, font=font(12), fill=TEXT_MED)
        bw = int(250*pct)
        rounded_rect(d, [350, by, 350+bw, by+26], 6, col)
        d.text((356+bw, by+6), f"{int(pct*100)}%", font=font(11, True), fill=TEXT_DARK)

    # Next actions
    rounded_rect(d, [636, 494, W-18, 720], 10, WHITE, GRAY_LIGHT, 1)
    d.text((656, 510), "Próximas acciones", font=font(14, True), fill=TEXT_DARK)
    actions = [("Hoy", "Llamar a Juan Pérez — GMM", ORANGE), ("Hoy", "Enviar cotización a Ana Ruiz", BLUE), ("Mañana", "Seguimiento Carlos Mendoza", TEAL), ("Vie", "Reunión con prospecto corp.", NAVY)]
    for i,(dia,act,col) in enumerate(actions):
        ay = 540 + i*44
        d.rectangle([636, ay, 640, ay+34], fill=col)
        badge(d, 648, ay+4, dia, col, 30, 14, 6)
        d.text((648+50, ay+9), act, font=font(12), fill=TEXT_DARK)

    img.save(os.path.join(OUT, "mockup_05_dashboard.png"), dpi=(150,150))
    print("OK mockup_05_dashboard.png")


# ──────────────────────────────────────────────────────────────────────
# MOCKUP 6 — TABLA DE PROSPECTOS
# ──────────────────────────────────────────────────────────────────────
def mockup_prospectos():
    W, H = 1100, 680
    img = Image.new("RGB", (W, H), (236, 239, 244))
    d   = ImageDraw.Draw(img)

    # Sidebar slim
    d.rectangle([0, 0, 60, H], fill=NAVY)
    for i,ico in enumerate(["🏠","👥","✅","📋","⚙️"]):
        d.text((12, 20+i*56), ico, font=font(18), fill=GRAY_MID if i!=1 else GOLD)

    # Header
    d.rectangle([60, 0, W, 56], fill=WHITE)
    d.rectangle([60, 56, W, 57], fill=GRAY_LIGHT)
    d.text((84, 16), "Prospectos", font=font(22, True), fill=TEXT_DARK)
    rounded_rect(d, [W-180, 14, W-20, 44], 8, NAVY)
    d.text((W-164, 22), "+ Nuevo prospecto", font=font(12, True), fill=WHITE)

    # Filter bar
    d.rectangle([60, 57, W, 100], fill=(248, 249, 252))
    filters = [("Todos","active"), ("Nuevo",""), ("Contactado",""), ("Propuesta",""), ("Cerrado","")]
    fx = 84
    for label, active in filters:
        tw = len(label)*9+20
        if active:
            rounded_rect(d, [fx, 68, fx+tw, 90], 8, NAVY)
            d.text((fx+10, 72), label, font=font(12, True), fill=WHITE)
        else:
            rounded_rect(d, [fx, 68, fx+tw, 90], 8, WHITE, GRAY_LIGHT, 1)
            d.text((fx+10, 72), label, font=font(12), fill=TEXT_MED)
        fx += tw + 10
    rounded_rect(d, [W-240, 64, W-100, 92], 8, OFF_WHITE, GRAY_MID, 1)
    d.text((W-228, 72), "🔍  Buscar...", font=font(12), fill=GRAY_MID)

    # Table header
    d.rectangle([60, 100, W, 132], fill=NAVY)
    cols = [("#", 30), ("Nombre", 180), ("Teléfono", 130), ("Correo", 200), ("Seguro", 130), ("Estatus", 120), ("Última acción", 140), ("", 70)]
    hx = 78
    for (h, cw) in cols:
        d.text((hx, 112), h, font=font(12, True), fill=WHITE)
        hx += cw

    rows = [
        ("01","Juan Pérez López","55-1234-5678","juan@email.com","Médico GMM","Contactado","Hace 2 días"),
        ("02","Ana Ruiz Morales","81-8765-4321","ana@email.com","Vida","Nuevo","Hoy"),
        ("03","Carlos Mendoza","33-9876-5432","carlos@email.com","Autos","Propuesta","Ayer"),
        ("04","Laura Torres","55-2222-3333","laura@email.com","Empresarial","Cerrado ✓","Hace 5 días"),
        ("05","Roberto García","81-4444-5555","roberto@email.com","Médico GMM","Nuevo","Hoy"),
        ("06","Sofía Jiménez","55-9999-0001","sofia@email.com","Vida","Contactado","Hace 1 día"),
        ("07","Miguel Ángel R.","33-7777-8888","miguel@email.com","Autos","Propuesta","Hace 3 días"),
    ]
    status_map = {"Contactado": BLUE, "Nuevo": ORANGE, "Propuesta": TEAL, "Cerrado ✓": GREEN, "Propuesta enviada": TEAL}

    for ri, row_data in enumerate(rows):
        ry = 132 + ri*70
        bg = WHITE if ri%2==0 else (249,250,253)
        d.rectangle([60, ry, W, ry+68], fill=bg)
        d.rectangle([60, ry+67, W, ry+68], fill=GRAY_LIGHT)
        rx = 78
        for ci,(cell,(_, cw)) in enumerate(zip(row_data, cols)):
            if ci == 5:  # status badge
                sc = status_map.get(cell, GRAY_DARK)
                rounded_rect(d, [rx, ry+22, rx+cw-10, ry+46], 8, sc)
                d.text((rx+8, ry+27), cell, font=font(11, True), fill=WHITE)
            elif ci == 7:  # actions
                d.text((rx, ry+26), "Ver  Editar", font=font(11), fill=BLUE)
            else:
                d.text((rx, ry+26), cell, font=font(12 if ci>0 else 11), fill=TEXT_DARK)
            rx += cw

    # Pagination
    d.rectangle([60, H-44, W, H], fill=WHITE)
    d.rectangle([60, H-44, W, H-43], fill=GRAY_LIGHT)
    d.text((84, H-30), "Mostrando 7 de 24 prospectos", font=font(12), fill=TEXT_MED)
    for i,pg in enumerate(["◀", "1", "2", "3", "▶"]):
        px = W-220+i*40
        col = NAVY if pg=="1" else WHITE
        rounded_rect(d, [px, H-36, px+32, H-8], 6, col, GRAY_LIGHT, 1)
        d.text((px+8, H-32), pg, font=font(12, True if pg=="1" else False), fill=WHITE if pg=="1" else TEXT_MED)

    img.save(os.path.join(OUT, "mockup_06_prospectos.png"), dpi=(150,150))
    print("OK mockup_06_prospectos.png")


# ──────────────────────────────────────────────────────────────────────
# MOCKUP 7 — FICHA DE CLIENTE
# ──────────────────────────────────────────────────────────────────────
def mockup_ficha_cliente():
    W, H = 1100, 740
    img = Image.new("RGB", (W, H), (236, 239, 244))
    d   = ImageDraw.Draw(img)

    # Slim sidebar
    d.rectangle([0, 0, 60, H], fill=NAVY)
    for i,ico in enumerate(["🏠","👥","✅","📋","⚙️"]):
        d.text((12, 20+i*56), ico, font=font(18), fill=GRAY_MID)

    # Top bar
    d.rectangle([60, 0, W, 52], fill=WHITE)
    d.rectangle([60, 52, W, 53], fill=GRAY_LIGHT)
    d.text((84, 14), "← Prospectos  /  Juan Pérez López", font=font(14), fill=TEXT_MED)
    rounded_rect(d, [W-200, 10, W-100, 38], 8, NAVY)
    d.text((W-190, 16), "Editar ficha", font=font(12, True), fill=WHITE)
    rounded_rect(d, [W-90, 10, W-20, 38], 8, GREEN)
    d.text((W-82, 16), "✓ Cerrar", font=font(12, True), fill=WHITE)

    # Left panel — datos
    rounded_rect(d, [72, 64, 390, H-16], 12, WHITE, GRAY_LIGHT, 1)
    d.ellipse([160, 78, 230, 148], fill=NAVY_L)
    d.text((178, 96), "JP", font=font(28, True), fill=WHITE)
    d.text((250, 84), "Juan Pérez López", font=font(16, True), fill=TEXT_DARK)
    badge(d, 250, 112, "Contactado", BLUE, 90, 16)
    d.text((250, 140), "Prospecto desde: Enero 2026", font=font(11), fill=GRAY_DARK)
    d.rectangle([90, 162, 374, 164], fill=GRAY_LIGHT)

    d.text((90, 175), "Datos de contacto", font=font(13, True), fill=NAVY)
    contact = [("📞 Teléfono", "55-1234-5678"), ("✉  Correo", "juan@email.com"), ("📍 Ciudad", "Ciudad de México"), ("🎂 Edad", "38 años")]
    for i,(lbl,val) in enumerate(contact):
        y = 202 + i*46
        d.text((90, y), lbl, font=font(11), fill=GRAY_DARK)
        d.text((90, y+18), val, font=font(13, True), fill=TEXT_DARK)

    d.rectangle([90, 394, 374, 396], fill=GRAY_LIGHT)
    d.text((90, 406), "Interés de seguro", font=font(13, True), fill=NAVY)
    d.text((90, 430), "Tipo:", font=font(11), fill=GRAY_DARK)
    badge(d, 90, 448, "Seguro Médico GMM", BLUE, 140, 16)
    d.text((90, 480), "Familia: 4 integrantes", font=font(12), fill=TEXT_DARK)
    d.text((90, 504), "Presupuesto aprox.: $3,500/mes", font=font(12), fill=TEXT_DARK)

    d.rectangle([90, 524, 374, 526], fill=GRAY_LIGHT)
    d.text((90, 536), "Próxima acción", font=font(13, True), fill=NAVY)
    rounded_rect(d, [90, 556, 374, 596], 8, (255, 248, 230), (255, 200, 80), 1)
    d.text((104, 566), "📅  Llamar esta semana", font=font(12, True), fill=ORANGE)
    d.text((104, 584), "Presentar opciones de plan familiar", font=font(11), fill=TEXT_MED)

    # Right panel — historial
    rounded_rect(d, [400, 64, W-16, H-16], 12, WHITE, GRAY_LIGHT, 1)
    d.text((422, 80), "Historial de seguimiento", font=font(15, True), fill=TEXT_DARK)
    rounded_rect(d, [W-180, 72, W-36, 100], 8, NAVY)
    d.text((W-168, 80), "+ Registrar acción", font=font(11, True), fill=WHITE)
    d.rectangle([420, 108, W-36, 110], fill=GRAY_LIGHT)

    history = [
        ("Hoy, 10:15", "Llamada telefónica", "Se habló con Juan. Mostró interés en plan familiar. Enviará documentos esta semana.", GREEN, "María G."),
        ("Ayer, 16:40", "WhatsApp", "Se enviaron opciones de planes. Pidió tiempo para revisar con su esposa.", BLUE, "María G."),
        ("15 Ene", "Primera consulta", "Llegó por referido. Interesado en GMM familiar. Se agendó llamada de seguimiento.", TEAL, "María G."),
        ("12 Ene", "Registro inicial", "Prospecto creado desde formulario web. Pendiente primer contacto.", GRAY_MID, "Sistema"),
    ]
    for i, (fecha, tipo, nota, col, quien) in enumerate(history):
        hy = 118 + i * 140
        d.rectangle([420, hy, 432, hy+110], fill=col)
        rounded_rect(d, [440, hy, W-36, hy+120], 8, (249, 250, 253), GRAY_LIGHT, 1)
        d.text((456, hy+10), fecha, font=font(11), fill=GRAY_DARK)
        badge(d, 540, hy+6, tipo, col, len(tipo)*7, 14, 6)
        for j, line in enumerate(nota[:80].split(". ")[:2]):
            d.text((456, hy+36+j*22), line+".", font=font(12), fill=TEXT_DARK)
        d.text((456, hy+88), f"Registrado por: {quien}", font=font(11), fill=GRAY_MID)

    img.save(os.path.join(OUT, "mockup_07_ficha_cliente.png"), dpi=(150,150))
    print("OK mockup_07_ficha_cliente.png")


# ──────────────────────────────────────────────────────────────────────
# MOCKUP 8 — FLUJO DE SEGUIMIENTO
# ──────────────────────────────────────────────────────────────────────
def mockup_flujo():
    W, H = 1000, 500
    img = Image.new("RGB", (W, H), OFF_WHITE)
    d   = ImageDraw.Draw(img)

    d.text((W//2-180, 22), "Flujo de seguimiento comercial", font=font(22, True), fill=NAVY)
    d.rectangle([W//2-90, 58, W//2+90, 61], fill=GOLD)

    stages = [
        ("NUEVO","Prospecto recibido\nvía web o directo", ORANGE),
        ("CONTACTADO","Primer contacto\nrealizado", BLUE),
        ("PROPUESTA","Cotización\nenviada", TEAL),
        ("NEGOCIACIÓN","Revisión y\najustes", NAVY_L),
        ("CERRADO","Póliza firmada\ncon éxito", GREEN),
    ]
    sw = 148; sh = 100; gap = 26; sy = 120
    total_w = len(stages)*sw + (len(stages)-1)*gap
    sx = (W - total_w) // 2

    for i, (label, desc, col) in enumerate(stages):
        cx = sx + i*(sw+gap)
        # Arrow connector
        if i > 0:
            ax = cx - gap
            d.polygon([(ax, sy+sh//2-8),(ax+gap-2, sy+sh//2),(ax, sy+sh//2+8)], fill=col)

        rounded_rect(d, [cx, sy, cx+sw, sy+sh], 12, col)
        d.text((cx+sw//2-len(label)*5, sy+14), label, font=font(13, True), fill=WHITE)
        d.rectangle([cx+20, sy+36, cx+sw-20, sy+37], fill=(*WHITE, 80))
        for j, line in enumerate(desc.split("\n")):
            d.text((cx+14, sy+44+j*20), line, font=font(11), fill=WHITE)

        # Count badge
        counts = ["8","6","5","3","2"]
        rounded_rect(d, [cx+sw-28, sy-14, cx+sw-2, sy+12], 12, WHITE)
        d.text((cx+sw-22, sy-10), counts[i], font=font(13, True), fill=col)

    # Bottom labels
    labels2 = ["Registrar datos\ny asignar","Primera llamada\no WhatsApp","Enviar opciones\ny precios","Responder dudas,\nnegociar","Firma y\nactivación"]
    for i, lbl in enumerate(labels2):
        cx = sx + i*(sw+gap)
        for j, line in enumerate(lbl.split("\n")):
            d.text((cx+14, sy+sh+16+j*18), line, font=font(11), fill=TEXT_MED)

    # Legend
    d.text((sx, H-60), "Cada etapa registra:", font=font(13, True), fill=TEXT_DARK)
    items = ["  Fecha de contacto", "  Nombre del responsable", "  Nota de la interacción", "  Próxima acción programada"]
    for i, item in enumerate(items):
        ix = sx + (i%2)*290
        iy = H-40 + (i//2)*22
        d.text((ix, iy), "●" + item, font=font(12), fill=NAVY)

    img.save(os.path.join(OUT, "mockup_08_flujo.png"), dpi=(150,150))
    print("OK mockup_08_flujo.png")


# ──────────────────────────────────────────────────────────────────────
# COVER THUMB
# ──────────────────────────────────────────────────────────────────────
def mockup_cover_thumb():
    W, H = 900, 600
    img = Image.new("RGB", (W, H), NAVY)
    d   = ImageDraw.Draw(img)

    for i in range(H):
        r = int(NAVY[0] + (NAVY_L[0]-NAVY[0])*i/H)
        g = int(NAVY[1] + (NAVY_L[1]-NAVY[1])*i/H)
        b = int(NAVY[2] + (NAVY_L[2]-NAVY[2])*i/H)
        d.line([(0,i),(W,i)], fill=(r,g,b))

    d.rectangle([0, 0, 8, H], fill=GOLD)
    d.rectangle([0, H-8, W, H], fill=GOLD)
    d.text((60, 160), "PROPUESTA COMERCIAL", font=font(36, True), fill=WHITE)
    d.text((60, 214), "Desarrollo de Sitio Web", font=font(28), fill=GOLD)
    d.text((60, 254), "y Herramienta Digital", font=font(28), fill=GOLD)
    d.rectangle([60, 294, 420, 298], fill=GOLD)
    d.text((60, 312), "Para: Corredora de Seguros", font=font(18), fill=GRAY_LIGHT)
    d.text((60, 344), "PUBLICIDAD ENFOQUE Y TALENTO, S.A. DE C.V.", font=font(14), fill=GRAY_MID)
    d.text((60, 370), "2026  |  Propuesta v1.0", font=font(13), fill=GRAY_MID)

    rounded_rect(d, [60, 430, 280, 470], 10, GOLD)
    d.text((80, 440), "Versión profesional", font=font(15, True), fill=WHITE)

    img.save(os.path.join(OUT, "mockup_09_cover_thumb.png"), dpi=(150,150))
    print("OK mockup_09_cover_thumb.png")


if __name__ == "__main__":
    print("Generando mockups UI profesionales...")
    mockup_homepage()
    mockup_landing_seguro()
    mockup_mobile()
    mockup_formulario()
    mockup_dashboard()
    mockup_prospectos()
    mockup_ficha_cliente()
    mockup_flujo()
    mockup_cover_thumb()
    print("\n✅ Todos los mockups generados en:", OUT)

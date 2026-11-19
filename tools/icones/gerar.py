"""Ícones do Conduta no estilo da UI artist: desenho a lápis grafite com sombra de carvão.

Cada ícone = viewBox 64x64, fundo transparente (vai sobre a placa de metal), três camadas:
  sombra  -> áreas de carvão (hachura + mancha), atrás
  traco   -> o desenho principal, grafite com tremor de lápis
  realce  -> riscos claros finos (o "brilho" do metal arranhado)
"""
from pathlib import Path

OUT = Path(__file__).parent / "svg"
OUT.mkdir(exist_ok=True)
INK = "#222927"      # grafite (token grafite)
LIGHT = "#E8E6DC"    # aco-100, riscos de realce

def svg(name, seed, sombra, traco, realce=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
<title>{name}</title>
<defs>
<filter id="lapis" x="-10%" y="-10%" width="120%" height="120%">
<feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="{seed}" result="n"/>
<feDisplacementMap in="SourceGraphic" in2="n" scale="1.6" xChannelSelector="R" yChannelSelector="G"/>
</filter>
<filter id="carvao" x="-10%" y="-10%" width="120%" height="120%">
<feTurbulence type="fractalNoise" baseFrequency="1.4" numOctaves="2" seed="{seed + 7}" result="g"/>
<feColorMatrix in="g" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.6 1.5" result="m"/>
<feComposite in="SourceGraphic" in2="m" operator="in" result="s"/>
<feDisplacementMap in="s" in2="g" scale="2.2" xChannelSelector="R" yChannelSelector="G"/>
</filter>
<pattern id="hachura" width="2.6" height="2.6" patternUnits="userSpaceOnUse" patternTransform="rotate(-38)">
<line x1="0" y1="0" x2="0" y2="2.6" stroke="{INK}" stroke-width="1.2"/>
</pattern>
</defs>
<g filter="url(#carvao)" fill="url(#hachura)" stroke="none" opacity=".95">{sombra}</g>
<g filter="url(#lapis)" fill="none" stroke="{INK}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">{traco}</g>
<g fill="none" stroke="{LIGHT}" stroke-width=".8" stroke-linecap="round" opacity=".55">{realce}</g>
</svg>
"""

ICONS = {}
def icon(name, seed, sombra, traco, realce=""):
    ICONS[name] = svg(name, seed, sombra, traco, realce)

# ---------- condutas: o mesmo escudo, três estados ----------
ESCUDO = "M32 8 L50 14 C50 32 44 46 32 56 C20 46 14 32 14 14 Z"
icon("conduta_ordem", 3,
     f'<path d="M32 8 L50 14 C50 32 44 46 32 56 Z"/>',
     f'<path d="{ESCUDO}"/><path d="M32 16 V48 M22 26 H42" stroke-width="2.8"/><path d="M20 15.5 L32 11.5 L44 15.5" stroke-width="1.4" opacity=".7"/>',
     '<path d="M18 20 L26 13"/>')
icon("conduta_caos", 4,
     '<path d="M33 8 L50 14 C50 32 44 46 34 55 L37 38 L30 31 Z"/>',
     '<path d="M30 8.6 L14 14 C14 32 20 46 30 55.4 L27 39 L34 31 L28 22 Z"/><path d="M34 8 L50 14 C50 32 44 46 34 56 L37 39 L31 31 L37 21 Z"/><path d="M8 44 L12 41 M54 22 L58 19 M10 30 L7 29" stroke-width="1.8"/>',
     '<path d="M18 22 L24 15"/>')
icon("conduta_desconhecida", 5,
     '<path d="M14 14 L32 8 L32 56 C20 46 14 32 14 14 Z"/>',
     f'<path d="{ESCUDO}"/><path d="M25.5 24 C25.5 18 38.5 17.5 38.5 24.5 C38.5 29.5 32 29.5 32 35.5" stroke-width="3"/><circle cx="32" cy="43" r="1.6" fill="{INK}"/>',
     '<path d="M46 18 L42 24"/>')

# ---------- times ----------
icon("time_sobrevivente", 11,  # lamparina a querosene: a luz que mantém o abrigo
     '<path d="M23 30 C23 24 41 24 41 30 L41 44 C41 48 23 48 23 44 Z"/>',
     '<path d="M26 12 H38 M28 12 C24 12 22 16 22 20 L42 20 C42 16 40 12 36 12"/><path d="M24 20 L22 46 H42 L40 20"/><path d="M19 46 H45 V51 H19 Z"/><path d="M32 26 C29 30 29 34 32 37 C35 34 35 30 32 26 Z" stroke-width="2"/><path d="M22 20 C14 24 14 40 22 44 M42 20 C50 24 50 40 42 44" stroke-width="1.8"/><path d="M29 8 C29 5 35 5 35 8 V12" stroke-width="1.8"/>',
     '<path d="M26 24 L25 38"/>')
icon("time_opressor", 12,  # máscara de baile: ocultos entre os sobreviventes
     '<path d="M12 28 C12 22 22 22 32 27 C42 22 52 22 52 28 C52 38 44 40 38 36 C35 34 29 34 26 36 C20 40 12 38 12 28 Z"/>',
     '<path d="M10 27 C10 20 22 20 32 25 C42 20 54 20 54 27 C54 39 44 42 38 37 C35 35 29 35 26 37 C20 42 10 39 10 27 Z"/><path d="M17 29 C19 26 25 26 27 30 C24 32 19 32 17 29 Z" stroke-width="2"/><path d="M37 30 C39 26 45 26 47 29 C45 32 40 32 37 30 Z" stroke-width="2"/><path d="M54 25 L60 21 M54 29 C58 36 55 46 52 52" stroke-width="1.8"/>',
     '<path d="M14 24 L20 22"/>')
icon("time_mercenario", 13,  # punhal: contratado para um alvo
     '<path d="M30 14 L34 14 L36 36 L28 36 Z"/>',
     '<path d="M32 6 L37 36 H27 Z"/><path d="M32 10 V33" stroke-width="1.2"/><path d="M20 37 H44" stroke-width="3.2"/><path d="M28.5 40 H35.5 V52 H28.5 Z"/><path d="M28.5 44 H35.5 M28.5 48 H35.5" stroke-width="1.4"/><circle cx="32" cy="56" r="2.6"/>',
     '<path d="M33.5 14 L35 30"/>')
icon("time_fanatico", 14,  # vela votiva: o sacrifício da mesa
     '<path d="M25 30 H39 V52 H25 Z"/>',
     '<path d="M24 28 H40 V53 H24 Z"/><path d="M24 33 C28 35 30 31 33 34 C35 36 38 33 40 34" stroke-width="1.8"/><path d="M18 53 H46 L44 57 H20 Z"/><path d="M32 28 V24"/><path d="M32 8 C26 15 27 21 32 24 C37 21 38 15 32 8 Z"/><path d="M32 15 C30 18 30 20 32 21.5" stroke-width="1.6"/>',
     '<path d="M27 37 L27 48"/>')

# ---------- habilidades ----------
icon("habilidade_ordem_analise_profunda", 21,  # lupa sobre a ficha
     '<circle cx="27" cy="27" r="11"/>',
     '<circle cx="27" cy="27" r="14"/><path d="M37 37 L52 52" stroke-width="5"/><path d="M50 50 L54 54" stroke-width="6.5"/><path d="M20 22 H33 M20 27 H30 M20 32 H31" stroke-width="1.6"/>',
     '<path d="M18 21 C19 17 22 15 25 14.5"/>')
icon("habilidade_ordem_execucao", 22,  # forca
     '<path d="M27 34 C27 26 37 26 37 34 C37 42 27 42 27 34 Z"/>',
     '<path d="M14 58 V8 H44 M14 16 L22 8" stroke-width="3.2"/><path d="M38 8 V22"/><path d="M36 22 H40 V27 H36 Z" stroke-width="1.8"/><path d="M32 27 C25 28 25 41 32 42 C39 41 39 28 32 27" stroke-width="2.2"/><path d="M8 58 H24"/>',
     '<path d="M16 22 L16 40"/>')
icon("habilidade_ordem_reanimar", 23,  # coração e batimento
     '<path d="M32 50 C20 42 12 34 14 24 C16 17 26 15 32 23 Z"/>',
     '<path d="M32 52 C20 44 10 35 12 24 C14 15 26 13 32 22 C38 13 50 15 52 24 C54 35 44 44 32 52 Z"/><path d="M8 34 H21 L25 27 L30 41 L35 30 L38 34 H56" stroke-width="2.2"/>',
     '<path d="M17 21 C18 18 21 17 24 17.5"/>')
icon("habilidade_desconhecido_falsificacao", 31,  # pena sobre documento
     '<path d="M14 14 H38 V52 H14 Z"/>',
     '<path d="M12 10 H40 L46 16 V54 H12 Z"/><path d="M40 10 V16 H46" stroke-width="1.8"/><path d="M18 22 H34 M18 28 H36 M18 34 H28" stroke-width="1.6"/><path d="M58 8 C46 12 36 26 32 42 C42 34 52 24 58 8 Z"/><path d="M32 42 L28 50" stroke-width="2"/><path d="M58 8 L38 34" stroke-width="1.2"/><path d="M18 46 C22 42 25 48 29 44" stroke-width="1.6"/>',
     '<path d="M16 14 L16 26"/>')
icon("habilidade_desconhecido_voto_secreto", 32,  # urna com envelope
     '<path d="M12 34 H52 V54 H12 Z"/>',
     '<path d="M10 30 H54 V56 H10 Z"/><path d="M10 30 L16 22 H48 L54 30"/><path d="M26 26 H38" stroke-width="3"/><path d="M24 26 V8 H40 V26" stroke-width="2.2"/><path d="M24 8 L32 15 L40 8" stroke-width="1.8"/><path d="M26 42 H38" stroke-width="1.6"/>',
     '<path d="M14 36 L14 50"/>')
icon("habilidade_desconhecido_ultimas_palavras", 33,  # carta com selo de cera
     '<circle cx="40" cy="40" r="7"/>',
     '<path d="M8 16 H56 V48 H8 Z"/><path d="M8 16 L32 34 L56 16" stroke-width="2.2"/><path d="M8 48 L26 30 M56 48 L38 30" stroke-width="1.6"/><circle cx="40" cy="40" r="7.5"/><path d="M37 38 L40 43 L43 38" stroke-width="1.6"/><path d="M35 46 L33 52 M45 46 L47 51" stroke-width="1.6"/>',
     '<path d="M12 20 L20 26"/>')
icon("habilidade_caos_sequestro", 41,  # algemas em diagonal, ligadas por corrente
     '<path d="M8 22 C8 12 26 12 26 22 C26 30 8 30 8 22 Z"/><path d="M38 44 C38 34 56 34 56 44 C56 52 38 52 38 44 Z"/>',
     '<ellipse cx="17" cy="21" rx="11" ry="9.5"/><ellipse cx="17" cy="21" rx="6" ry="5" stroke-width="1.6"/><path d="M24 26 L29 31 L26 34 L21 29" stroke-width="2.2"/>'
     '<ellipse cx="47" cy="43" rx="11" ry="9.5"/><ellipse cx="47" cy="43" rx="6" ry="5" stroke-width="1.6"/><path d="M40 38 L35 33 L38 30 L43 35" stroke-width="2.2"/>'
     '<ellipse cx="31" cy="30" rx="3" ry="2" transform="rotate(45 31 30)" stroke-width="1.8"/><ellipse cx="33.5" cy="32.5" rx="3" ry="2" transform="rotate(-45 33.5 32.5)" stroke-width="1.8"/>',
     '<path d="M9 18 C10 15 12 13 15 12.5"/>')
icon("habilidade_caos_manipulacao_de_dados", 42,  # pasta de arquivo rasurada
     '<path d="M8 22 H56 V52 H8 Z"/>',
     '<path d="M6 16 H24 L28 21 H58 V54 H6 Z"/><path d="M6 25 H58" stroke-width="1.6"/><path d="M14 34 H34 M14 41 H28" stroke-width="1.8"/><path d="M12 33 L36 35" stroke-width="3"/><path d="M50 30 L36 50 L33 52 L34 48 L48 28 Z" stroke-width="2"/><path d="M46 31 L49 33" stroke-width="1.6"/>',
     '<path d="M10 19 L20 19"/>')
icon("habilidade_caos_infeccao", 43,  # seringa com gotas
     '<path d="M30 20 L46 36 L40 42 L24 26 Z"/>',
     '<path d="M22 22 L42 42 L36 48 L16 28 Z" transform="translate(4 -4)"/><path d="M44 38 L54 48 M50 44 L58 36" stroke-width="2.6"/><path d="M28 18 L34 12 M20 26 L14 32" stroke-width="2"/><path d="M23 21 L13 11 M10 14 L16 8" stroke-width="2.6"/><path d="M28 24 L31 21 M32 28 L35 25 M36 32 L39 29" stroke-width="1.4"/><path d="M14 46 C12 50 12 52 14 54 C16 52 16 50 14 46 Z M22 52 C21 55 21 56 22 58 C23 56 23 55 22 52 Z" stroke-width="1.6"/>',
     '<path d="M32 22 L40 30"/>')

# ---------- interface / features ----------
icon("interface_grupo_social", 51,
     '<path d="M8 54 C8 44 16 40 22 40 C28 40 36 44 36 54 Z"/>',
     '<circle cx="22" cy="28" r="7"/><path d="M8 54 C8 44 15 40 22 40 C29 40 36 44 36 54"/><circle cx="42" cy="24" r="6" stroke-width="2"/><path d="M36 38 C38 36 40 35 42 35 C49 35 56 40 56 50" stroke-width="2"/><circle cx="12" cy="22" r="4.5" stroke-width="1.6"/><path d="M4 40 C4 34 8 31 12 31" stroke-width="1.6"/>',
     '<path d="M18 24 L20 22"/>')
icon("interface_times", 52,  # bandeiras cruzadas
     '<path d="M27 10 C21 8 15 13 7 10 L9 26 C17 29 22 24 29 27 Z"/>',
     '<path d="M14 58 L30 8 M50 58 L34 8" stroke-width="2.8"/>'
     '<path d="M29 11 C22 8 15 14 6 10 L9 27 C17 30 22 24 28 28"/>'
     '<path d="M35 11 C42 8 49 14 58 10 L55 27 C47 30 42 24 36 28" stroke-width="2.2"/>'
     '<circle cx="30" cy="7" r="1.6" fill="#222927"/><circle cx="34" cy="7" r="1.6" fill="#222927"/>',
     '<path d="M16 50 L24 26"/>')
icon("interface_perfil", 53,  # crachá / carteirinha
     '<path d="M14 22 H30 V44 H14 Z"/>',
     '<path d="M8 16 H56 V50 H8 Z"/><path d="M26 10 H38 V18 H26 Z" stroke-width="2"/><path d="M14 22 H30 V44 H14 Z" stroke-width="1.8"/><circle cx="22" cy="30" r="4" stroke-width="1.8"/><path d="M16 42 C16 37 28 37 28 42" stroke-width="1.8"/><path d="M36 26 H50 M36 32 H48 M36 38 H44" stroke-width="1.8"/>',
     '<path d="M10 20 L18 20"/>')
icon("interface_comunicacao", 54,  # balões de conversa
     '<path d="M30 30 H56 V48 H48 L44 54 L42 48 H30 Z"/>',
     '<path d="M6 10 H38 V32 H20 L12 40 V32 H6 Z"/><path d="M28 30 H58 V50 H50 L44 56 L44 50 H28 Z" stroke-width="2.2"/><path d="M12 18 H32 M12 24 H26" stroke-width="1.6"/>',
     '<path d="M9 13 L16 13"/>')
icon("controle_editar", 55,  # caderno com lápis
     '<path d="M12 10 H34 V56 H12 Z"/>',
     '<path d="M12 8 H44 V58 H12 Z"/><path d="M12 14 H8 M12 22 H8 M12 30 H8 M12 38 H8 M12 46 H8 M12 54 H8" stroke-width="2"/><path d="M20 18 H36 M20 26 H34 M20 34 H30" stroke-width="1.6"/><path d="M56 22 L36 50 L32 54 L33 49 L52 19 Z" stroke-width="2"/><path d="M50 22 L53 24" stroke-width="1.6"/>',
     '<path d="M16 12 L16 24"/>')
icon("interface_atualizar", 56,  # plugue: a partida não morre se alguém cair
     '<path d="M22 18 H42 V34 C42 40 22 40 22 34 Z"/>',
     '<path d="M20 18 H44 V32 C44 42 20 42 20 32 Z"/><path d="M26 18 V8 M38 18 V8" stroke-width="3.2"/><path d="M32 41 V48 C32 54 40 56 46 54 C52 52 54 56 56 60"/><path d="M8 34 C10 26 14 22 18 20 M56 30 C54 24 50 22 46 21" stroke-width="1.6"/>',
     '<path d="M24 22 L24 32"/>')
icon("interface_jogar", 57,  # celular com o jogo
     '<path d="M20 12 H44 V48 H20 Z"/>',
     '<path d="M18 6 H46 V58 H18 Z"/><path d="M18 12 H46 M18 50 H46" stroke-width="1.8"/><circle cx="32" cy="54" r="2" stroke-width="1.6"/><path d="M28 24 L40 31 L28 38 Z" stroke-width="2.4"/>',
     '<path d="M22 16 L22 28"/>')
icon("ficha_retida", 61,  # silhueta trancada
     '<path d="M14 58 C14 44 22 38 32 38 C42 38 50 44 50 58 Z"/><circle cx="32" cy="22" r="10"/>',
     '<circle cx="32" cy="22" r="11"/><path d="M12 58 C12 44 21 37 32 37 C43 37 52 44 52 58"/><path d="M36 44 H54 V58 H36 Z" stroke-width="2.4"/><path d="M40 44 V40 C40 34 50 34 50 40 V44" stroke-width="2.4"/><circle cx="45" cy="50" r="1.8" fill="#222927"/>',
     '<path d="M24 16 L27 13"/>')

for name, txt in ICONS.items():
    (OUT / f"{name}.svg").write_text(txt, encoding="utf-8")

# folha de contato para revisão no navegador
cells = "".join(
    f'<figure><div class="placa"><img src="svg/{n}.svg"></div><figcaption>{n}</figcaption></figure>' for n in ICONS)
(Path(__file__).parent / "folha.html").write_text(f"""<!doctype html><meta charset="utf-8"><title>Ícones v2</title>
<style>body{{background:#282A24;color:#E8E6DC;font:12px system-ui;margin:16px}}main{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:14px}}
figure{{margin:0;text-align:center}}.placa{{width:112px;height:112px;margin:auto;background:#8F918C;display:grid;place-items:center;
box-shadow:inset 0 0 0 2px #63635F,inset 0 0 0 4px #A8A79F,0 4px 0 #1C1E1B}}.placa img{{width:84px;height:84px}}
figcaption{{margin-top:6px;opacity:.7;font-size:10px;word-break:break-all}}</style><main>{cells}</main>""", encoding="utf-8")
print(len(ICONS), "ícones")

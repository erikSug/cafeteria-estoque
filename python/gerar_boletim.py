from datetime import datetime
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

# item, unidade, quantidade atual, estoque mínimo
ESTOQUE = [
    ("Grãos de café", "kg", 12, 10),
    ("Leite", "L", 8, 20),
    ("Açúcar", "kg", 15, 5),
    ("Copos 300 ml", "un", 120, 200),
    ("Chocolate em pó", "kg", 4, 3),
    ("Pão de queijo", "un", 60, 40),
]

SAIDA = Path(__file__).parent / "boletim.pdf"


def status(qtd, minimo):
    if qtd < minimo:
        return "Crítico"
    if qtd < minimo * 1.5:
        return "Atenção"
    return "OK"


def gerar_pdf():
    estilos = getSampleStyleSheet()
    doc = SimpleDocTemplate(str(SAIDA), pagesize=A4)

    elementos = [
        Paragraph("Boletim de Estoque - Cafeteria", estilos["Title"]),
        Paragraph(f"Gerado em {datetime.now():%d/%m/%Y %H:%M}", estilos["Normal"]),
        Spacer(1, 0.8 * cm),
    ]

    fundo = {
        "Crítico": colors.HexColor("#f8d7da"),
        "Atenção": colors.HexColor("#fff3cd"),
        "OK": colors.HexColor("#d4edda"),
    }

    dados = [["Item", "Unidade", "Atual", "Mínimo", "Status"]]
    estilo = [
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#4b2e1e")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.lightgrey),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
    ]

    for i, (item, un, qtd, minimo) in enumerate(ESTOQUE, start=1):
        s = status(qtd, minimo)
        dados.append([item, un, qtd, minimo, s])
        estilo.append(("BACKGROUND", (0, i), (-1, i), fundo[s]))

    tabela = Table(dados, colWidths=[6 * cm, 2.5 * cm, 2.5 * cm, 2.5 * cm, 3 * cm])
    tabela.setStyle(TableStyle(estilo))
    elementos.append(tabela)

    doc.build(elementos)
    print(f"PDF gerado em {SAIDA}")


if __name__ == "__main__":
    gerar_pdf()
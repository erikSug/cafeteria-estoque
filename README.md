# Controle de Estoque (Cafeteria)

Script em Python (ReportLab) que gera um boletim de estoque em PDF, e uma página web simples para visualizá-lo.

## Como usar

```bash
pip install -r requirements.txt
python python/gerar_boletim.py
```

Depois abra `index.html` e clique em **Ver boletim**.
Se o navegador bloquear o PDF, rode `python -m http.server` dentro de `docs/` e acesse `localhost:8000`.

## Estrutura

- `gerar_boletim.py`: gera `boletim.pdf`

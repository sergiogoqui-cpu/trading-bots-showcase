#!/usr/bin/env python3
"""Agrega una nota al DEVLOG.md bajo la fecha de hoy.

Uso: python scripts/devlog.py "Reconexión WebSocket con backoff exponencial" --tag ws --tag python
"""

import argparse
import re
import sys
from datetime import date
from pathlib import Path

DEVLOG = Path(__file__).resolve().parent.parent / "DEVLOG.md"
START, END = "<!-- DEVLOG:START -->", "<!-- DEVLOG:END -->"

# Evita publicar secretos o datos de estrategia por accidente.
BLOQUEADO = re.compile(
    r"(api[_-]?key|secret|token|password|private[_-]?key|sharpe|profit|pnl|win ?rate|take[_-]?profit|stop[_-]?loss\s*=?\s*\d)",
    re.IGNORECASE,
)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("nota")
    ap.add_argument("--tag", action="append", default=[])
    args = ap.parse_args()

    if BLOQUEADO.search(args.nota):
        print("Rechazado: la nota parece contener secretos o datos de estrategia.", file=sys.stderr)
        return 1

    texto = DEVLOG.read_text(encoding="utf-8")
    if START not in texto or END not in texto:
        print("DEVLOG.md no tiene los marcadores START/END.", file=sys.stderr)
        return 1

    hoy = f"## {date.today().isoformat()}"
    tags = "".join(f"`[{t}]` " for t in args.tag) or "`[nota]` "
    linea = f"- {tags}{args.nota.strip()}"

    antes, resto = texto.split(START, 1)
    cuerpo, despues = resto.split(END, 1)
    cuerpo = cuerpo.strip("\n")
    if cuerpo.startswith(hoy):
        encabezado, _, items = cuerpo.partition("\n")
        cuerpo = f"{encabezado}\n{linea}\n{items}".rstrip("\n")
    else:
        cuerpo = f"{hoy}\n{linea}\n\n{cuerpo}".rstrip("\n")

    DEVLOG.write_text(f"{antes}{START}\n{cuerpo}\n{END}{despues}", encoding="utf-8")
    print(f"Nota agregada: {linea}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

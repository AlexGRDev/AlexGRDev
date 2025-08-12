#!/usr/bin/env python3
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
READM E = ROOT / "README.md"
DATA   = ROOT / "pwn.progress.json"

START = "<!-- PWN:START -->"
END   = "<!-- PWN:END -->"

def render_table(dojos):
    total_h = sum(d["hacking"] for d in dojos)
    total_m = sum(d["modules"] for d in dojos)
    total_c = sum(d["challenges"] for d in dojos)

    lines = []
    lines += [
        "### 🥷 pwn.college — Progreso",
        "",
        "| Dojo | Hacking | Módulos | Retos |",
        "|---|---:|---:|---:|",
    ]
    for d in dojos:
        lines.append(f"| {d['name']} | {d['hacking']} | {d['modules']} | {d['challenges']} |")
    lines += [
        "",
        f"**Totales:** 🔓 **{total_h} Hacking** · 📚 **{total_m} Módulos** · 🎯 **{total_c} Retos**",
        "",
        "_Última actualización automática._"
    ]
    return "\n".join(lines)

def main():
    if not DATA.exists():
        print("No existe pwn.progress.json", file=sys.stderr)
        sys.exit(1)

    dojos = json.loads(DATA.read_text(encoding="utf-8"))["dojos"]
    block = render_table(dojos)

    readme = READM E.read_text(encoding="utf-8")

    if START not in readme or END not in readme:
        # Si no hay marcadores, los añadimos al final
        readme = readme.rstrip() + f"\n\n{START}\n{block}\n{END}\n"
    else:
        before = readme.split(START)[0]
        after  = readme.split(END, 1)[1]
        readme = before + START + "\n" + block + "\n" + END + after

    READM E.write_text(readme, encoding="utf-8")

if __name__ == "__main__":
    main()

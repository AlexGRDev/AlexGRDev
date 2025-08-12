#!/usr/bin/env python3
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
DATA = ROOT / "pwn.progress.json"

START = "<!-- PWN:START -->"
END = "<!-- PWN:END -->"

def render_table(dojos):
    total_h = sum(d["hacking"] for d in dojos)
    total_m = sum(d["modules"] for d in dojos)
    total_c = sum(d["challenges"] for d in dojos)

    lines = [
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
        "_Última actualización automática._",
    ]
    return "\n".join(lines)

def main():
    if not DATA.exists():
        print("No existe pwn.progress.json", file=sys.stderr)
        sys.exit(1)

    dojos = json.loads(DATA.read_text(encoding="utf-8"))["dojos"]
    block = render_table(dojos)

    readme_text = README.read_text(encoding="utf-8")

    if START not in readme_text or END not in readme_text:
        # Si no hay marcadores, añádelos al final
        readme_text = readme_text.rstrip() + f"\n\n{START}\n{block}\n{END}\n"
    else:
        before = readme_text.split(START)[0]
        after = readme_text.split(END, 1)[1]
        readme_text = before + START + "\n" + block + "\n" + END + after

    README.write_text(readme_text, encoding="utf-8")

if __name__ == "__main__":
    main()

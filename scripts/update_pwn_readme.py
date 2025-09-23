#!/usr/bin/env python3
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

START = "<!--START_SECTION:repos-->"
END = "<!--END_SECTION:repos-->"

def render_latest_commits(n=5):
    try:
        # Obtener los últimos n commits en formato corto
        result = subprocess.run(
            ["git", "log", f"-{n}", "--pretty=format:- %h - %s (%ci)"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True
        )
        commits = result.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print("Error obteniendo commits:", e, file=sys.stderr)
        sys.exit(1)

    lines = [
        "## 🗂️ Últimos repos actualizados / Latest Updated Repos",
        "",
    ]
    lines.extend(commits)
    lines.append("")  # línea final vacía
    lines.append("_Última actualización automática._")
    return "\n".join(lines)

def main():
    block = render_latest_commits()

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

import json
import sys
import os
import subprocess

def generate_tex(tag, problems, output_tex):
    header = r"""
\documentclass[12pt]{article}
\usepackage[left=2cm, right=2cm, top=2cm]{geometry}
\usepackage{amsmath, amsfonts, amssymb}
\usepackage{hyperref}
\usepackage{fancyhdr}
\usepackage[dvipsnames]{xcolor}
\usepackage{xepersian}

\settextfont[BoldFont=XbNiloofarBd.ttf, ItalicFont=XbNiloofarIt.ttf, BoldItalicFont=XbNiloofarBdIt.ttf]{XbNiloofar.ttf}
\setlatintextfont{Times New Roman}

\definecolor{linkcolor}{rgb}{0.13, 0.55, 0.13}

\newcounter{counter}
\newcommand{\problem}[1]{\leavevmode\linebreak\noindent\refstepcounter{counter}\href{#1}{\bfseries مسئله \thecounter .}}
\newcommand{\englishtext}[1]{\leavevmode{\vspace{-10pt}\begin{latin}\noindent #1 \end{latin}}}

\hypersetup{colorlinks=true, urlcolor=linkcolor}

\newcommand{\subjecttitle}{""" + tag + r"""}

\fancypagestyle{firstpage}{
    \fancyhf{}
    \rhead{متین یوسفی}
    \chead{\LARGE \subjecttitle}
    \lhead{بزدلی بزرگ‌ترین گناه است...}
}

\fancypagestyle{main}{
    \fancyhf{}
    \lhead{متین یوسفی}
    \rhead{\subjecttitle}
}

\begin{document}
\thispagestyle{firstpage}
\pagestyle{main}
"""
    footer = r"\end{document}"

    with open(output_tex, "w", encoding="utf-8") as tex_file:
        tex_file.write(header)
        for problem in problems:
            tex_file.write(f"\\problem{{{problem['link']}}}\n")
            tex_file.write(problem['persian'] + "\n\n")
            tex_file.write(f"\\englishtext{{{problem['statement']}}}\n\n")
        tex_file.write(footer)

def compile_tex(tex_file):
    try:
        subprocess.run(["xelatex", tex_file], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to compile the LaTeX file.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python tag_selector.py <tag>")
        sys.exit(1)

    tag = sys.argv[1]
    db_path = "./db.fr.json"  # Currently set relative to Makefile
    output_tex = f"{tag}.tex"
    output_pdf = f"{tag}.pdf"

    with open(db_path, "r", encoding="utf-8") as db_file:
        problems = json.load(db_file)

    filtered_problems = [p for p in problems if tag in p["tags"]]

    if not filtered_problems:
        print(f"No problems found with the tag '{tag}'.")
        sys.exit(1)

    generate_tex(tag, filtered_problems, output_tex)
    compile_tex(output_tex)

    for ext in [".aux", ".log"]:
        aux_file = output_tex.replace(".tex", ext)
        if os.path.exists(aux_file):
            os.remove(aux_file)

    print(f"PDF generated: {output_pdf}")

if __name__ == "__main__":
    main()

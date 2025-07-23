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

\definecolor{linkcolor}{rgb}{1.0, 0.33, 0.64}
\hypersetup{colorlinks=true, urlcolor=linkcolor}

\newcounter{counter}
\newcommand{\prob}[1]{\leavevmode\linebreak\noindent\refstepcounter{counter}\href{#1}{\bfseries Problem \thecounter .}}

\fancypagestyle{firstpage}{
    \fancyhf{}
    \lhead{In the Name of God}
    \chead{\LARGE """ + tag + r"""}
    \rhead{\today}
    \cfoot{\thepage}
}

\fancypagestyle{main}{
    \fancyhf{}
    \lhead{Matin Yousefi}
    \rhead{""" + tag + r"""}
}

\begin{document}
\thispagestyle{firstpage}
\pagestyle{main}
"""
    footer = r"\end{document}"

    with open(output_tex, "w") as tex_file:
        tex_file.write(header)
        for problem in problems:
            tex_file.write(f"\\prob{{{problem['link']}}} {problem['statement']}\n\n")
        tex_file.write(footer)

def compile_tex(tex_file):
    try:
        subprocess.run(["pdflatex", tex_file], check=True)
    except subprocess.CalledProcessError:
        print("Error: Failed to compile the LaTeX file.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python tag_selector.py <tag>")
        sys.exit(1)

    tag = sys.argv[1]
    db_path = "/home/matin/olympiad/nt-problems/db.json"
    output_tex = f"{tag}.tex"
    output_pdf = f"{tag}.pdf"

    # Load problems from the database
    with open(db_path, "r") as db_file:
        problems = json.load(db_file)

    # Filter problems by the given tag
    filtered_problems = [p for p in problems if tag in p["tags"]]

    if not filtered_problems:
        print(f"No problems found with the tag '{tag}'.")
        sys.exit(1)

    # Generate the .tex file
    generate_tex(tag, filtered_problems, output_tex)

    # Compile the .tex file to PDF
    compile_tex(output_tex)

    # Clean up auxiliary files
    for ext in [".aux", ".log"]:
        aux_file = output_tex.replace(".tex", ext)
        if os.path.exists(aux_file):
            os.remove(aux_file)

    print(f"PDF generated: {output_pdf}")

if __name__ == "__main__":
    main()

import re
import sys

UNORD_LST = False
ORD_LST = False
TABLE = False

def env_end(line):
    global UNORD_LST, ORD_LST, TABLE
    if line == "" or line[0] == "\n":
        if UNORD_LST:
            line = "\\end{itemize}\n\n"
            UNORD_LST = False
        elif ORD_LST:
            line = "\\end{enumerate}\n\n"
            ORD_LST = False
        elif TABLE:
            line = "\\end{tabular}\n\\end{center}\n\n"
            TABLE = False
    return line

outfile = open("outfile.tex","w",encoding="utf-8")
with open(sys.argv[1],"r",encoding="utf-8") as infile:
    for line in infile:
        # headings
        line = re.sub(r"^# (.*?)$",r"\section{\1}",line)
        line = re.sub(r"^## (.*?)$",r"\subsection{\1}",line)
        line = re.sub(r"^### (.*?)$",r"\subsubsection{\1}",line)
        # fonts
        line = re.sub(r"\*\*(.*?)\*\*",r"\\textbf{\1}",line)
        line = re.sub(r"\*([^ ].*?)\*",r"\emph{\1}",line) # distinguish with unordered lists
        line = re.sub(r'<font color="(.*?)">(.*?)</font>', \
                      r'\\textcolor{\1}{\2}',line)
        line = re.sub(r'<u>(.*?)</u>',r'\underline{\1}',line)
        line = re.sub(r'<br/>','\n',line)
        # codes
        line = re.sub(r'```([a-z]+)',r'\\begin{lstlisting}[language=\1]',line)
        line = re.sub(r'```',r'\end{lstlisting}',line)
        # math
        line = re.sub(r'\$\$(.*?)\$\$',r'\\[\1\\]',line)
        # figures
        line = re.sub(r'!\[.*\]\((.*)\)',
                      r'\\begin{figure}[H]\n'
                      r'\centering\n'
                      r'\includegraphics[width=0.8\linewidth]{\1}\n'
                      r'\end{figure}',line)
        # links
        line = re.sub(r'\[(.*)\]\((.*)\)',r'\href{\2}{\1}',line)
        line = re.sub(r'<(http.*)>',r'\url{\1}',line)
        # big environments
        if line[:2] == "* ": # unordered lists
            if UNORD_LST:
                line = "\\item" + line[1:]
            else:
                line = "\\begin{itemize}\n\\item" + line[1:]
                UNORD_LST = True
        elif re.match(r"[0-9]+\. ",line) != None: # ordered lists
            idx = re.match(r"[0-9]+\.",line).span()[1]
            if ORD_LST:
                line = "\\item" + line[idx:]
            else:
                line = "\\begin{enumerate}\n\\item" + line[idx:]
                ORD_LST = True
        elif "|" in line: # tables
            line = line.strip()
            if ":-" in line or "-:" in line:
                continue
            line = line[1:-1].replace("|","&")
            num = len(re.findall("&",line)) + 1
            if TABLE:
                line = line + "\\\\ \\hline\n"
            else:
                line = "\\begin{center}\n\\begin{tabular}{%s|}\n" % ('|c' * num) + line + "\\\\ \\hline\n"
                TABLE = True
        else:
            line = env_end(line)
        # comments
        line = re.sub(r'<!--(.*?)-->',r'% \1',line)
        outfile.write(line)
    line = env_end("")
    outfile.write(line)

outfile.close()
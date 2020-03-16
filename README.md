# DocTools: Tools for formatting docs (tex/txt + bib)

As a LaTeX-fancier, I cannot bear myself processing text and fine-tuning the formats in Microsoft Office Word endlessly, but at some times I have to use Word or textbook to write something. To free myself from tedious formatting, I build the wheels.

(As for another reason, I can easily customize my tools to meet different formatting requirements.)

## BibTool
A tool that automatically generates references and corresponding numbers from citations.

You can use `\cite` in the text as what you do in LaTeX. With the assistance of text editors like Sublime Text or VS Code, you can quickly insert the references into the text if you specify your text as a TeX file, and the auto-completion will work.

You need not count the number or order the references yourself. Just evoke the tool to link your text with the bibliography (in BibTeX format).

```
python bibtool.py example/text.txt example/ref.bib  # python 3 is needed
```

And you will get the output file like this
```
# output.txt - Generated by bibtool.py

TVM is an end-to-end deep learning compiler stack for CPUs, GPUs, and specialized accelerators [1,2].

Reference:
[1] Thierry Moreau, Tianqi Chen, Ziheng Jiang, Luis Ceze, Carlos Guestrin and Arvind Krishnamurthy, "VTA: An Open Hardware-Software Stack for Deep Learning" in arXiv:1807.04188 [cs, stat], 2018.
[2] Tianqi Chen, Thierry Moreau, Ziheng Jiang, Lianmin Zheng, Eddie Yan, Meghan Cowan et al., "TVM: an automated end-to-end optimizing compiler for deep learning" in Proceedings of the 12th USENIX conference on Operating Systems Design and Implementation (OSDI), 2018.
```

The input example can be found in the folder.


## Markdown to LaTeX (md2tex)
A tool that transforms Markdown grammar to LaTeX grammar.

Most of the markdown grammar are be supported, including nested environments. To change the style of generated tables, figures, and codes, you can directly modify the output string.

Just type

```
python md2tex.py example/text.md # python 3 is needed
```

The corresponding LaTeX file (`output.tex`) will be generated.


## TiddlyWiki to Markdown (tiddly2md)
A tool that transforms [TiddlyWiki](https://tiddlywiki.com/) grammar to Markdown grammar.

Just type

```
python tiddly2md.py tiddly.txt output.md # python 3 is needed
```

Disclaimer: I do not use complex parsing techniques so these tools might easily get into trouble.
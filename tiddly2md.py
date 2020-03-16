import re
import sys

if len(sys.argv) >= 3:
    outfile_name = sys.argv[2]
else:
    outfile_name = "output.md"
outfile = open(outfile_name,"w",encoding="utf-8")
outfile.write("---\n")
outfile.write("layout: post\n")
outfile.write("title: \n")
outfile.write("date: \n")
outfile.write("tag: \n")
outfile.write("---\n")
with open(sys.argv[1],"r",encoding="utf-8") as infile:
    for line in infile:
        # headings
        line = re.sub(r"^! (.*?)$",r"# \1",line)
        line = re.sub(r"^!! (.*?)$",r"## \1",line)
        line = re.sub(r"^!!! (.*?)$",r"### \1",line)
        # fonts
        line = re.sub(r"''(.*?)''",r"**\1**",line)
        # unordered lists
        line = re.sub(r"^\* (.*?)$",r"* \1",line)
        line = re.sub(r"^\*\* (.*?)$",r"\t* \1",line)
        line = re.sub(r"^\*\*\* (.*?)$",r"\t\t* \1",line)
        line = re.sub(r"^\*\*\*\* (.*?)$",r"\t\t\t* \1",line)
        outfile.write(line)
outfile.close()
import os



dir = "C:/projects/singstar/txtfiles/"
inputfile = "c:/projects/singstar/inputfile.txt"
os.remove(inputfile)

fout = open(inputfile,"wt",encoding="utf-8")

for title in os.listdir(dir):
    fout.write(title + '\n')

fout.close()
import os
import urllib.request
import re

def findvideo(search_keyword):
    words = search_keyword.split()

    url = "http://www.youtube.com/results?search_query="

    for word in words:
        url += word + "+"

    html = urllib.request.urlopen(url[:-1])
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    fout.write("https://www.youtube.com/watch?v=" + video_ids[0] + '\n')


dir = "C:/projects/singstar/txtfiles/"
inputfile = "c:/projects/singstar/inputfile.txt"
os.remove(inputfile)

fout = open(inputfile,"wt",encoding="utf-8")

for title in os.listdir(dir):
    songtitle = title[0:len(title) - 4]
    fout.write(songtitle + '\n')
    findvideo(songtitle)

fout.close()    



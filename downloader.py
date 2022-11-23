from yt_dlp import YoutubeDL
import os
import shutil
import time
import os
import urllib.request
import re

# DownloadedTxtFilesLocation = "c:/me/projects/singstar/txtfiles/"
# inputfile = "C:/me/projects/singstar/combinedlinksandtitles.txt"
# songlocation = "c:/me/test/" + title

DownloadedTxtFilesLocation = "C:/projects/singstar/txtfiles/"
inputfile = "C:/projects/singstar/inputfile.txt"
outputdir = "C:/Users/Jeroen/Downloads/output/"

def changetxtfile(title,mp3value,mp4value):
    fin = open(title + '.txt', 'rt')
    fout = open("out.txt", "wt")

    for line in fin:        
        if line.startswith('#MP3'):
            fout.write('#MP3:' + mp3value + '\n' + '#VIDEO:' + mp4value + '\n')
            continue
        if line.startswith('#VIDEO'):   
            continue
        if line.startswith('desktop'):
            continue
        else:
            fout.write(line)

    fin.close()
    fout.close()

    os.remove(title + '.txt')
    os.rename("out.txt", title + '.txt')

def downloadLink(title, videolink):
    songlocation = outputdir + title
    os.mkdir(songlocation)
    shutil.copy(DownloadedTxtFilesLocation + title + ".txt", songlocation  + "/" + title + ".txt")
    os.chdir(songlocation)
    #download the whole video
    ydl_opts = {'outtmpl': songlocation + "/" + title, 
                'postprocessors': [{'key': 'FFmpegVideoConvertor','preferedformat':'mp4'}]}
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(videolink) 
    #download as mp3
    ydl_opts = {'format': 'bestaudio/best',
                'outtmpl': songlocation + "/" + title + '.mp3',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320'}]}
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(videolink)

    #change text file to include video and audio
    mp3value = title + '.mp3'
    mp4value = title + '.mp4'

    changetxtfile(title,mp3value,mp4value)




def findvideo(search_keyword):
    words = search_keyword.split()

    url = "http://www.youtube.com/results?search_query="

    for word in words:
        url += word + "+"

    html = urllib.request.urlopen(url[:-1])
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    fout.write("https://www.youtube.com/watch?v=" + video_ids[0] + '\n')

#get all textfiles in folder
dir = "C:/projects/singstar/txtfiles/"
os.remove(inputfile)

fout = open(inputfile,"wt",encoding="utf-8")
#put them in the inputfile.txt with the first found youtube vid
for title in os.listdir(dir):
    if title.startswith("desktop"):
        continue
    songtitle = title[0:len(title) - 4]
    fout.write(songtitle + '\n')
    findvideo(songtitle)    

fout.close()    

video = ""
title = ""
index = 1

#read the inputfile title and
#create folder
#download + convert video
#change txt file to include downloaded stuff
d = {}
with open(inputfile) as f:
    for line in f:
        d[index] = line.strip() #.replace('.txt','') #video
        index += 1

diclength = len(d)
    
print(diclength)
step = 1

while step < diclength:
    downloadLink(d[step],d[step+1])
    step += 2


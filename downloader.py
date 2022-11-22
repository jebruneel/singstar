from yt_dlp import YoutubeDL
import os
import shutil

DownloadedTxtFilesLocation = "c:/me/projects/singstardownloader/txtfiles/"
combinedFile = "C:/me/projects/singstardownloader/combinedlinksandtitles.txt"

def downloadLink(title, videolink):
    songlocation = "c:/me/test/" + title
    os.mkdir(songlocation)
    shutil.copy(DownloadedTxtFilesLocation + title + ".txt", songlocation  + "/" + title + ".txt")
    ydl_opts = {'outtmpl': songlocation + "/" + title + ".mp3"}
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(videolink)

video = ""
title = ""
index = 1

d = {}
with open(combinedFile) as f:
    for line in f:
        d[index] = line.strip().replace('.txt','') #video
        index += 1

diclength = len(d)

print(diclength)
step = 1

while step < diclength:
    downloadLink(d[step],d[step+1])
    step += 2


from yt_dlp import YoutubeDL
import os
import shutil

DownloadedTxtFilesLocation = "c:/me/projects/singstar/txtfiles/"
combinedFile = "C:/me/projects/singstar/combinedlinksandtitles.txt"


def changetxtfile(title,mp3value,mp4value):
    print('lol')


def downloadLink(title, videolink):
    songlocation = "c:/me/test/" + title
    os.mkdir(songlocation)
    shutil.copy(DownloadedTxtFilesLocation + title + ".txt", songlocation  + "/" + title + ".txt")
    os.chdir(songlocation)
    #download the whole video
    ydl_opts = {'outtmpl': songlocation + "/" + title + '.%(ext)s'}
    with YoutubeDL(ydl_opts) as ydl:
        # info = ydl.extract_info(videolink, download=False)
        # file_extensions = ydl.prepare_filename(info)
        # print('banana ' + file_extensions)
        ydl.download(videolink)
    #download as mp3
    # ydl_opts = {'format': 'bestaudio/best',
    #             'postprocessors': [{
    #                 'key': 'FFmpegExtractAudio',
    #                 'preferredcodec': 'mp3',
    #                 'preferredquality': '320',
    # }]}
    # with YoutubeDL(ydl_opts) as ydl:
    #     ydl.download(videolink)

    #change text file to include video and audio
    mp3value = title + '.mp3'
    mp4value = title + '.mp4'

    changetxtfile(title,mp3value,mp4value)

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


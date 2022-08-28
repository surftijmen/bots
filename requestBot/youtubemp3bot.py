from __future__ import unicode_literals
from unicodedata import name
import yt_dlp

# function to download youtube audio
def downloadMp3():
    # options for downloading
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': "S:\clip music" + '/%(title)s.%(ext)s',
        'noplaylist':True,        
        }

    # read the youtube links from the yt.txt file
    with open('requestBot/yt.txt') as f:
        lines = f.read().splitlines()

    # download the youtube links
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(lines)

    # after downloading, empty yt.txt
    open("yt.txt", 'w').close()

if __name__ == "__main__":
    downloadMp3()
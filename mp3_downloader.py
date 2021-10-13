from __future__ import unicode_literals
import youtube_dl
from youtubesearchpython import VideosSearch

print("---------------------")
print("music mp3 downloader")
print("---------------------")

# User Input
print("Enter song name: ")
keywords = input()
print("Number of matches you expect: ")
matches = int(input())



# video search
videosSearch = VideosSearch(keywords, limit = matches)
results = videosSearch.result()['result']
titles = [item['title'] for item in results]

# print titles
i = 0
for title in titles:
	i+=1
	print(str(i)+" "+title) 

# pick option
print("Pick option(eg:-2) :")
option = int(input())
print("Downloading...Downloding...")

# download selected option
option_url = results[option-1]['link']



# downloading option
class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([option_url])


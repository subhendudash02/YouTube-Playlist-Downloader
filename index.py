from pytube import Playlist, YouTube
import re
import urllib

pl = input("Enter a playlist: ")
playlist = Playlist(pl)
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))
count = 1
for url in playlist.video_urls:
    try:
        print("Downloading: ", url)
        print("Count: ", count)
        url = YouTube(url)
        url = url.streams.get_highest_resolution()
        url.download()
        print("done")
        count += 1
    except urllib.error.URLError:
        print("Download failed...Going to the next video")
        count += 1
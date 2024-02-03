import os
from pytube import Playlist
from pytube import YouTube

url_playlist = input("Enter The Playlist URL:  ")
input = url_playlist
p = Playlist(input)

for i in range(len(p.video_urls)):
  print("Starting Downloading ...")
  try:
    yt = YouTube(p.video_urls[i])
    print(f"Remaining Videos : {len(p.video_urls) - i} ")

    yt.streams.filter(progressive=True)
    stream = yt.streams.get_by_itag(22)

    path = os.getcwd() + "\Downloads"
    stream.download(path)
    print("Download Completed")
  except Exception as e:
    print("Error coming : ", e)

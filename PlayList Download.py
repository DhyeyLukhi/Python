from pytube import Playlist

url = input("URL: ")
playlist = Playlist(url)

for video in playlist:
    video.stream.get_highest_resolution().download()


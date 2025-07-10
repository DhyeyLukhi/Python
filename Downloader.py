import os
import yt_dlp
import pytube


while True:
    try:
        try:

            url = input("Enter the URL: ")
            path = os.getcwd()

            ydl_opts = {}

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                # ydl.format_resolution()

            print("Downloaded")
            break

        except Exception as e1:
            print(e1)

    except Exception as e:
        print(e)

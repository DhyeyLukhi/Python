import yt_dlp

while True:
    try:
        url = input("Enter the URL: ")

        ydl_opts = {}

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        print("Downloaded")

    except Exception as e:
        print(e)

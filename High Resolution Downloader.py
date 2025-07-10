from pytube import YouTube

while True:
    try:
        videourl = input("Enter the URL: ")
        path = 'D:\\'

        video = YouTube(videourl)

        stream = video.streams.get_highest_resolution()

        stream.download(output_path=path)
        print("Done")
    except Exception as e:
        print(e)

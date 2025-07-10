import moviepy.editor

try:
    path = "D:\\songs\\new copy.mp4"
    video = moviepy.editor.VideoFileClip(path)
    audio = video.audio
except Exception as e:
    print(e)

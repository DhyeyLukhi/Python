import os
import yt_dlp


def get_info(url):
    ydl_opts = {'quiet': True, 'extract_flat': False}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        return ydl.extract_info(url, download=False)


def list_formats(formats):
    video_formats = [f for f in formats if f.get('vcodec') != 'none' and f.get('acodec') != 'none']
    video_formats = sorted(video_formats, key=lambda x: int(x.get('height', 0)))
    print("\nAvailable formats:")
    for idx, f in enumerate(video_formats, 1):
        print(f"{idx}> {f['height']}p - {f['ext']} - {f['format_note']}")
    return video_formats


def select_format(formats):
    video_formats = list_formats(formats)
    choice = int(input("\nEnter the format number: ")) - 1
    return video_formats[choice]


def find_nearest_format(formats, target_height):
    video_formats = [f for f in formats if f.get('vcodec') != 'none' and f.get('acodec') != 'none']
    video_formats = sorted(video_formats, key=lambda x: abs(int(x.get('height', 0)) - target_height))
    return video_formats[0] if video_formats else None


def download_video(url, format_id, filename):
    ydl_opts = {
        'format': format_id,
        'outtmpl': filename,
        'quiet': False,
        'noplaylist': True,
        'writesubtitles': True,
        'writeautomaticsub': True,
        # 'subtitleslangs': ['en', 'hi'],  # Download English and Hindi subtitles
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main():
    url = input("Enter the URL: ").strip()
    try:
        info = get_info(url)
    except Exception as e:
        print("Error: Video/playlist does not exist.")
        return

    if 'entries' in info:  # Playlist
        print("Detected playlist.")
        playlist_title = info.get('title', 'Playlist')
        os.makedirs(playlist_title, exist_ok=True)
        first_video = info['entries'][0]
        selected_format = select_format(first_video['formats'])
        target_height = int(selected_format['height'])
        format_id = selected_format['format_id']

        print(f"\nDownloading playlist into folder: {playlist_title}")
        for idx, entry in enumerate(info['entries'], 1):
            vid_info = get_info(entry['webpage_url'])
            nearest_format = find_nearest_format(vid_info['formats'], target_height)
            fname = os.path.join(playlist_title, f"{idx:02d} - {vid_info['title']}.%(ext)s")
            print(f"Downloading: {fname} in {nearest_format['height']}p")
            download_video(entry['webpage_url'], nearest_format['format_id'], fname)
    else:  # Single video
        print("Detected single video.")
        selected_format = select_format(info['formats'])
        fname = f"{info['title']}.%(ext)s"
        print(f"Downloading: {fname} in {selected_format['height']}p")
        download_video(url, selected_format['format_id'], fname)

    print("\nDownload complete.")


if __name__ == "__main__":
    main()

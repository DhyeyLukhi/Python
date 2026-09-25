import yt_dlp

def download_youtube_playlist(playlist_url, output_folder="Downloads"):
    # Configure the download options
    ydl_opts = {
        # Download best available video and audio, merge them into mp4
        'format': 'bestvideo+bestaudio/best',
        
        # Save files inside output_folder grouped by playlist title
        'outtmpl': f'{output_folder}/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',
        
        # Ensure it processes the URL specifically as a playlist
        'noplaylist': False,
    }
    
    # Initialize yt_dlp and execute the download
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"Starting download for playlist: {playlist_url}")
            ydl.download([playlist_url])
            print("Download completed successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with your target playlist link
    URL = "https://www.youtube.com/playlist?list=PLOJR6EhNalnsCaQz8RCfKo5fc-FLeaVDb"
    download_youtube_playlist(URL)

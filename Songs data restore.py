import os
from mutagen.easyid3 import EasyID3
from musicbrainzngs import set_useragent, search_recordings


def search_metadata(filename):
    set_useragent("MusicMetadataRestorer", "1.0", "dhyeylukhi72@gmail.com")

    # Extract the main part of the filename without extension
    query = os.path.splitext(filename)[0]

    # Search for the recording on MusicBrainz
    results = search_recordings(query=query, limit=1)

    if results['recording-list']:
        return results['recording-list'][0]
    return None


def restore_metadata(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            song_info = search_metadata(filename)
            try:
                if song_info:
                    audio = EasyID3(filepath)

                    audio['title'] = song_info['title']
                    audio['artist'] = song_info['artist-credit'][0]['artist']['name']
                    audio['album'] = song_info['release-list'][0]['title']
                    audio['genre'] = song_info.get('tag-list', [{}])[0].get('name', 'Unknown')

                    audio.save()
                    print(f"Restored metadata for {filename}")

            except Exception as e:
                print(f"{filename} has {e}")
                audio = EasyID3(filepath)
                audio['genre'] = song_info.get('tag-list', [{}])[0].get('name', 'Unknown')

                audio.save()



if __name__ == "__main__":
    music_directory = "D:\\Musics"
    restore_metadata(music_directory)

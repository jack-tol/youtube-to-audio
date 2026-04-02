import yt_dlp

class YouTubeDownloader:
    SUPPORTED_FORMATS = ["mp3", "wav", "flac", "aac", "ogg", "m4a", "opus"]

    def __init__(self, audio_format: str = "mp3", output_name: str = None, playlist_name: str = None):
        if audio_format not in self.SUPPORTED_FORMATS:
            raise ValueError(f"Invalid format! Choose between {', '.join(self.SUPPORTED_FORMATS)}.")
        self.audio_format = audio_format
        self.output_name = output_name
        self.playlist_name = playlist_name

    def download_audio(self, youtube_url: str):
        is_playlist = "playlist?" in youtube_url.lower()

        if is_playlist:
            playlist_folder = self.playlist_name or "%(playlist_title)s"
            output_template = f"{playlist_folder}/%(title)s.%(ext)s"
        else:
            output_template = f"{self.output_name}.%(ext)s" if self.output_name else "%(title)s.%(ext)s"

        ydl_opts = {
            'format': 'bestaudio/best',
            'extractaudio': True,
            'audioformat': self.audio_format,
            'outtmpl': output_template,
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': self.audio_format}],
            'quiet': True,
            'noprogress': True,
            'no_warnings': True,
            'yes_playlist': True,
            'ignoreerrors': is_playlist,
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(youtube_url, download=True)

                if is_playlist:
                    playlist_title = self.playlist_name or info_dict.get('title', 'Unknown Playlist')
                    return f"✅ Playlist download complete! Saved in folder: '{playlist_title}'."
                
                video_title = self.output_name or info_dict.get('title', 'Unknown Video')
                return f"✅ Download complete! Saved as '{video_title}.{self.audio_format}'."

        except Exception as e:
            raise RuntimeError(f"❌ Error downloading audio: {e}")
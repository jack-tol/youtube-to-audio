import os
from pytubefix import YouTube

class Downloader:
    def __init__(self, url, client='MWEB'):
        self.url = url
        self.client = client

    def download_video(self, output_path="video.mp4"):
        if os.path.exists(output_path):
            os.remove(output_path)

        try:
            yt = YouTube(self.url, client=self.client)
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download(filename=output_path)
            return output_path
        except KeyError as e:
            raise Exception(f"Error downloading video: Video may be unavailable or restricted. Details: {e}")
        except Exception as e:
            raise Exception(f"Unexpected error while downloading video: {e}")

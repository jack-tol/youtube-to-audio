from youtube_to_audio.downloader import Downloader

def test_downloader():
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    downloader = Downloader(url)
    video_path = downloader.download_video()
    assert video_path.endswith(".mp4")
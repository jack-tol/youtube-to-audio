import os
import argparse
from pytubefix import YouTube
from moviepy.editor import VideoFileClip

def download_youtube_video(url):
    # Download the video from YouTube using pytubefix
    yt = YouTube(url)
    video_stream = yt.streams.get_highest_resolution()
    video_path = "video.mp4"
    video_stream.download(filename=video_path)
    return video_path

def extract_audio_from_video(video_file_path, output_format):
    # Extract audio from the video and save it with the specified format
    output_audio_path = f"audio.{output_format.lower()}"
    video_clip = VideoFileClip(video_file_path)
    audio_clip = video_clip.audio
    
    if output_format.lower() == 'wav':
        audio_clip.write_audiofile(output_audio_path, codec='pcm_s16le')
    elif output_format.lower() == 'mp3':
        audio_clip.write_audiofile(output_audio_path, codec='libmp3lame')
    else:
        raise ValueError("Invalid audio format. Choose either 'wav' or 'mp3'.")

    audio_clip.close()
    video_clip.close()
    return output_audio_path

def cleanup_video_file(video_file_path):
    # Remove the downloaded video file
    if os.path.exists(video_file_path):
        os.remove(video_file_path)

if __name__ == "__main__":
    # Set up argument parser for command-line arguments
    parser = argparse.ArgumentParser(description="Download YouTube video and extract audio.")
    parser.add_argument('url', help="YouTube video URL")
    parser.add_argument('format', nargs='?', default='wav', choices=['wav', 'mp3'], help="Audio format to extract (default is wav)")

    # Parse the command-line arguments
    args = parser.parse_args()
    youtube_url = args.url
    audio_format = args.format

    # Download video
    video_file_path = download_youtube_video(youtube_url)

    # Extract audio in the specified or default format
    extract_audio_from_video(video_file_path, audio_format)

    # Clean up the video file
    cleanup_video_file(video_file_path)

    print(f"Audio extracted and saved as 'audio.{audio_format}'. Video file cleaned up.")

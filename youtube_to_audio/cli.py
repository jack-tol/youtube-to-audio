import argparse
import logging
import os
from pytubefix import Playlist
from youtube_to_audio.downloader import Downloader
from youtube_to_audio.converter import Converter
from youtube_to_audio.utils import Utils

def process_video(url, output, audio_format, client):
    downloader = Downloader(url, client=client)
    video_file_path = downloader.download_video()

    video_title = os.path.splitext(os.path.basename(video_file_path))[0]

    output_file = output if output else video_title

    logging.info("Extracting audio...")
    converter = Converter(video_file_path)
    audio_file_path = converter.extract_audio(audio_format, f"{output_file}.{audio_format.lower()}")

    logging.info(f"Audio extracted successfully: {audio_file_path}")

    logging.info("Cleaning up temporary files...")
    Utils.cleanup_file(video_file_path)

def main():
    parser = argparse.ArgumentParser(description="Extract audio from YouTube videos or playlists in multiple formats.")
    parser.add_argument('url', help="YouTube video or playlist URL")
    parser.add_argument('format', nargs='?', default='mp3', choices=Converter.SUPPORTED_FORMATS, 
                        help="Audio format to extract (default is mp3)")
    parser.add_argument('--output', help="Output audio file name (optional, without extension). If not specified, the YouTube video title will be used.", default=None)
    parser.add_argument('--client', help="Specify the YouTube client to use. Options: MWEB, WEB, ANDROID, IOS. Default is 'MWEB'.", default='MWEB')
    parser.add_argument('--verbose', action='store_true', help="Enable verbose output")

    args = parser.parse_args()

    log_format = "%(message)s"
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG, format=log_format)
    else:
        logging.basicConfig(level=logging.INFO, format=log_format)

    youtube_url = args.url
    audio_format = args.format
    client = args.client

    try:
        if "list=" in youtube_url:
            logging.info("Processing playlist...")
            playlist = Playlist(youtube_url)

            for index, video in enumerate(playlist.videos, start=1):
                logging.info(f"Processing video {index}/{len(playlist.videos)}: {video.title}")
                process_video(video.watch_url, args.output, audio_format, client)

            logging.info("Playlist processed successfully.")
        else:
            logging.info("Processing single video...")
            process_video(youtube_url, args.output, audio_format, client)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
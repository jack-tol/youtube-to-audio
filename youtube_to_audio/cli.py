import argparse
import logging
from youtube_to_audio.downloader import Downloader
from youtube_to_audio.converter import Converter
from youtube_to_audio.utils import Utils

def main():
    parser = argparse.ArgumentParser(description="Download YouTube video and extract audio in multiple formats.")
    parser.add_argument('url', help="YouTube video URL")
    parser.add_argument('format', nargs='?', default='wav', choices=Converter.SUPPORTED_FORMATS, 
                        help="Audio format to extract (default is wav)")
    parser.add_argument('--output', help="Output audio file name (optional, without extension). Defaults to 'audio'.", default='audio')
    parser.add_argument('--client', help="Specify the YouTube client to use (e.g., MWEB, WEB, etc.). Default is 'MWEB'.", default='MWEB')
    parser.add_argument('--verbose', action='store_true', help="Enable verbose output")

    args = parser.parse_args()

    # Set up logging
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    youtube_url = args.url
    audio_format = args.format
    output_file = args.output  # The base name for the audio file
    client = args.client

    try:
        logging.info("Starting download...")
        downloader = Downloader(youtube_url, client=client)
        video_file_path = downloader.download_video()

        logging.info("Extracting audio...")
        converter = Converter(video_file_path)
        audio_file_path = converter.extract_audio(audio_format, f"{output_file}.{audio_format.lower()}")

        logging.info(f"Audio extracted successfully: {audio_file_path}")

        logging.info("Cleaning up temporary files...")
        Utils.cleanup_file(video_file_path)

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

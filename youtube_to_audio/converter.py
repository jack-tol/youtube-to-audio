from moviepy.editor import VideoFileClip

class Converter:
    SUPPORTED_FORMATS = ['wav', 'mp3', 'ogg', 'aac', 'flac']

    def __init__(self, video_file_path):
        self.video_file_path = video_file_path

    def extract_audio(self, output_format, output_audio_path=None):
        if output_format.lower() not in self.SUPPORTED_FORMATS:
            raise ValueError(f"Invalid audio format. Supported formats: {self.SUPPORTED_FORMATS}")

        if not output_audio_path:
            output_audio_path = f"audio.{output_format.lower()}"  # Default name if none provided

        try:
            video_clip = VideoFileClip(self.video_file_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(output_audio_path, codec=self.get_codec(output_format))
            audio_clip.close()
            video_clip.close()
        except Exception as e:
            raise Exception(f"Error extracting audio: {e}")

        return output_audio_path

    def get_codec(self, output_format):
        codecs = {
            'wav': 'pcm_s16le',
            'mp3': 'libmp3lame',
            'ogg': 'libvorbis',
            'aac': 'aac',
            'flac': 'flac',
        }
        return codecs.get(output_format.lower())

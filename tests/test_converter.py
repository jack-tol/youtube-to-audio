from unittest.mock import patch, MagicMock
from youtube_audio_extractor.converter import Converter

@patch('youtube_audio_extractor.converter.VideoFileClip')
def test_extract_audio(mock_video_clip):
    # Mock the audio clip and its methods
    mock_audio = MagicMock()
    mock_video_clip.return_value.audio = mock_audio

    converter = Converter("video.mp4")
    audio_path = converter.extract_audio("wav")

    # Check that the audio file was written
    mock_audio.write_audiofile.assert_called_once_with('audio.wav', codec='pcm_s16le')
    mock_audio.close.assert_called_once()
    mock_video_clip.return_value.close.assert_called_once()
    
    assert audio_path == "audio.wav"

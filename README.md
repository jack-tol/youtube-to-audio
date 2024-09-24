# YouTube-to-Audio CLI Tool

A lightweight Python package and command-line interface (CLI) tool that extracts audio from YouTube videos and playlists in multiple formats, such as MP3, WAV, OGG, AAC, and FLAC.

## Features

- Extract audio from YouTube videos or playlists in various formats: MP3, WAV, OGG, AAC, and FLAC
- Customize the output audio file name
- By default, names the audio file after the YouTube video title
- Extract audio from YouTube videos using different clients (e.g., `MWEB`, `WEB`, `ANDROID`)
- Automatically clean up temporary video files after extraction

## Installation

To install the package from PyPI, run the following command:

```
pip install youtube_to_audio
```

## Usage

### 1. Download and Extract Audio from a Single Video in the Default Format (MP3)

```
youtube-to-audio "https://www.youtube.com/watch?v=WysanSNOjMc"
```

This command extracts the audio in MP3 format and saves it with the same name as the YouTube video title (e.g., `Your Video Title.mp3`).

### 2. Extract Audio from a Playlist in MP3 Format

```
youtube-to-audio "https://www.youtube.com/playlist?list=PLRBp0Fe2GpgnymQGm0yIxcdzkQsPKwnBD"
```

This command extracts the audio from all videos in the playlist and saves each file with the same name as the YouTube video title (e.g., `Video1.mp3`, `Video2.mp3`, etc.).

### 3. Extract Audio in WAV Format

```
youtube-to-audio "https://www.youtube.com/watch?v=WysanSNOjMc" wav
```

This command extracts the audio in WAV format and saves it with the YouTube video title (e.g., `Your Video Title.wav`).

### 4. Specify a Custom Audio File Name

```
youtube-to-audio "https://www.youtube.com/watch?v=WysanSNOjMc" wav --output my_custom_name
```

This command extracts the audio in WAV format and saves it as `my_custom_name.wav`.

### 5. Extract Audio Using a Specific YouTube Client (e.g., MWEB or WEB)

You can extract audio from YouTube videos or playlists using different clients (for example, `MWEB`, `WEB`, or `ANDROID`) by specifying the `--client` argument:

```
youtube-to-audio "https://www.youtube.com/watch?v=WysanSNOjMc" flac --client WEB
```

> **Note:** If audio extraction fails with one client, try switching to a different client (e.g., from `MWEB` to `WEB` or `ANDROID`) to resolve the issue.

### 6. Enable Verbose Logging

To enable detailed logging (useful for debugging the download or extraction process), use the `--verbose` flag:

```
youtube-to-audio "https://www.youtube.com/watch?v=WysanSNOjMc" aac --verbose
```

This will display detailed logs during the download and extraction process.

## Development

If you'd like to contribute or modify the package locally, clone the repository and install the development dependencies:

```
pip install -r requirements-dev.txt
```

### Running Tests

To run tests, you can use `pytest` (after installing the development dependencies):

```
pytest
```

---

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

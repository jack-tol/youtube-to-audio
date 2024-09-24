# YouTube to Audio

A Python package that downloads YouTube videos and extracts audio in multiple formats such as WAV, MP3, OGG, AAC, and FLAC. You can also specify the YouTube client type and customize the audio output file name.

## Features

- Download YouTube videos using different clients (e.g., `MWEB`, `WEB`)
- Extract audio in various formats: WAV, MP3, OGG, AAC, and FLAC
- Customize the output audio file name
- Clean up temporary video files after extraction

## Installation

To install the package from PyPI:

```
pip install youtube-to-audio
```

## Usage

### 1. Download and Extract Audio in Default Format (WAV)

```
youtube-to-audio "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

This command will download the YouTube video and extract the audio in WAV format with the default name `audio.wav`.

### 2. Extract Audio in MP3 Format

```
youtube-to-audio "https://www.youtube.com/watch?v=dQw4w9WgXcQ" mp3
```

This will extract the audio in MP3 format as `audio.mp3`.

### 3. Specify a Custom Audio File Name

```
youtube-to-audio "https://www.youtube.com/watch?v=dQw4w9WgXcQ" mp3 --output my_custom_name
```

This will extract the audio in MP3 format and save it as `my_custom_name.mp3`.

### 4. Specify a YouTube Client (e.g., MWEB or WEB)

You can specify the YouTube client (for example, `MWEB` or `WEB`) using the `--client` argument:

```
youtube-to-audio "https://www.youtube.com/watch?v=dQw4w9WgXcQ" mp3 --client WEB
```

This will use the `WEB` client instead of the default `MWEB`.

### 5. Enable Verbose Logging

If you want more detailed output (for example, to debug the download process), use the `--verbose` flag:

```
youtube-to-audio "https://www.youtube.com/watch?v=dQw4w9WgXcQ" mp3 --verbose
```

This will output detailed logs during the download and extraction process.

## Development

If you want to contribute or modify the package locally, clone the repository and install it locally using:

```
pip install -e .
```

### Running Tests

To run the tests, you can use `pytest`:

```
pytest
```

---

### License

This project is licensed under the MIT License.

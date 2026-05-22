# CCAssistant by BetaBeta10
A Tkinter GUI application for ComputerCraft media conversion. Was made for personal use in my friend's modded server

![example gif](example.gif)

## Features

- **Image to NFP**: Convert PNG, JPG, BMP, and other image formats to ComputerCraft NFP format
  - Configure monitor width, height, and text scale
  - Automatic dimension calculation
  - Direct output to same directory as input

- **Audio/Video to DFPWM**: Convert MP3, MP4, WAV, MKV, and other formats to ComputerCraft DFPWM audio format
  - Uses ffmpeg for conversion
  - Output to same directory as input

## Requirements

- Python 3.7+
- Pillow (PIL) - for image processing
- ffmpeg - for audio/video conversion

## Installation

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Install ffmpeg:
   - **Windows**: Download from https://ffmpeg.org/download.html
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt-get install ffmpeg`

## Usage

Run the application:
```bash
python main.py
```
OR run the .exe file (buggy) in dist/CCAssistant.exe

### Image Conversion
1. Go to "Image to NFP" tab
2. Select an image file
3. Set monitor width, height, and text scale
4. Click "Convert to NFP"

**Parameters**:
- **Monitor Width/Height**: Number of monitors to span
- **Text Scale**: Text size multiplier (0.1 - 5.0)
- **Calculated Resize**: Automatically computed based on width × 7 / scale and height × 5 / scale

### Audio/Video Conversion
1. Go to "Audio/Video to DFPWM" tab
2. Select an audio or video file
3. Click "Convert to DFPWM"
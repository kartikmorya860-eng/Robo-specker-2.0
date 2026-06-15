# Robo Speaker 2.0

Robo Speaker 2.0 is a small Python utility that uses the Windows SAPI voice engine to speak text entered by the user.

## Overview

This project includes a single script, `my_speaker.py`, which uses the `pywin32` / `win32com` library to access Microsoft Speech API (SAPI) and speak any text typed into the console.

## Features

- Interactive text input
- Text-to-speech using Windows SAPI
- Exit by typing `bye`
- Simple and lightweight Python script

## Requirements

- Windows 10 or later
- Python 3.7 or newer
- `pywin32` Python package

## Installation

1. Open a command prompt or PowerShell window.
2. Install the dependency:

```bash
pip install pywin32
```

## Usage

Run the project from its folder:

```bash
python my_speaker.py
```

Then type the text you want the speaker to say and press Enter. To stop the program, type:

```text
bye
```

Example:

```text
Enter what you want me to speak : Hello, world!
Enter what you want me to speak : bye
```

## File

- `my_speaker.py` — Interactive speaker script using Windows SAPI.

## Notes

- This project depends on the Windows SAPI speech engine and will not work on non-Windows systems.
- The voice and speech settings can be customized via the SAPI interface in the script.

## File

- `my_speaker.py`: Interactive speaker script.

## Next steps (optional)

- Add command-line flags for non-interactive usage.
- Add voice selection and rate controls.

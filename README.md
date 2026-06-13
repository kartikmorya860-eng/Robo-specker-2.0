# Robo Speaker

Robo Speaker is a small Python utility that uses the Windows SAPI voice engine to speak text you type interactively.

## Description

This project contains a single script, `my_speaker.py`, that uses the `pywin32`/`win32com` library to access the Microsoft Speech API (SAPI) and speak text entered by the user.

## Requirements

- Windows 10 or later (uses SAPI)
- Python 3.7+
- pywin32 (win32com)

Install the dependency with:

```bash
pip install pywin32
```

## Usage

Run the script from the project folder:

```bash
python my_speaker.py
```

The script runs interactively. Type the text you want spoken and press Enter. To exit, type `bye`.

Example session:

```
Enter what you want me to speak : Hello, world!
Enter what you want me to speak : bye
```

## Notes

- This project depends on the Windows SAPI speech engine and will not work on non-Windows systems.
- The voice and speech settings can be customized via the SAPI interface in the script.

## File

- `my_speaker.py`: Interactive speaker script.

## Next steps (optional)

- Add command-line flags for non-interactive usage.
- Add voice selection and rate controls.

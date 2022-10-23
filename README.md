# TI-caption-corrector
Corrects TI caption files, expects captions and images to sit along side each other in the same directory, exects the caption filenaame to be the same as the image filename except having a `.txt` extension.

Attempts to prevent line deletions and insertions to that the line numbers match up with a sorted list of the captioned images.

## Usage

captionCorrector.py K:\directory\path

![demo image](https://user-images.githubusercontent.com/35278260/197368033-70c8ae9b-5f0a-44c9-8bfe-978fe32b5597.png)

Each caption is displayed on a single line, moving between lines moves between images, unsaved changed lines are shown in blue, click save to save edits to caption files.

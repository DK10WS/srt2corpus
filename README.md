# SRT2CORPUS

This project contains a Python class Clean that processes text files by cleaning unwanted elements like timestamps, HTML tags, locations, actions, hyphens, and more. It helps clean and format subtitles into usable and clean corpus for nlp projects.


``` python
from srt2corpus import Clean

# Initialize the Clean class with options for cleaning
cleaner = Clean("path_to_your_file")

# Clean the file and save the result
cleaner.corpus()
```

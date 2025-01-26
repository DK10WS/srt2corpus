import os
import re


class Clean:
    """Initialize the class Clean with the file directory and default options"""

    def __init__(self, dir, html=True, location=True, action=True, hyphens=True):
        self.dir = dir
        self.html = html
        self.location = location
        self.action = action
        self.hyphens = hyphens

    def extractText(self):

        # Check if the file exists in the provided directory
        if not os.path.exists(self.dir):
            raise FileNotFoundError(f"File '{self.dir}' not found")

        # Open the file and read its content
        with open(self.dir, "r", encoding="utf-8") as file:
            text = file.read()

        # Remove timestamp patterns (e.g., "00:00:00,000 --> 00:00:00,000")
        text = re.sub(
            r"\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}", "", text
        )

        # remove HTML tags if the 'html' flag is True
        if self.html:
            text = re.sub(r"</?.+?>", "", text)

        # remove location markers (e.g., {location})
        if self.location:
            text = re.sub(r"{.+?}", "", text)

        # remove action markers (e.g., [action]) if the 'action' flag is True
        if self.action:
            text = re.sub(r"\[.+?\]", "", text)

        # remove hyphens if the 'hyphens' flag is True
        if self.hyphens:
            text = re.sub(r"-", "", text)

        # Remove extra empty lines
        text = re.sub(r"\n+", "\n", text).strip()  # empty lines

        # Remove leading whitespace in lines
        text = re.sub(r"\n\s+", "\n", text)

        # Encode text to handle non-UTF-8 characters gracefully and decode back to ensure clean text
        cleantext = text.encode("utf-8", "replace").decode("utf-8-sig")

        return cleantext

    def corpus(self):

        cleaned_text = self.extractText()

        # Write the cleaned text to a new file with "_cleaned" appended to the original filename
        with open(f"{self.dir}_cleaned.txt", "w", encoding="utf-8") as output_file:
            output_file.write(cleaned_text)

        # Print confirmation
        print(f"{self.dir}_cleaned.txt file created")

        return True

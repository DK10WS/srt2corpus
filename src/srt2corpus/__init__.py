import os
import re


class Clean:
    def __init__(self, dir, html=True, location=True, action=True, hyphens=True):
        self.dir = dir
        self.html = html
        self.location = location
        self.action = action
        self.hyphens = hyphens

    def extractText(self):
        if not os.path.exists(self.dir):
            raise FileNotFoundError(f"File '{self.dir}' not found")

        with open(self.dir, "r", encoding="utf-8") as file:
            text = file.read()

        text = re.sub(
            r"\d+\n\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}", "", text
        )

        if self.html:
            text = re.sub(r"</?.+?>", "", text)

        if self.location:
            text = re.sub(r"{.+?}", "", text)

        if self.action:
            text = re.sub(r"\[.+?\]", "", text)

        if self.hyphens:
            text = re.sub(r"-", "", text)

        text = re.sub(r"\n+", "\n", text).strip()  # empty lines

        text = re.sub(r"\n\s+", "\n", text)

        cleantext = text.encode("utf-8", "replace").decode("utf-8")

        return cleantext

    def corpus(self):
        cleaned_text = self.extractText()

        with open(f"{self.dir}_cleaned.txt", "w", encoding="utf-8") as output_file:
            output_file.write(cleaned_text)
        with open(f"{self.dir}_cleaned.txt", "r") as f:
            lines = f.readlines()

        with open(f"{self.dir}_cleaned.txt", "w") as f:
            f.writelines(lines[1:])

        print(f"{self.dir}_cleaned.txt file created")

        return True

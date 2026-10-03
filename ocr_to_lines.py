"""Photo of a bill or khata page -> lines you can paste into the app.
Usage: python ocr_to_lines.py bill.jpg
Setup: pip install easyocr   (runs locally, no API key)
Lines starting with '# CHECK' could not be read as 'qty item price'; fix them by hand.
"""
import re
import sys

import easyocr

reader = easyocr.Reader(["hi", "en"])  # change 'hi' to your language code
for line in reader.readtext(sys.argv[1], detail=0):
    nums = re.findall(r"\d+(?:\.\d+)?", line)
    words = re.sub(r"[\d.]+", "", line).strip(" -:\u20b9.,")
    if len(nums) >= 2 and words:
        print(f"{nums[0]} {words} {nums[-1]}")
    else:
        print(f"# CHECK: {line}")

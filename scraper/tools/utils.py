from markdown import markdown

import re
import asyncio

from tools.config import categories

#Remove emojis from a text
def remove_emojis(input_string: str) -> str:
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # Emoticons
        "\U0001F300-\U0001F5FF"  # Miscellaneous Symbols and Pictographs
        "\U0001F680-\U0001F6FF"  # Transport and Map Symbols
        "\U0001F700-\U0001F77F"  # Alchemical Symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"  # Enclosed Characters
        "\U0001F926-\U0001F937"  # Supplemental Symbols
        "\U00010000-\U0010FFFF"  # Supplementary Private Use Area
        "]+",
        flags=re.UNICODE
    )
    return emoji_pattern.sub('', input_string)

#Categorize a text with tools.config.categories
def word_match(resume: str) -> list:
    matched_categories = []
    for category, keywords in categories.items():
        if any(keyword.lower() in (resume.lower()) for keyword in keywords):
            matched_categories.append(category)
    return matched_categories

#Retry to get the article if failed
async def get_first_locator_with_retries(page, selector, max_retries=5, delay=1):
    for attempt in range(max_retries):
        try:
            locators = await page.locator(selector).all()
            if locators:
                return locators[0]
            else:
                raise
        except:
            if attempt < max_retries - 1:
                await asyncio.sleep(delay)
            else:
                raise

#Json dump the article object
def article_to_json(title: str,link: str,date: str,resume: str,output: str,categories: list,image: str):
    return {
        "title":f"{title}",
        "link":f"{link}",
        "date":f"{date}",
        "resume":f"{markdown(resume)}", #Use markdown to return HTML
        "output":f"{output}",
        "categories":categories,
        "image":f"{image}",
    }

#Display a progress bar
def progress_bar(progress, total):
    length = 50
    multiplier = 100/length
    percent = length * (progress / float(total))
    bar = '▓' * int(percent) + '▒' * (length - int(percent))
    print(f"\r{bar} Processing websites: {percent*multiplier:.2f}%", end="\r")
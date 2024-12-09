from playwright.async_api import Playwright, async_playwright

from datetime import datetime
import asyncio
import inspect
import json

from website import sources
from tools.utils import article_to_json
from tools.config import folder

async def run(playwright: Playwright) -> None:
    then = datetime.now()
    await processWeb(playwright)
    now = datetime.now()
    print("Processing time: "+str(now - then)+" seconds")

async def processWeb(playwright: Playwright) -> None:
    classes = [obj for _, obj in inspect.getmembers(sources, predicate=inspect.isclass) if obj.__module__ == "website.sources"]
    articles = []
    #Iterates through all sources...
    for classe in classes:
        classe = classe()
        page = await classe.getPageInit(playwright)
        await classe.getCards(page)
        await page.context.close()
        for article in classe.articles:
            #Add every articles in the Class
            articles.append(article_to_json(article['title'],article['href'],article['date'],article['resume'],article['output'],article['categories'],classe.imgUrl))
    #Write the results to result.json
    with open(folder+"result.json",'w', encoding="utf-8") as file:
        file.write(json.dumps(articles, indent=4))

async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright.chromium)

asyncio.run(main())

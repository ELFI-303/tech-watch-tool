from playwright.async_api import Page,Playwright
from bs4 import BeautifulSoup
from dateutil.parser import parse

from abc import ABC,abstractmethod
from requests import get
import re
import html

from tools.config import date_stop
from tools.utils import get_first_locator_with_retries
from analyse.llm import analyze_relevance
from tools.utils import progress_bar

class rss(ABC):
    #Initialize the RSS Feed
    @abstractmethod
    def __init__(self, url: str, corp: str, imgUrl: str):
        self.url = url
        self.corp = corp
        self.imgUrl = imgUrl
        self.articles = []

    #Initialize Playwright Page
    @abstractmethod
    async def getPageInit(self, playwright: Playwright) -> Page:
        browser = await playwright.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        return page
    
    #Get RSS Feed Items, Analyze them and add them to self.articles
    @abstractmethod
    async def getCards(self,page: Page):
        response = get(self.url)
        decoded_feed = html.unescape(response.text)
        clean_feed = re.sub(r"&(?!(amp|lt|gt|quot|apos);)", "&amp;", decoded_feed)
        soup = BeautifulSoup(clean_feed, "xml")
        items = soup.find_all("item")
        total_items = len(items)
        progress_bar(0,total_items)
        i = 1
        for item in items:
            if date_stop >= parse(item.pubDate.string).replace(tzinfo=None):
                return
            corp = await self.navigateArticle(page,item.link.string)
            output,resume,categories = analyze_relevance(corp)
            self.articles.append({
                "title":(item.title.string).replace("\n"," "),
                "date":parse(item.pubDate.string).replace(tzinfo=None).strftime("%d/%m/%Y"),
                "href":item.link.string,
                "corp":corp,
                "resume":resume,
                "output":output,
                "categories":categories
            })
            progress_bar(i,total_items)
            i += 1
        await page.context.close()
    
    #Get the article from the website
    @abstractmethod
    async def navigateArticle(self, page: Page, href: str) -> str:
        new_context = page.context
        new_page = await new_context.new_page()
        await new_page.goto(href)
        try:
            locators = await get_first_locator_with_retries(new_page, self.corp)
        except:
            return ""
        text = await locators.all_inner_texts()
        string = ""
        for el in text:
            string += el
        return string
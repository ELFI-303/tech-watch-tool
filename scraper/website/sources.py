from playwright.async_api import Playwright,Page

from website.rss import rss

class techrepublicRss(rss):
    def __init__(self):
        super().__init__("https://www.techrepublic.com/rssfeeds/topic/cloud/", #The link to the RSS blog.
                         ".article-main", #The locator() used to get the article text.
                         "https://www.techrepublic.com/wp-content/uploads/2022/01/tr-logo-large.png") #An image representing the website. In this example it's the TechRepublic Logo.
        
    async def getPageInit(self, playwright: Playwright) -> Page:
        page = await super().getPageInit(playwright)
        #Initiate the page
        return page
    
    async def getCards(self, page: Page) -> Page:
        page = await super().getCards(page)
        #GetCards
        return page
    
    async def navigateArticle(self, page: Page, href: str) -> str:
        if '/article/' in href:
            return await super().navigateArticle(page, href)
        else:
            #In case the RSS Feed does not publish only articles
            return "This is not an article"

#Add other classes for the websites you want to watch
#class YourFavoriteWebsite(RSS)...


BOT_NAME = "karem"

SPIDER_MODULES = ["karem.spiders"]
NEWSPIDER_MODULE = "karem.spiders"



DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}


ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": True,
    #"timeout": 200000 * 100000,  # 20 seconds
}

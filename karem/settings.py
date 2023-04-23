

BOT_NAME = "karem"

SPIDER_MODULES = ["karem.spiders"]
NEWSPIDER_MODULE = "karem.spiders"


# Add Your ScrapeOps API Key
SCRAPEOPS_API_KEY = 'e4ea08af-ef35-4354-885d-e75b34979a52'

# Add In The ScrapeOps Extension
EXTENSIONS = {
        'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
        }

# Update The Download Middlewares
DOWNLOADER_MIDDLEWARES = {
'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
}

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

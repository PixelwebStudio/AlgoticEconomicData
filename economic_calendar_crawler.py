import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, BrowserConfig

URL = "https://algoticlab.com/calendar.html"

async def main():
    browser_config = BrowserConfig(
        headless=True,
        viewport_width=1920,
        viewport_height=1080,
        verbose=True
    )

    crawler_config = CrawlerRunConfig(
        locale="en-US",
        scan_full_page=True,
        scroll_delay=0.2,
        delay_before_return_html=2.0,
        page_timeout=60000,
        verbose=True,
        wait_for="table"  # صبر تا جدول لود شود
    )

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url=URL, config=crawler_config)
        if result.media and "tables" in result.media:
            tables = result.media["tables"]
            if tables:
                print("\nجدول اقتصادی استخراج‌شده:")
                for i, table in enumerate(tables):
                    print(f"\n--- جدول شماره {i+1} ---\n")
                    print(table)
            else:
                print("هیچ جدول معتبری پیدا نشد.")
        else:
            print("هیچ جدول پیدا نشد یا سایت دسترسی را محدود کرده است.")

if __name__ == "__main__":
    asyncio.run(main()) 
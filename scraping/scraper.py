import logging
from playwright.async_api import async_playwright
from urllib.parse import urljoin


logger = logging.getLogger(__name__)

class Scraper:
    async def fetch_meeting(page_url: str) -> str:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(page_url, wait_until="domcontentloaded", timeout=30000)

            img = await page.wait_for_selector(
                "img[src*='struktura-chgu']",
                timeout=15000,
            )
            src = await img.get_attribute("src")
            await browser.close()

        return urljoin("https://www.chsu.ru", src)


    async def fetch_admission(page_url) -> list[str]:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(page_url, wait_until="domcontentloaded", timeout=30000)
            await page.locator(".block-icon-download-32").first.wait_for(state="visible")
            docx = await page.eval_on_selector_all(
                "a[href$='.docx']",
                "elements => elements.map(el => el.href)",
            )
            pdfs = await page.eval_on_selector_all(
                "a[href$='.pdf']",
                "elements => elements.map(el => el.href)",
            )
            img = await page.eval_on_selector(
                "img[src$='.png'][alt*='Военный учебный центр ЧГУ']",
                "el => el.src",
            ) 
            await browser.close()
            docx = [urljoin(page_url, u) for u in docx if u]
            pdfs = [urljoin(page_url, u) for u in pdfs if u]
            img = [urljoin(page_url, img)]

            docx = list(dict.fromkeys(docx))
            pdfs = list(dict.fromkeys(pdfs))
            img = list(dict.fromkeys(img))

        return {
            "docx": docx,
            "pdfs": pdfs,
            "img": img
        }



    async def fetch_main(page_url: str) -> list[str]:
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=True)
            page = await browser.new_page()

            await page.goto(page_url, wait_until="domcontentloaded", timeout=30000)

            await page.wait_for_selector(
                "img[src$='.jpg']",
                timeout=15000,
            )
            img = await page.eval_on_selector_all(
                "img[src$='.jpg']",
                "elements => elements.map(el => el.src)",
            )
            pdfs = await page.eval_on_selector_all(
                "a[href$='.pdf']",
                "elements => elements.map(el => el.href)",
            )

            await browser.close()

            img = [urljoin(page_url, u) for u in img if u]
            pdfs = [urljoin(page_url, u) for u in pdfs if u]

            img = list(dict.fromkeys(img))
            pdfs = list(dict.fromkeys(pdfs))

        return {
            "image": img,
            "pdfs": pdfs
        }



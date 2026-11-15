import logging
from playwright.async_api import async_playwright, Page
from urllib.parse import urljoin, urlparse, unquote
from pathlib import Path
from bot.config import settings


logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = PROJECT_ROOT / "assets"


class Scraper:
    def __init__(self, assets_dir: Path | None = None):
        self.assets_dir = assets_dir or ASSETS_DIR

    async def fetch_meeting(self, download: bool = False) -> list[str]:
        page_url = "https://www.chsu.ru/struktura-chgu/voennyy-uchebnyy-tsentr/grafik-vstrech.php"
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(page_url, wait_until="domcontentloaded", timeout=30000)

            img = await page.wait_for_selector(
                "img[src*='struktura-chgu']",
                timeout=15000,
            )
            src = await img.get_attribute("src")
            if not src:
                raise RuntimeError("Image src (meeting page) not found")
            url = urljoin("https://www.chsu.ru", src)

            if download:
                saved = await self._download(page, url, self.assets_dir, filename=settings.MEETING_SCHEDULE_IMG)

            await browser.close()

        return {
            "path": str(saved) if saved and not None else None
        }

    async def fetch_admission(self, download: bool = False) -> list[str]:
        page_url = "https://www.chsu.ru/struktura-chgu/voennyy-uchebnyy-tsentr/postuplenie.php"
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

            if download:
                saved = await self._download(page, img, self.assets_dir, filename=settings.GUIDE_IMG) 

            await browser.close()

            docx = [urljoin(page_url, u) for u in docx if u]
            pdfs = [urljoin(page_url, u) for u in pdfs if u]

            docx = list(dict.fromkeys(docx))
            pdfs = list(dict.fromkeys(pdfs))

        return {
            "docx": docx,
            "pdfs": pdfs,
            "img_path": str(saved) if saved else None 
        }

    async def fetch_main(self, download: bool = False) -> list[str]:
        saved = None
        page_url = "https://www.chsu.ru/struktura-chgu/voennyy-uchebnyy-tsentr/"
        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=True)
            page = await browser.new_page()

            await page.goto(page_url, wait_until="domcontentloaded", timeout=30000)
            await page.locator(".page-content").first.wait_for(state="visible")
            img = await page.eval_on_selector(
                "img[src$='.jpg']",
                "el => el.src",
            )
            pdfs = await page.eval_on_selector_all(
                "a[href$='.pdf']",
                "elements => elements.map(el => el.href)",
            )

            if download:
                saved = await self._download(page, img, self.assets_dir, filename=settings.TITLE_IMG)

            await browser.close()

            pdfs = [urljoin(page_url, u) for u in pdfs if u]
            pdfs = list(dict.fromkeys(pdfs))

        return {
            "pdfs": pdfs,
            "img_path": str(saved)
        }

    async def _download(self, page: Page, url: str, dest_dir: Path, filename: str | None = None) -> Path:
        dest_dir.mkdir(parents=True, exist_ok=True)
        if filename:
            path = dest_dir / filename
        else:
            path = dest_dir / Path(unquote(urlparse(url).path)).name

        response = await page.request.get(url)
        if not response.ok:
            raise RuntimeError(f"HTTP {response.status} for {url}")

        data = await response.body()
        if not data:
            raise RuntimeError(f"Empty bode for {url}")

        path.write_bytes(data)
        logger.info(f"Saved {path} ({len(data)} bytes)")
        return path
 


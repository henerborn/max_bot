import logging
from scraping import Scraper
from bot.config import settings
from database import LinksRepository, DatabaseManager

logger = logging.getLogger(__name__)

scraper = Scraper()
db_manager = DatabaseManager(settings.DB_URL)
repo = LinksRepository(db_manager)

async def parse_task():
    """Parse CHSU-website, fetch into DB needed info (url on public pdfs and docx), save images locally"""
    await db_manager.init_db()
    main_data = await scraper.fetch_main(download=True)
    pdfs = main_data["pdfs"]
    await repo.new_url("regulations_about_VUC", pdfs[1])
    await repo.new_url("regulations_about_competetive_selection", pdfs[2])
    await repo.new_url("presentation_of_VUC", pdfs[3])

    admission_data = await scraper.fetch_admission(download=True)
    pdfs = admission_data["pdfs"]
    await repo.new_url("phisical_preparation_assessment", pdfs[1])
    docx = admission_data["docx"]
    await repo.new_url("condidate_profile", docx[0])
    await repo.new_url("autobiography", docx[1])
    await repo.new_url("personal_data_agreement", docx[2])

    await scraper.fetch_meeting(download=True)


    
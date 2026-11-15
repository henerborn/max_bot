import asyncio
import logging
import schedule
from bot.config import settings
from workers.parse_task import parse_task

logger = logging.getLogger(__name__)

async def run_parse():
    try:
        logger.info("Starting scheduled parsing...")
        await parse_task()
        logger.info("Scheduled parsing completed")
    except Exception:
        logger.exception("Scheduled parsing failed")

def schedule_parse():
    asyncio.create_task(run_parse())

async def main():
    schedule.every().day.at(settings.PARSE_TIME).do(schedule_parse)
    logger.info("Scheduler started")

    while True:
        schedule.run_pending()
        seconds = schedule.idle_seconds()
        if seconds is not None:
            await asyncio.sleep(seconds)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Scheduler shutdown...")                                                                        
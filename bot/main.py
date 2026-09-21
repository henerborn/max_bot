import asyncio
import logging
from maxapi import Bot, Dispatcher
from maxapi.types import BotStarted, Command, MessageCreated
from bot.config import settings
from bot.utils.logging import configure_logging
from bot.handlers import include_routers

logger = logging.getLogger(__name__)

bot = Bot(settings.BOT_TOKEN)
dp = Dispatcher()


async def main():
    include_routers(dp)
    configure_logging(logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot shutdown...")


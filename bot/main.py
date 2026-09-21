import asyncio
import logging
from bot.config import settings
from maxapi import Bot, Dispatcher
from maxapi.enums.format import Format
from bot.handlers import include_routers
from bot.utils.logging import configure_logging
from bot.utils.commands_list import setup_commands

logger = logging.getLogger(__name__)

bot = Bot(settings.BOT_TOKEN, format=Format.HTML)
dp = Dispatcher()


async def main():
    include_routers(dp)
    configure_logging(logging.INFO)
    await setup_commands(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot shutdown...")


import logging
from maxapi import Bot
from maxapi.types import BotCommand

logger = logging.getLogger(__name__)

async def setup_commands(bot: Bot): 
    await bot.set_commands(
        BotCommand(
            name="main",
            description="Главная страница"
        ),
        BotCommand(
            name="help",
            description="Помощь"
        ),
        BotCommand(
            name="admission",
            description="Поступление"
        ),
        BotCommand(
            name="meetings",
            description="График встреч"
        ),
        BotCommand(
            name="contacts",
            description="Контакты"
        )
    )
    logger.info("Bot commands successfully configured")
import logging
from maxapi import F
from maxapi.types import BotStarted, Command, MessageCreated, MessageCallback
from maxapi import Router
from bot.handlers.messages import Messages

logger = logging.getLogger(__name__)

router = Router()


# /main BotStarted, Callback and Message handlers
@router.bot_started()
async def bot_started(event: BotStarted):
    await Messages.main_info(event.bot, chat_id=event.chat_id)

@router.message_created(Command("main"))
async def main_message(event: MessageCreated):
    await Messages.main_info(bot=event.bot, chat_id=event.chat.chat_id)

@router.message_callback(F.callback.payload == "main")
async def main_callback(callback: MessageCallback):
    await Messages.main_info(callback.bot, chat_id=callback.chat.chat_id)


# /admission Callback and Message handlers
@router.message_callback(F.callback.payload == "admission")
async def admission_callback(callback: MessageCallback):
    await Messages.admission_info(callback.bot, chat_id=callback.chat.chat_id)

@router.message_created(Command("admission"))
async def admission_message(event: MessageCreated):
    await Messages.admission_info(event.bot, chat_id=event.chat.chat_id)


# /meeting Callback and Message handlers
@router.message_callback(F.callback.payload == "meeting_schedule")
async def meeting_callback(callback: MessageCallback):
    await Messages.meeting_info(callback.bot, chat_id=callback.chat.chat_id)

@router.message_created(Command("meeting"))
async def meeting_message(event: MessageCreated):
    await Messages.meeting_info(event.bot, chat_id=event.chat.chat_id)


# /contacts Callback and Message handlers
@router.message_callback(F.callback.payload == "contacts")
async def contacts_callback(callback: MessageCallback):
    await Messages.contacts_info(callback.bot, chat_id=callback.chat.chat_id)

@router.message_created(Command("contacts"))
async def contacts_message(event: MessageCreated):
    await Messages.contacts_info(event.bot, chat_id=event.chat.chat_id)


# /help Callback and Message handlers
@router.message_callback(F.callback.payload == "help")
async def help_callback(callback: MessageCallback):
    await Messages.help(callback.bot, chat_id=callback.chat.chat_id)

@router.message_created(Command("help"))
async def help_message(event: MessageCreated):
    await Messages.help(event.bot, chat_id=event.chat.chat_id)


from maxapi import Dispatcher
from bot.handlers.user import router as user_router

def include_routers(dp: Dispatcher):
    dp.include_routers(user_router)
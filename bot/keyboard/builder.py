from maxapi.utils.inline_keyboard import InlineKeyboardBuilder
from maxapi.types import (
    ChatButton, 
    LinkButton, 
    CallbackButton, 
    MessageButton, 
    ButtonsPayload, 
    RequestContactButton, 
    OpenAppButton, 
)

class Builder:
    @staticmethod
    def main_kb():
        buttons = [
            [CallbackButton(text="Поступление", payload="admission")],
            [CallbackButton(text="График встреч", payload="meeting_schedule")],
            [CallbackButton(text="Контакты", payload="contacts")]
        ]
        payload = ButtonsPayload(buttons=buttons).pack()
        return payload
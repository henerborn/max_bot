import logging
from maxapi.types import (
    ChatButton, 
    LinkButton, 
    CallbackButton, 
    MessageButton, 
    ButtonsPayload, 
    RequestContactButton, 
    OpenAppButton, 
)

logger = logging.getLogger(__name__)

class Builder:
    @staticmethod
    def main_kb():
        buttons = [
            [CallbackButton(text="Поступление", payload="admission")],
            [CallbackButton(text="График встреч", payload="meeting_schedule")],
            [CallbackButton(text="Контакты", payload="contacts")],
            [CallbackButton(text="Помощь", payload="help")]
        ]
        payload = ButtonsPayload(buttons=buttons).pack()
        return payload

    @staticmethod
    def admission_kb():
        buttons = [
            [CallbackButton(text="На главную", payload="main")],
            [CallbackButton(text="График встреч", payload="meeting_schedule")],
            [CallbackButton(text="Контакты", payload="contacts")],
            [CallbackButton(text="Помощь", payload="help")]
        ]
        payload = ButtonsPayload(buttons=buttons).pack()
        return payload

    @staticmethod
    def meeting_schedule_kb():
        buttons = [
            [CallbackButton(text="На главную", payload="main")],
            [CallbackButton(text="Поступление", payload="admission")],
            [CallbackButton(text="Контакты", payload="contacts")],
            [CallbackButton(text="Помощь", payload="help")]
        ]
        payload = ButtonsPayload(buttons=buttons).pack()
        return payload

    @staticmethod
    def contacts_kb():
        buttons = [
            [CallbackButton(text="На главную", payload="main")],
            [CallbackButton(text="Поступление", payload="admission")],
            [CallbackButton(text="График встреч", payload="meeting_schedule")],
            [CallbackButton(text="Помощь", payload="help")]
        ]
        payload = ButtonsPayload(buttons=buttons).pack()
        return payload
    
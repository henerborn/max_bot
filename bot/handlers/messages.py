import logging
from maxapi import Bot
from maxapi.types import InputMedia
from bot.keyboard import Builder

logger = logging.getLogger(__name__)

class Messages:
    @staticmethod
    async def main_info(bot: Bot, chat_id: int):
        await bot.send_message(
            chat_id=chat_id,
            attachments=[InputMedia(path="assets/title1.jpg"), Builder.main_kb()],
            text=(
                f"<h1>О военном учебном центре</h1>\n\n"
                f"Центр готовит студентов по военно-учетным специальностям для Воздушно-космических сил Минобороны России. Студенты, которые проходят подготовку по программам факультета военного образования, будут участвовать в учебных военных сборах.\n\n"
                f"<b>Критерии отбора устанавливаются военкоматом</b>\n"
                f"- прохождение медицинской комиссиии\n"
                f"- прохождение психологического тестирования\n"
                f"- рейтинг в учебной деятельности по итогам 1 курса\n\n"
                f"<b>Прием граждан в Военный учебный центр проводится на конкурсной основе.</b>\n\n"
                f"<b>Для участия в конкурсном отборе для допуска к военной подготовке рассматриваются граждане</b> в возрасте до 30 лет, обучающиеся по очной форме обучения в Университете по специальностям соответствующим, квалификационным требованиям по военно-учетным специальностям.\n\n"
                f"<b>1. Мероприятия конкурсного отбора проводятся заранее</b>, для начинающих обучение стартует в сентябре.\n"
                f"<b>2. До начала проведения отбора  проводится общее собрание</b> с гражданами из числа обучающихся, желающих пройти военную подготовку.\n"
                f"<b>3. Указанные граждане в срок до 1 апреля через институты (факультет) подают заявления об участии в конкурсном отборе для допуска к военной подготовке по военно-учетной специальности.</b>\n"
                f"<b>4. На основании поданных заявлений в ВУЦ составляется список граждан из числа обучающихся, который утверждается</b>. Граждане, внесенные в указанный список, проходят конкурсный отбор, который состоит из предварительного и основного отбора.\n\n"
                f"-- <b>предварительный отбор состоит из</b> медицинского освидетельствования и профессионального психологического отбора.\n"
                f"-- <b>к основному отбору допускаются кандидаты</b>, прошедшие предварительный отбор в военном комиссариате по месту воинского учета. Для дальнейшего рассмотрения результатов предварительного отбора кандидатов: их текущей успеваемости, оценки уровня физической подготовленности.\n"

            )
        )
        await bot.send_message(
            chat_id=chat_id,
            attachments=[InputMedia(path="assets/ВУЦ Презентация.pdf")]
        )
        await bot.send_message(
                chat_id=chat_id,
                attachments=[InputMedia(path="assets/Положение о порядке проведения конкурсного отбора.pdf")]
            )
        await bot.send_message(
                chat_id=chat_id,
                attachments=[InputMedia(path="assets/Положение о Военном учебном центре.pdf")]
            )

    @staticmethod
    async def admission_info(bot: Bot, chat_id: int):
        await bot.send_message(
            chat_id=chat_id,
            attachments=[InputMedia(path="assets/памятка.png"), Builder.admission_kb()],
            text=(
                "<h1>Памятка студенту, поступающему в ВУЦ</h1>\n\n"
                "<i>Начальник отделения набора кадров:</i>\n"
                "<pre>+7 953 519-55-21</pre>"
            )
        )
        # await bot.send_message(
        #     chat_id=chat_id,
        #     attachments=[InputMedia(path="assets/памятка.png")]
        # )
        # await bot.send_message(
        #     chat_id=chat_id,
        #     attachments=[InputMedia(path="assets/памятка.png")]
        # )
        # await bot.send_message(
        #     chat_id=chat_id,
        #     attachments=[InputMedia(path="assets/памятка.png")]
        # )
        # await bot.send_message(
        #     chat_id=chat_id,
        #     attachments=[InputMedia(path="assets/памятка.png")]
        # )
        # await bot.send_message(
        #     chat_id=chat_id,
        #     attachments=[InputMedia(path="assets/памятка.png")]
        # )    
        
    @staticmethod
    async def meeting_info(bot: Bot, chat_id: int):
        await bot.send_message(
            chat_id=chat_id,
            attachments=[InputMedia(path="assets/grafik2026.jpg"), Builder.admission_kb()],
            text="При себе необходимо иметь паспорт и студенческий билет!"
        )

    @staticmethod
    async def contacts_info(bot: Bot, chat_id: int):
        await bot.send_message(
            chat_id=chat_id,
            attachments=[Builder.contacts_kb()],
            text=(
                "<h1>Контакты</h1>\n\n"
                "По вопросам поступления в Военный учебный центр Череповецкого государственного университета обращаться по адресу: Советский пр. д. 25 в часы работы университета.\n\n"
                "<i>Телефон учебной части</i>: +7 921 054-27-99"
            )
        )

    @staticmethod
    async def help(bot: Bot, chat_id: int):
        await bot.send_message(
            chat_id=chat_id,
            attachments=[],
            text=(
                "<h1>Команды для управления ботом:</h1>\n\n"
                "<blockquote><b>/help</b> - помощь в управлении ботом\n\n"
                "<b>/main</b> - главная страница бота\n\n"
                "<b>/admission</b> - страница 'Поступлениe в ВУЦ'\n\n"
                "<b>/meeting</b> - страница 'График встреч'\n\n"
                "<b>/contacts</b> - страница 'Контакты'</blockquote>\n\n"

                "Более подробную информацию о ВУЦ можно получить на <a href='https://www.chsu.ru/struktura-chgu/voennyy-uchebnyy-tsentr/'>официальном сайте ЧГУ</a>"
            )
        )
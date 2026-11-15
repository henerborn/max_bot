import logging
from maxapi import Bot
from maxapi.types import InputMedia
from bot.keyboard import Builder
from bot.config import settings
from database import DatabaseManager, LinksRepository

logger = logging.getLogger(__name__)
db_manager = DatabaseManager(settings.DB_URL)
repo = LinksRepository(db_manager)

class Messages:
    @staticmethod
    async def main_info(bot: Bot, chat_id: int):
        pdf1 = await repo.get_url("regulations_about_VUC")
        pdf2 = await repo.get_url("regulations_about_competetive_selection")
        pdf3 = await repo.get_url("presentation_of_VUC")
        await bot.send_message(
            chat_id=chat_id,
            attachments=[InputMedia(path=f"assets/{settings.TITLE_IMG}"), Builder.main_kb()],
            text=(
                f"<h1>О военном учебном центре</h1>\n\n"
                f"Центр готовит студентов по военно-учетным специальностям для Воздушно-космических сил Минобороны России. Студенты, которые проходят подготовку по программам факультета военного образования, будут участвовать в учебных военных сборах.\n\n"
                f"<b>Критерии отбора устанавливаются военкоматом</b>\n"
                f"- прохождение медицинской комиссии\n"
                f"- прохождение психологического тестирования\n"
                f"- рейтинг в учебной деятельности по итогам 1 курса\n\n"
                f"<b>Прием граждан в Военный учебный центр проводится на конкурсной основе.</b>\n\n"
                f"<b>Для участия в конкурсном отборе для допуска к военной подготовке рассматриваются граждане</b> в возрасте до 30 лет, обучающиеся по очной форме обучения в Университете по специальностям соответствующим, квалификационным требованиям по военно-учетным специальностям.\n\n"
                f"<b>1. Мероприятия конкурсного отбора проводятся заранее</b>, для начинающих обучение стартует в сентябре.\n"
                f"<b>2. До начала проведения отбора  проводится общее собрание</b> с гражданами из числа обучающихся, желающих пройти военную подготовку.\n"
                f"<b>3. Указанные граждане в срок до 1 апреля через институты (факультет) подают заявления об участии в конкурсном отборе для допуска к военной подготовке по военно-учетной специальности.</b>\n"
                f"<b>4. На основании поданных заявлений в ВУЦ составляется список граждан из числа обучающихся, который утверждается</b>. Граждане, внесенные в указанный список, проходят конкурсный отбор, который состоит из предварительного и основного отбора.\n\n"
                f"-- <b>предварительный отбор состоит из</b> медицинского освидетельствования и профессионального психологического отбора.\n"
                f"-- <b>к основному отбору допускаются кандидаты</b>, прошедшие предварительный отбор в военном комиссариате по месту воинского учета. Для дальнейшего рассмотрения результатов предварительного отбора кандидатов: их текущей успеваемости, оценки уровня физической подготовленности.\n\n"
                f"🔸 <a href='{pdf1}'>Положение о Военном учебном центре</a>\n"
                f"🔸 <a href='{pdf2}'>Положение о порядке проведения конкурсного отбора</a>\n"
                f"🔸 <a href='{pdf3}'>Презентация ВУЦ</a>\n" 
            )
        )

    @staticmethod
    async def admission_info(bot: Bot, chat_id: int):
        pdf1 = await repo.get_url("phisical_preparation_assessment")
        docx1 = await repo.get_url("condidate_profile")
        docx2 = await repo.get_url("autobiography")
        docx3 = await repo.get_url("personal_data_agreement")
        await bot.send_message(
            chat_id=chat_id,
            attachments=[InputMedia(path=f"assets/{settings.GUIDE_IMG}"), Builder.admission_kb()],
            text=(
                "<h1>Памятка студенту, поступающему в ВУЦ</h1>\n\n"     
                "<i>Начальник отделения набора кадров:</i>\n"
                "<pre>+7 953 519-55-21</pre>\n\n"
                f"🔸 <a href='{pdf1}'>График проведения оценки физической подготовленности</a>\n"
                f"<b>Бланки для заполнения:</b>\n\n"
                f"🔹 <a href='{docx1}'>Характеристика на кандидата</a>\n"
                f"🔹 <a href='{docx2}'>Автобиография</a>\n"      
                f"🔹 <a href='{docx3}'>Согласие на обработку персональных данных в ВУЦ</a>\n\n" 
            )
        )  
        
    @staticmethod
    async def meeting_info(bot: Bot, chat_id: int):
        await bot.send_message(
            chat_id=chat_id,
            attachments=[InputMedia(path=f"assets/{settings.MEETING_SCHEDULE_IMG}"), Builder.meeting_schedule_kb()],
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
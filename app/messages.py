# все сообщения оптравляемые в тг бота
from create_bot import bot

import os
import re

from dotenv import load_dotenv

load_dotenv()

CHAT_ID = os.getenv("CHAT_ID")


def start():
    message = "Вас приветствует компания TT-ENGINEERING"
    return message


def escape(text: str) -> str:
    return re.sub(r'([_*\[\]()~`>#+\-=|{}.!\\])', r'\\\1', text)


async def send_order(model, user):
    first_name = escape(user.first_name or '—')
    last_name = escape(user.last_name or '—')
    username = escape(f"@{user.username}") if user.username else '\\—'
    model_escaped = escape(model)

    message = (
        f"*Заказ аппарата {model_escaped}*\n\n"
        f"Информация о заказе:\n"
        f"Имя: {first_name}\n"
        f"Фамилия: {last_name}\n"
        f"Username: {username}\n"
        f"Товар: {model_escaped}"
    )

    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="MarkdownV2")

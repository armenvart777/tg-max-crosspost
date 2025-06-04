"""
Кроспостинг бот: Telegram → MAX
Мониторит TG канал и дублирует посты в MAX канал.
"""

import asyncio
import logging
import os
import re

import aiohttp
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

TG_BOT_TOKEN = os.getenv('TG_BOT_TOKEN', '')
TG_CHANNEL_ID = int(os.getenv('TG_CHANNEL_ID', '0'))  # числовой ID канала

MAX_BOT_TOKEN = os.getenv('MAX_BOT_TOKEN', '')
MAX_CHANNEL_ID = int(os.getenv('MAX_CHANNEL_ID', '0'))  # числовой chat_id канала в MAX

MAX_API_BASE = 'https://botapi.max.ru'

bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher()
http: aiohttp.ClientSession = None


async def max_request(method: str, path: str, **kwargs) -> dict:
    """Выполняет запрос к MAX Bot API."""
    ...

async def max_send(text: str, attachments: list = None) -> dict:
    """Отправляет сообщение в MAX канал."""
    ...

async def upload_photo_from_url(photo_url: str) -> str | None:
    """Загружает фото по URL в MAX и возвращает token."""
    ...

@dp.channel_post()
async def on_channel_post(message: Message):
    """Обработчик новых постов в TG канале."""
    ...

async def main():
    ...

if __name__ == '__main__':
    asyncio.run(main())

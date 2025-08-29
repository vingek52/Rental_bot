import logging
import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

from client_handler import client_router


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(client_router)


async def main():
    print("ZZZZ")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

asyncio.run(main())
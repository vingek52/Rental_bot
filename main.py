import logging
import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from dotenv import find_dotenv, load_dotenv



load_dotenv(find_dotenv())
from middlewares.db import DataBaseSession
from database.engine import create_db, drop_db, session_maker
from client_handler import client_router


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(client_router)


async def on_startup(bot):
    
    run_param = False
    
    if run_param:
        await drop_db()
        
    await create_db()

async def on_shutdown(bot):
    print("Бот лег")
    

async def main():
    
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.update.middleware(DataBaseSession(session_pool=session_maker))
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

asyncio.run(main())
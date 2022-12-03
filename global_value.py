from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

array = []
TOKEN = " ";
bot = Bot(token = TOKEN)
dp = Dispatcher(bot = bot, storage=MemoryStorage())
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

array = []
TOKEN = "5935207453:AAEJ8AgmCpwHf8OO0V4jlVqDwC2UPtGWJL4";
bot = Bot(token = TOKEN)
dp = Dispatcher(bot = bot, storage=MemoryStorage())
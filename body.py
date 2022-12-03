from datetime import datetime
import time
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from global_value import *
from Button_file import*

@dp.message_handler(commands = ['start'])
async def StartHandler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привет, {message.from_user.full_name}!", reply_markup = kb_client)
    await bot.send_message(message.from_user.id, f"Я бот, который умеет вести расходы \nЯ твой незаменимый помошник! ", reply_markup = kb_client)
    
@dp.message_handler(commands = ['help'])
async def StartHandler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привет, {message.from_user.full_name}!\nкак я уже говорил это бот для учёта расходов\nон может записывать и показывать твои расходы\nимеет фильтры:\nпо категории расходов\nпо времени")
    await bot.send_message(message.from_user.id, f"Я бот, который умеет вести расходы \nЯ твой незаменимый помошник! ", reply_markup = kb_client)
    
@dp.message_handler()
async def UpHandler(message: types.Message):
    await bot.send_message(message.from_user.id, "Ошибка")
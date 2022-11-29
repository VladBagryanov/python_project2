from Button_file import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from global_value import *

@dp.message_handler(commands = ['Посмотреть_все_расходы'])
async def PrintHandler(message: types.Message):
    user_id = message.from_user.id
    cheker = False
    for i in array:
        if i['user_id'] == user_id:
            cheker = True
            await bot.send_message(message.from_user.id, f"Категория: {i['category']} \nСумма: {i['value']} рублей \nДата: {i['data']}")
    if cheker:
        await bot.send_message(message.from_user.id, "Это все ваши расходы", reply_markup = kb_client)
    else:
        await bot.send_message(message.from_user.id, "У вас нет занесённых в базу расходов", reply_markup = kb_client)

@dp.message_handler(commands = ['Сумма_всех_расходов'])
async def PrintHandler(message: types.Message):
    user_id = message.from_user.id
    print_sum = 0
    for i in array:
        if i['user_id'] == user_id:
            print_sum += int(i['value'])
    await bot.send_message(message.from_user.id, f"Ваши расходы за всё время составили {print_sum} рублей", reply_markup = kb_client)
from Button_file import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import string
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from global_value import *

def min_data(first_data, second_data):
    if int(first_data[6:] + first_data[3:5] + first_data[:2]) <= int(second_data[6:] + second_data[3:5] + second_data[:2]):
        return True
    return False

class print_expenses(StatesGroup):
    category = State()
    all_data = State()
    data_begin = State()
    data_end = State()
    tipe = State()

@dp.message_handler(commands = ['Посмотреть_определённые_расходы'], state = None)
async def UpHandler(message: types.Message):
    state = dp.current_state(user = message.from_user.id)
    await state.set_state(print_expenses.category)
    await print_expenses.category.set()
    await bot.send_message(message.from_user.id, f"Уважаемый, {message.from_user.full_name}, выбери категорию, которая тебя интерисует",  reply_markup = print_kb)

@dp.message_handler(state = print_expenses.category)
async def UpHandler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await bot.send_message(message.from_user.id, "Теперь выбери период, за который тебя интерисуют расходы", reply_markup = print_data_kb)
    await print_expenses.next()

@dp.message_handler(state = print_expenses.all_data)
async def UpHandler(message: types.Message, state: FSMContext):
    if message.text == "Всё время":
        async with state.proxy() as data:
            data['all_data'] = True
            data['data_begin'] = 0
            data['data_end'] = 0
            await print_expenses.next()
            await print_expenses.next()
            await print_expenses.next()
            await bot.send_message(message.from_user.id, "Теперь выбери действие с расходами",  reply_markup = print_act_kb)
            return
    async with state.proxy() as data:
        data['all_data'] = False
    await bot.send_message(message.from_user.id, "Теперь введи дату начала периода")
    await print_expenses.next()

@dp.message_handler(state = print_expenses.data_begin)
async def UpHandler(message: types.Message, state: FSMContext):
    if len(message.text) != 10 or message.text[:2].isdigit() != True or message.text[2] != '.' or message.text[3:5].isdigit() != True or message.text[5] != '.' or message.text[6:].isdigit() != True:
        await bot.send_message(message.from_user.id, "Это не дата, ты хочешь обмануть меня")
        await bot.send_message(message.from_user.id, "Введи дату заново, только на этот раз правильно")
        return
    async with state.proxy() as data:
        data['data_begin'] = message.text
    await bot.send_message(message.from_user.id, "Теперь введи дату конца периода")
    await print_expenses.next()

@dp.message_handler(state = print_expenses.data_end)
async def UpHandler(message: types.Message, state: FSMContext):
    if len(message.text) != 10 or message.text[:2].isdigit() != True or message.text[2] != '.' or message.text[3:5].isdigit() != True or message.text[5] != '.' or message.text[6:].isdigit() != True:
        await bot.send_message(message.from_user.id, "Это не дата, ты хочешь обмануть меня")
        await bot.send_message(message.from_user.id, "Введи дату заново, только на этот раз правильно")
        return
    async with state.proxy() as data:
        data['data_end'] = message.text
    await bot.send_message(message.from_user.id, "Теперь выбери действие с расходами",  reply_markup = print_act_kb)
    await print_expenses.next()

@dp.message_handler(state = print_expenses.tipe)
async def UpHandler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['tipe'] = message.text
    await bot.send_message(message.from_user.id, "Вот ваши расходы")
    user_id = message.from_user.id
    print_sum = 0
    for i in array:
        if data['user_id'] == message.from_user.id and (data['all_data'] or (min_data(data['data_begin'], i['data']) and min_data(i['data'], data['data_end']))) and (data['category'] == 'Все категории' or data['category'] == i['category']):
            if data['tipe'] == 'сумма':
                print_sum += int(i[value])
            else:
                await bot.send_message(message.from_user.id, f"Категория: {i['category']} \nСумма: {i['value']} рублей \nДата: {i['data']}")
    if data['tipe'] == 'сумма':
        await bot.send_message(message.from_user.id, f"{message.from_user.first_name}, ваши расходы за данный период составили: {print_sum} рублей")
    await bot.send_message(message.from_user.id, f"{message.from_user.full_name}, что дальше?", reply_markup = kb_client)
    await state.set_state(None)
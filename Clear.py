from aiogram import Bot, Dispatcher, types
import asyncio
from Button_file import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from global_value import *

class delete(StatesGroup):
    confirm = State()

@dp.message_handler(commands = ['Очистить_данные'], state = None)
async def UpHandler(message: types.Message):
    state = dp.current_state(user = message.from_user.id)
    await state.set_state(delete.confirm)
    await delete.confirm.set()
    await bot.send_message(message.from_user.id, f'{message.from_user.full_name}, ты точно хочешь очитстить все данные?')
    await bot.send_message(message.from_user.id, f'Востановить их получится',  reply_markup = print_conf_kb)

@dp.message_handler(state = delete.confirm)
async def UpHandler(message: types.Message, state: FSMContext):
    await state.set_state(None)
    user_id = message.from_user.id
    if message.text == 'Да':
        for i in array:
            if i['user_id'] == user_id:
                array.remove(i)
        await bot.send_message(message.from_user.id, f'{message.from_user.full_name}, я удалил все твои платежи', reply_markup = kb_client)
    else:
        await bot.send_message(message.from_user.id, f'{message.from_user.full_name}, я отменил операцию', reply_markup = kb_client)
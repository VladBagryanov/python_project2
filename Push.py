import string
from Button_file import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from global_value import *

class expenses(StatesGroup):
    category = State()
    value = State()
    data = State()

@dp.message_handler(commands = ['Добавить_расходы'], state = None)
async def UpHandler(message: types.Message):
    state = dp.current_state(user = message.from_user.id)
    await state.set_state(expenses.category)
    await expenses.category.set()
    await bot.send_message(message.from_user.id, f"Уважаемый, {message.from_user.full_name}, куда ты потратил деньги?",  reply_markup = url_kb)

@dp.message_handler(state = expenses.category)
async def UpHandler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text
    await bot.send_message(message.from_user.id, "И сколько ты потратил в рублях?")
    await expenses.next()
    
@dp.message_handler(state = expenses.value)
async def UpHandler(message: types.Message, state: FSMContext):
    if message.text.isdigit() != True:
        await bot.send_message(message.from_user.id, f"{message.from_user.full_name}, я хотел услышать число, а это не число")
        await bot.send_message(message.from_user.id, "Введи сумму заново")
        return
    async with state.proxy() as data:
        data['value'] = message.text
    await bot.send_message(message.from_user.id, f"И когда ты только успел?")
    await bot.send_message(message.from_user.id, f"{message.from_user.full_name}, я жду ответа в формате дд.мм.гггг ")
    await expenses.next()

@dp.message_handler(state = expenses.data)
async def UpHandler(message: types.Message, state: FSMContext):
    if len(message.text) != 10 or message.text[:2].isdigit() != True or message.text[2] != '.' or message.text[3:5].isdigit() != True or message.text[5] != '.' or message.text[6:].isdigit() != True:
        await bot.send_message(message.from_user.id, "Это не дата, ты хочешь обмануть меня")
        await bot.send_message(message.from_user.id, "Введи дату заново, только на этот раз правильно")
        return    
    async with state.proxy() as data:
        data['data'] = message.text
        data['user_id'] = message.from_user.id
    await bot.send_message(message.from_user.id, f"{message.from_user.full_name}, я всё записал", reply_markup = kb_client)
    array.append(data)
    await state.set_state(None)
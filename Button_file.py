from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
#кнопки меню
button1 = KeyboardButton('/Добавить_расходы')
button2 = KeyboardButton('/Посмотреть_определённые_расходы')
button3 = KeyboardButton('/Посмотреть_все_расходы')
button4 = KeyboardButton('/Сумма_всех_расходов')
button5 = KeyboardButton('/help')
button6 = KeyboardButton('/Очистить_данные')
kb_client = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
kb_client.add(button1).add(button2).add(button3).add(button4).add(button5).insert(button6)
#кнопки выбора категории ввода
button1 = KeyboardButton('Еда')
button2 = KeyboardButton('Рестораны')
button3 = KeyboardButton('Магазины')
button4 = KeyboardButton('Здоровье')
button5 = KeyboardButton('Развлечения')
button6 = KeyboardButton('Образование')
button7 = KeyboardButton('Другое')
url_kb = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
url_kb.add(button1).insert(button2).add(button3).insert(button4).add(button5).insert(button6).add(button7)
#кнопки выбора категории вывода
button8 = KeyboardButton('Все категории')
print_kb = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
print_kb.add(button8).add(button1).insert(button2).add(button3).insert(button4).add(button5).insert(button6).add(button7)
#кнопки выбора периода вывода
button1 = KeyboardButton('Всё время')
button2 = KeyboardButton('Определённый период')
print_data_kb = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
print_data_kb.add(button1).add(button2)
#кнопки выбора действия
button1 = KeyboardButton('Все расходы')
button2 = KeyboardButton('Сумма')
print_act_kb = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
print_act_kb.add(button1).add(button2)
#кнопки подтверждения
button1 = KeyboardButton('Да')
button2 = KeyboardButton('Нет')
print_conf_kb = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
print_conf_kb.add(button1).add(button2)
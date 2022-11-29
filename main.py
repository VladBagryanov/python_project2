from aiogram import Bot, Dispatcher, executor, types
import asyncio
from Clear import *
from global_value import *
from Push import *
from watch import *
from watch_all import *
from body import *

executor.start_polling(dp, skip_updates = True)
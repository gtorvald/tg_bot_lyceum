from aiogram import Bot, Dispatcher, executor, types
import datetime
import json

from utils import token # существует только на сервере
from src import lessons

bot = Bot(token.BOT_TOKEN)
dp = Dispatcher(bot)

LESSONS_PATH = 'data/time_table.json'

with open(LESSONS_PATH) as file:
    data = json.load(file)

@dp.message_handler(commands=['now'])
async def get_text_messages(message: types.Message):
    response = lessons.get_current_lesson(data)
    await bot.send_message(message.chat.id, response)

executor.start_polling(dp)

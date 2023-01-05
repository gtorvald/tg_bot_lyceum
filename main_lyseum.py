from aiogram import Bot, Dispatcher, executor, types
import datetime

from utils import token # существует только на сервере
from src import lessons

bot = Bot(token.BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['now'])
async def get_text_messages(message: types.Message):
    response = lessons.get_current_lesson()
    await bot.send_message(message.chat.id, response)

executor.start_polling(dp)

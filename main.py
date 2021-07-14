import logging
from aiogram import Bot, Dispatcher, executor, types
import os
import utils

TOKEN = os.environ["TELEGRAM_TOKEN"]

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="bruh")
async def send_bruh_signs_count(message: types.Message):
    """
    Send signs count
    """
    sc = utils.download_signs_count()
    await message.reply(str(sc))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

import logging
from aiogram import Bot, Dispatcher, executor, types
import os
import utils

TOKEN = os.environ["TELEGRAM_TOKEN"]
POLL_CHAT = -1001472813343

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="bruh")
async def send_bruh_signs_count(message: types.Message):
    """
    Send signs count
    """
    sc = utils.download_signs_count()
    await message.reply(str(sc))


@dp.message_handler(content_types=["poll"])
async def pin_poll(message):
    if message.chat.id == POLL_CHAT:
        await message.pin(disable_notification=True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

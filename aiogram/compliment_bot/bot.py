import configparser
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from tools.keyboards import start_reply
from tools.parser_site import get_compmliment

# start loffing data
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

# parsing config file with tokens
config = configparser.ConfigParser()
config.read('config.cfg')

bot = Bot(token=config["Telegram"]["token"], parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    # if username is empty name is first name
    name = msg.from_user.username if msg.from_user.username != "None" else msg.from_user.first_name
    
    await msg.answer(f'❤Hello, <b>{name}</b>', reply_markup=start_reply)


@dp.message_handler(Text(equals="😍Compliment"))
async def compliment(msg: types.Message):
    await msg.answer(f'😘 {get_compmliment()}')


if __name__ == "__main__":
    executor.start_polling(dp)
import configparser
import logging

from aiogram import Bot, Dispatcher, executor, types

from database.sqlite_db import Database


logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

# parse config
config = configparser.ConfigParser()
config.read('bot.cfg')

# create client bot
bot = Bot(token=config["Telegram"]["TOKEN"])
dp = Dispatcher(bot)

# start db
db = Database("db_sql.db")


@dp.message_handler()
async def add_message(msg: types.Message):
    user_id = int(msg.from_user.id)
    
    db.create_profile(user_id)
    
    print(db.mute(user_id))
    # check on mute
    if not db.mute(user_id):
        # limit length message
        if len(msg.text) <= int(config["limited"]["length_message"]):
            user_text = msg.text.splitlines()
            # check on template
            try:
                if user_text[1].split("@")[0] == "Связь📝: " and user_text[2] == "Гарант🔐: @unlegal_way_garant":
                    pass
                else:
                    raise IndexError
            except IndexError:
                await msg.reply(f"Отправьте в формате:\n"
                                f"`*Услуга*\n"
                                f"Связь📝: @{msg.from_user.username}\n"
                                f"Гарант🔐: @unlegal_way_garant`",
                                parse_mode="MARKDOWN")
            finally:
                db.set_mute(user_id, int(config["limited"]["hold_message"]))
                db.add_message(user_id, int(config["limited"]["message_in_day"]))
        else:
            await msg.delete()
    else:
        await msg.delete()
    

if __name__ == "__main__":
    executor.start_polling(dp)
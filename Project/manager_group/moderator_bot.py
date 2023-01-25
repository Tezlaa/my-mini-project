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
    
    # check on mute
    if not db.mute(user_id):
        # limit length message
        if len(msg.text) <= int(config["limited"]["length_message"]):
            user_text = msg.text
            # check on template
            try:
                if user_text.find("@unlegal_way_garant") != -1:
                    pass
                else:
                    raise IndexError
            except IndexError:
                if int(config["limited"]["message_in_day"]) == (db.get_count_message(user_id) + 1):
                    await msg.delete()
                    await msg.answer(f'⚠ ***@{msg.from_user.username}, '
                                     f'Превышено количество сообщений***\n_Попробуйте через 24 часа_',
                                     parse_mode="MarkdownV2")
                else:
                    await msg.delete()
                    await msg.answer(f'@{msg.from_user.username}, ***Ваше сообщение было удалено, '
                                     f'потому что Вы не указали гаранта чата*** \n`@unlegal_way_garant`\n\n'
                                     f'_⏳До сегоднешнего лимита заявок:_ '
                                     f'***{db.get_count_message(user_id) + 1}'
                                     f'/{int(config["limited"]["message_in_day"])}***\n'
                                     f'_Попробуйте через_ ***{int(config["limited"]["hold_message"]) // 60} минут***',
                                     parse_mode="MarkdownV2")
            finally:
                db.set_mute(user_id, int(config["limited"]["hold_message"]))
                db.add_message(user_id, int(config["limited"]["message_in_day"]))
        else:
            await msg.delete()
            await msg.answer(f'_⚠ @{msg.from_user.username}, '
                             f'длина превышает {config["limited"]["length_message"]} символов_',
                             parse_mode="MarkdownV2")
    else:
        await msg.delete()
    

if __name__ == "__main__":
    executor.start_polling(dp)
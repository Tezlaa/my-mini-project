import logging
import sqlite3
import time


class Database:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.base = sqlite3.connect(db_name)
        self.cur = self.base.cursor()
        
        if self.base:
            logging.info('Data base connected!')
        else:
            logging.info(self.base)
    
        stmt = """CREATE TABLE IF NOT EXISTS profile(
            user_id INTEGER,
            count_message INTEGER,
            mute_time INTEGER
            )"""
            
        self.base.execute(stmt)
        self.base.commit()
        return
        
    def create_profile(self, user_id: int) -> None:
        user = self.cur.execute(f'SELECT 1 FROM profile WHERE user_id == {user_id}').fetchone()
        if not user:
            self.cur.execute("INSERT INTO profile VALUES(?, ?, ?)", (user_id, 0, 0))
        self.base.commit()
        return
    
    def get_count_message(self, user_id: int) -> int:
        message = int(
            self.cur.execute(f'SELECT count_message FROM profile WHERE user_id = {user_id}').fetchone()[0])
        return message
    
    def add_message(self, user_id: int, limit: int) -> None:
        how_much_msg = str(self.get_count_message(user_id) + 1)
        self.cur.execute(f'UPDATE profile SET count_message = {how_much_msg} WHERE user_id = "{user_id}"')
        self.base.commit()
        
        if int(how_much_msg) >= limit:
            self.set_mute(user_id, 86400)
            self.cur.execute(f'UPDATE profile SET count_message = {0} WHERE user_id = "{user_id}"')
            self.base.commit()
        return
    
    def mute(self, user_id: int) -> bool:
        mute_time = self.cur.execute(f'SELECT mute_time FROM profile WHERE user_id = "{user_id}"').fetchone()[0]
        return int(mute_time) >= int(time.time())
    
    def set_mute(self, user_id: int, mute_time: int):
        self.cur.execute(f'UPDATE profile SET mute_time={int(time.time())+(mute_time)} WHERE user_id = "{user_id}"')
        self.base.commit()
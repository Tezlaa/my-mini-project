import logging
import sqlite3


class Database():
    def __init__(self, namebase: str) -> None:
        """
        Args:
            namebase (str): name for database
                ex: "personal"
        """
        self.namebase = namebase
        self.db = sqlite3.connect(f'{self.namebase}.db')
        self.cur = self.db.cursor()
        
        # error-checked
        if self.db:
            logging.info("Data base connected!")
        else:
            logging.info(self.db)


class UserTabel(Database):
    def __init__(self, namebase, name_tabel: str):
        super().__init__(namebase=namebase)
        
        self.name_tabel = name_tabel
        
        tabel = f"""CREATE TABLE IF NOT EXISTS {self.name_tabel}(
            user_id INTEGER PRIVATE KEY,
            user_name TEXT)
        """
        self.cur.execute(tabel)
        self.db.commit()

    def create_user(self, user_id: int, user_name: str):
        user = self.cur.execute(f'SELECT 1 FROM {self.name_tabel} WHERE user_id = {user_id}').fetchone()
        if not user:
            self.cur.execute(f"INSERT INTO {self.name_tabel} VALUES(?, ?)", (user_id, user_name))
        self.db.commit()
    
    def get_username(self, user_id: int) -> str:
        username = self.cur.execute(f'SELECT user_name FROM {self.name_tabel} WHERE user_id = "{user_id}"')\
            .fetchone()[0]
        return str(username)

    def get_user_id(self, user_name: str) -> int:
        user_id = self.cur.execute(f'SELECT user_id FROM {self.name_tabel} WHERE user_name = "{user_name}"')\
            .fetchone()[0]
        return int(user_id)
        
        
if __name__ == "__main__":
    pass
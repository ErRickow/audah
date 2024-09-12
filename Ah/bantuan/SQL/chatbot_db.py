from sqlalchemy import Boolean, Column, String, UnicodeText

from Ah.bantuan.SQL import BASE, SESSION

class Chatbot:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS chatbots (
                chat_id INTEGER PRIMARY KEY,
                user_id INTEGER
            )
        ''')
        self.connection.commit()

    async def add_chatbot(self, chat_id, user_id):
        self.cursor.execute('''
            INSERT INTO chatbots (chat_id, user_id)
            VALUES (?, ?)
            ON CONFLICT(chat_id) DO UPDATE SET
                user_id=excluded.user_id
        ''', (chat_id, user_id))
        self.connection.commit()
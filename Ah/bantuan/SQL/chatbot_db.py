from sqlalchemy import Boolean, Column, String, UnicodeText

from Ah.bantuan.SQL import BASE, SESSION

from sqlalchemy.orm import sessionmaker
from models import Chatbot, db_connect, create_table

class Chatbot(BASE):
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    async def add_chatbot(self, chat_id, user_id):
        chatbot = Chatbot(chat_id=chat_id, user_id=user_id)
        self.session.merge(chatbot)
        self.session.commit()
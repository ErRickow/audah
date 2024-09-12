from sqlalchemy import Boolean, Column, String, UnicodeText

from Ah.bantuan.SQL import BASE, SESSION

from sqlalchemy.orm import sessionmaker
from models import Chatbot, db_connect, create_table

class Chatbot(BASE):
    __tablename__ = "chatbot"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)  #

    async def add_chatbot(self, chat_id, user_id):
        chatbot = Chatbot(chat_id=chat_id, user_id=user_id)
        self.session.merge(chatbot)
        self.session.commit()
from sqlalchemy import Column, String
from Ah.bantuan.SQL import BASE, SESSION

class Chatbot(BASE):
    __tablename__ = "chatbot"
    chat_id = Column(String(14), primary_key=True)
    user_id = Column(String(20))

    def __init__(self, chat_id, user_id):
        self.chat_id = str(chat_id)
        self.user_id = str(user_id)

class ChatbotManager:
    async def clear_chatbot_history(self, user_id):
        unset_clear = {"chatbot_chat": None}
        query = SESSION.query(Chatbot).filter(Chatbot.user_id == user_id).update(unset_clear)
        SESSION.commit()
        
        if query > 0:
            return "Chat history cleared successfully."
        else:
            return "No chat history found to clear."

    async def add_chatbot(self, chat_id, user_id):
        chatbot = Chatbot(chat_id=chat_id, user_id=user_id)
        SESSION.merge(chatbot)
        SESSION.commit()
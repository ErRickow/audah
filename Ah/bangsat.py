import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from Ah.bantuan.tools import *
from config import PREFIX as cmd
from Ah import *


def send_simtalk(message: str) -> str:
    if len(message) > 1000:
        return "Character terlalu panjang."
    else:
        params = {"text": message, "lc": "id"}
        try:
            response = requests.post(
                "https://api.simsimi.vn/v1/simtalk",
                data=params
            ).json()
            return response.get("message", "Maaf, tidak bisa merespons sekarang.")
        except Exception as e:
            return f"Error: {str(e)}"


@Client.on_message(filters.me & filters.command("kmtl", cmd))
async def manage_chatbot_status(client: Client, message: Message):
    global chatbot_active
    arg = get_text(message).lower()

    if arg == "off":
        chatbot_active = False
        await message.reply("Chatbot dinonaktifkan.")
    elif arg == "on":
        chatbot_active = True
        await message.reply("Chatbot diaktifkan.")
        
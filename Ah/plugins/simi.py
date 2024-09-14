import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from Ah.bantuan.tools import *

from Ah import *


def send_simtalk(message):
    if len(message) > 1000:
        return "character too big"
    else:
        params = {"text": message, "lc": "id"}
        response = requests.post(
            "https://api.simsimi.vn/v1/simtalk",
            data=params
        ).json()
        return response.get("message")

@Client.on_message(filters.command("simi", cmd))
async def gtp(client, message: Message):
    text = get_text(message)
    if not text:
        return await message.reply("Kasih teks GOLBOK!!")
    pros = await message.reply("Sabar njing ..")
    simtak = send_simtalk(message)
    return await pros.edit(simtak)
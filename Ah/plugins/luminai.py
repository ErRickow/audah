from pyrogram import Client, filters, enums
from pyrogram.types import Message
import requests
from Ah.bantuan.tools import *

from .help import add_command_help
from Ah import *

import requests

async def tanya(text):
    url = "https://luminai.my.id/"
    data = {"content": text}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        data = response.json()
        return data["result"]
    else:
        return f"{response.text}"

@Client.on_message(filters.command("asg", cmd))
async def _(client, message):
    text = get_text(message)
    if not text:
        return await message.reply("Kasih teks GOLBOK!!")
    
    hasil = await tanya(text)
    return await message.reply(hasil)
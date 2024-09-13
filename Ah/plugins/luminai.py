from  pyrogram import *
from pyrogram import Client, filters
from pyrogram.types import *
import requests

async def luminer(messagestr):
    url = "https://lumin-ai.xyz/"
    response = requests.post(url, json={"content": content})
    if response.status_code != 200:
        return None
    return response.json()
    
@Client.on_message(filters.me & filters.command("uy", cmd))
async def saya(client: Client, message: Message)
    if len(message.command) > 1:
        prompt = message.text.split(maxsplit=1)[1]
    elif message.reply_to_message:
        prompt = message.reply_to_message.text
    else:
        return await message.reply_text("Give ask from CHATGPT-3")
    try:
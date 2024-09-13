from pyrogram import Client, filters
from pyrogram.types import Message
import requests

from Ah import *
from Ah.bantuan.tools import *

async def luminer(content):
    url = "https://lumin-ai.xyz/"
    response = requests.post(url, json={"content": content})
    if response.status_code != 200:
        return None
    return response.json()

@Client.on_message(filters.me & filters.command("uy"))
async def saya(client: Client, message: Message):
    if len(message.command) > 1:
        prompt = message.text.split(maxsplit=1)[1]
    elif message.reply_to_message:
        prompt = message.reply_to_message.text
    else:
        return await message.reply_text("Give ask from LUMINAI")
    
    # Memanggil fungsi luminer dan menunggu hasilnya
    result = await luminer(prompt)
    
    if result is None:
        await message.reply_text("Failed to get a response from LUMINAI.")
    else:
        await message.reply_text(f"Response: {result}")

# Pastikan Anda menambahkan kode untuk menjalankan client
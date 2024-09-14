import aiohttp
from pyrogram import Client, filters
from pyrogram.types import Message
from Ah.bantuan.tools import *

from .help import add_command_help
from Ah import *

async def tanya(text):
    url = "https://widipe.com/gptgo"
    params = {'text': text}
    headers = {'accept': 'application/json'}
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as response:
            if response.status == 200:
                data = await response.json()
                if 'result' in data:
                    return data['result']
                else:
                    return "Tidak ada hasil yang ditemukan."
            else:
                return f"Error goblok: {response.status} - {await response.text()}"

@Client.on_message(filters.command("gtp"))
async def gtp(client, message: Message):
    text = get_text(message)
    if not text:
        return await message.reply("Kasih teks GOLBOK!!")
    
    hasil = await tanya(text)
    return await message.reply(hasil)
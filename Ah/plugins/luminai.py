from pyrogram import Client, filters
from pyrogram.types import Message
from Ah.bantuan.tools import *

from Ah import *
import requests

async def fetch_content(content):
    url = 'https://lumin-ai.xyz/'
    response = requests.post(url, json={'content': content})
    
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data
    else:
        print(f'Error: {response.status_code}')
        return None

@Client.on_message(filters.me & filters.command("luminai", cmd))
async def saya(client: Client, message: Message):
    if len(message.command) > 1:
        prompt = message.text.split(maxsplit=1)[1]
    else:
        return await message.reply_text("Provide a prompt for LUMINAI")

    result = await fetch_content(prompt)

    if result is None:
        await message.reply_text("Failed to get a response from LUMINAI.")
    else:
        for response in result['responses']:
            await message.reply_text(response)
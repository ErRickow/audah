from pyrogram import Client, filters
from pyrogram.types import Message
from Ah.bantuan.tools import *

import requests

async def fetch_content(content):
    url = 'https://lumin-ai.xyz/'
    response = requests.post(url, json={'content': content})
    
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None

@Client.on_message(filters.me & filters.command("luminai"))
async def saya(client: Client, message: Message):
    await message.reply_text("Provide a prompt for LUMINAI")

    result = await fetch_content(prompt)

    if result is None:
        await message.reply_text("Failed to get a response from LUMINAI.")
    else:
        await message.reply_text(f"Response: {result}")
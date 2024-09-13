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
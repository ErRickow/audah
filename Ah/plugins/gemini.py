import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from Ah import *

@Client.on_message(filters.command("ask", prefix) & filters.me)
async def handle_message(client, message):
    # Mengambil teks dari pesan
    text = message.text
    
    # Memanggil API dan mendapatkan respons
    url = f"https://api.botcahx.eu.org/api/search/blackbox-chat?text={text}&apikey=LwulPck3"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            if data is None or "result" not in data:
                await message.reply("Terjadi kesalahan dalam mendapatkan hasil.")
                return
            
            result = data["result"]
            
            if len(result) > 0:
                await message.reply(result)
            else:
                await message.reply("Hasil kosong.")
        else:
            await message.reply(f"Kesalahan saat mengakses API: {response.status_code}")

    except Exception as e:
        await message.reply(f"Terjadi kesalahan: {e}")
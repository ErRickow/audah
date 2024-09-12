import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from Ah import *
from config import PREFIX as cmd

# Ganti dengan API key Anda
  

async def ai_hadeh(c, text):
  gwa = f"<a href=tg://user?id={c.me.id}>{c.ne.first_name}{c.me.last_name or ''}</a>"
    try:
        params = {
            'message': message,
            'apikey': 'LwulPck3'
        }
        
        response = requests.post('https://api.botcahx.eu.org/api/search/openai-custom', json=params)
        response.raise_for_status()  # Memicu exception jika status kode bukan 2xx
        return response.json()  # Mengembalikan data JSON dari respons

    except Exception as error:
        return str(error)  # Mengembalikan pesan kesalahan sebagai string

@Client.on_message(filters.command("ask", cmd))
def handle_message(client, message):
    # Ambil isi pesan dari pengguna setelah perintah
    user_message = " ".join(message.command[1:])  # Menggabungkan argumen menjadi satu string
    
    if not user_message:
        message.reply("Silakan berikan pertanyaan setelah perintah.")
        return
    
    # Dapatkan respons dari fungsi ai_btc
    ai_response = ai_btc(user_message)
    
    # Balas dengan respons dari AI
    message.reply(ai_response)
import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from Ah import *

def ai_btc(message):
    try:
        params = {
            'message': message,
            'apikey': ''  # Ganti dengan API key Anda
        }
        
        response = requests.post('https://api.botcahx.eu.org/api/search/openai-custom', json=params)
        response.raise_for_status()  # Memicu exception jika status kode bukan 2xx
        return response.json()  # Mengembalikan data JSON dari respons

    except Exception as error:
        return str(error)  # Mengembalikan pesan kesalahan sebagai string
@Client.on_message(filters.command("ask", prefix) & filters.me)
def handle_message(client, message):
    # Ambil isi pesan dari pengguna
    user_message = message.text
    
    # Dapatkan respons dari fungsi ai_btc
    ai_response = ai_btc(user_message)
    
    # Balas dengan respons dari AI
    message.reply(ai_response)
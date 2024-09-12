import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from Ah import *
from config import PREFIX as cmd

# Ganti dengan API key Anda
  

async def ai_hadeh(c, text):
  gwa = f"<a href=tg://user?id={c.me.id}>{c.ne.first_name}{c.me.last_name or ''} </a>"
  bahan = [
      {
          "role": "system"
          "content": f"Lo adalah asistant telekram dari pengguna akun {gwa}",
      },
      {
          "role": "assistant"
          "content": f"gunakan bahasa indonesia toxic, dan lo adalah assistant dari pengguna telekram {gw}",
      },
      {"role": "user", "content": f"{text}"},
  ]
  url = "https://api.botcahx.eu.org/api/search/openai-custom"
  payloaf = {"message":, bahan, "apikey": "LwulPck3"}
  res = await fetch.post(url, json=payloaf)
  if res.status_code == 200:
      data = res.json()
      return data["result"]
  else:
      return f"{res.text}"

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
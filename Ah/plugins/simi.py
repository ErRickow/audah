import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from Ah.bantuan.tools import *

from Ah import *

# Fungsi untuk mengirim permintaan ke API Simsimi
# Status chatbot (aktif/tidak aktif)
chatbot_active = True

# Fungsi untuk mengirim permintaan ke API Simsimi
def send_simtalk(message: str) -> str:
    if len(message) > 1000:
        return "Character terlalu panjang."
    else:
        params = {"text": message, "lc": "id"}
        try:
            response = requests.post(
                "https://api.simsimi.vn/v1/simtalk",
                data=params
            ).json()
            return response.get("message", "Maaf, tidak bisa merespons sekarang.")
        except Exception as e:
            return f"Error: {str(e)}"

# Handler untuk semua pesan teks
@Client.on_message(filters.text & ~filters.command)
async def chatbot_response(client, message: Message):
    global chatbot_active

    # Cek apakah chatbot aktif
    if not chatbot_active:
        return

    # Ambil teks dari pesan
    text = message.text

    if not text:
        return

    # Panggil fungsi untuk mendapatkan balasan dari Simsimi
    simtalk_response = send_simtalk(text)

    # Kirim balasan dari Simsimi
    await message.reply(simtalk_response)

# Handler untuk command "/chatbot on"
@Client.on_message(filters.command("idup", cmd) & filters.me)
async def chatbot_on(client, message: Message):
    global chatbot_active
    chatbot_active = True
    await message.reply("Chatbot diaktifkan.")

# Handler untuk command "/chatbot off"
@Client.on_message(filters.command("mati", cmd) & filters.me)
async def chatbot_off(client, message: Message):
    global chatbot_active
    chatbot_active = False
    await message.reply("Chatbot dinonaktifkan.")

import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from Ah.bantuan.tools import *
from config import PREFIX as cmd
from Ah import *

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

            # Pastikan response valid
            if response and "message" in response:
                return response["message"]
            else:
                return "Maaf, tidak bisa merespons sekarang."
        except Exception as e:
            return f"Error: {str(e)}"

# Handler untuk semua pesan teks dan mengatur status chatbot
@Client.on_message(filters.text & ~filters.bot & filters.me)
async def chatbot_response(client: Client, message: Message):
    global chatbot_active
    text = message.text.lower()

    # Cek apakah pesan merupakan perintah untuk mengaktifkan atau menonaktifkan chatbot
    if text.startswith(tuple(cmd)):
        command = text[len(cmd[0]):].strip()  # Menghapus prefix dari teks
        if command == "koff":
            chatbot_active = False
            await message.reply("Chatbot dinonaktifkan.")
            return
        elif command == "on":
            chatbot_active = True
            await message.reply("Chatbot diaktifkan.")
            return

    # Jika chatbot sedang nonaktif, abaikan pesan lainnya
    if not chatbot_active:
        return

    # Panggil fungsi untuk mendapatkan balasan dari Simsimi
    simtalk_response = send_simtalk(message.text)

    # Kirim balasan ke chat
    await message.reply(simtalk_response)

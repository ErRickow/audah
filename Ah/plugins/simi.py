import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from Ah.bantuan.tools import *

from Ah import *

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

            # Ambil pesan dari respons API Simsimi
            return response.get("message", "Maaf, tidak bisa merespons sekarang.")
        except Exception as e:
            return f"Error: {str(e)}"

# Handler untuk command "/simi"
@Client.on_message(filters.command("simi", cmd) & filters.me)
async def gtp(client, message: Message):
    # Ambil teks dari pesan
    text = get_text(message)

    if not text:
        return await message.reply("Kasih teks GOBLOK!!")
    
    # Beri respon sementara saat proses berlangsung
    pros = await message.reply("Sabar njing ..")

    # Panggil fungsi untuk mendapatkan balasan dari Simsimi
    simtalk_response = send_simtalk(text)

    # Edit pesan sebelumnya dengan balasan dari Simsimi
    return await pros.edit(simtalk_response)

import requests
import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from Ah.bantuan.tools import get_text
from config import PREFIX as cmd
from Ah import *
from Ah.bantuan.PyroHelpers import ReplyCheck
from config import *

# Status chatbot (aktif/non-aktif)
chatbot_active = True

# Konfigurasi logging
HNDLR = [""]

# Fungsi untuk mengirim permintaan ke API Simsimi
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logger = logging.getLogger(__name__)

# Fungsi untuk mengirim permintaan ke API Simsimi # Jangan lupa impor requests

# Fungsi untuk mengirim pesan ke Simsimi
async def send_simtalk(message: str) -> str:
    if len(message) > 1000:
        logger.warning("Pesan terlalu panjang untuk diproses.")
        return "Character terlalu panjang."
    else:
        params = {"text": message, "lc": "id"}
        try:
            # Gunakan await untuk menangani operasi asinkron
            response = await asyncio.to_thread(requests.post, 
                                               "https://api.simsimi.vn/v1/simtalk",
                                               data=params)
            result = response.json()
            logger.info("Berhasil mendapatkan respons dari Simsimi.")
            return result.get("message", "Maaf, tidak bisa merespons sekarang.")
        except Exception as e:
            logger.error(f"Error saat mengirim permintaan ke Simsimi API: {str(e)}")
            return f"Error: {str(e)}"

# Handler untuk semua pesan teks
@Client.on_message(filters.me)
async def chatbot_response(client, message: Message):
    global chatbot_active

    # Cek apakah chatbot sedang aktif
    if not chatbot_active:
        logger.info("Chatbot sedang dinonaktifkan, tidak merespons pesan.")
        return


    text = message.text
    if f"{HNDLR}cmd" in text:
        logger.warning("Pesan kosong diterima, tidak ada yang bisa diproses.")
        return

    # Mendapatkan respons dari Simsimi
    logger.info(f"Mengirim pesan ke Simsimi: {text}")
    simtalk_response = await send_simtalk(text)

    # Mengirimkan respons kembali ke pengguna
    await message.reply(simtalk_response)
    logger.info(f"Respons dari Simsimi: {simtalk_response}")


# Handler untuk mengatur status chatbot (on/off)
@Client.on_message(filters.command("yu", cmd) & filters.me)
async def manage_chatbot_status(client, message: Message):
    global chatbot_active
    arg = get_text(message)

    # Cek jika arg None atau bukan string
    if not isinstance(arg, str) or not arg:
        await message.reply("Format perintah tidak valid. Gunakan chatbot on atau chatbot off.")
        logger.warning("Argumen tidak valid atau None diterima.")
        return

    arg = arg.lower()

    if arg == "off":
        chatbot_active = False
        await message.reply("Chatbot dinonaktifkan.")
        logger.info("Chatbot telah dinonaktifkan oleh pengguna.")
    elif arg == "on":
        chatbot_active = True
        await message.reply("Chatbot diaktifkan.")
        logger.info("Chatbot telah diaktifkan oleh pengguna.")
    else:
        await message.reply("Gunakan perintah: chatbot on atau chatbot off.")
        logger.warning(f"Perintah tidak valid: {arg}")

# Helpers with Randy devs a.k.a xtedev
# ang ang ang ang
# ©Er a.k.a @Chakszzz
import requests
import logging
from pyrogram import *
from pyrogram.types import Message
from Ah.bantuan.tools import get_text
from Ah import *
from Ah.bantuan.PyroHelpers import ReplyCheck
from config import *
import re
import asyncio
import os
import sys
import shutil
import subprocess

from git import Repo
from git.exc import InvalidGitRepositoryError

# Status chatbot (aktif/non-aktif)
chatbot_active = False

# Konfigurasi logging
HNDLR = ["yu off", "xupdate"]

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logger = logging.getLogger(__name__)

# Fungsi untuk mengirim pesan ke Simsimi
async def send_simtalk(message: str) -> str:
    if len(message) > 1000:
        logger.warning("Pesan terlalu panjang untuk diproses.")
        return "Character terlalu panjang."
    else:
        params = {"text": message, "lc": "id"}  # Language code harus string, pastikan 'lc' diisi dengan benar
        try:
            loop = asyncio.get_event_loop()
            # Menggunakan run_in_executor sebagai pengganti to_thread
            response = await loop.run_in_executor(None, requests.post, "https://api.simsimi.vn/v2/simtalk", None, params)
            
            if response.status_code != 200:
                logger.error(f"Error dari Simsimi API: {response.status_code}")
                return f"Error dari API: {response.status_code}"

            result = response.json()

            # Cek apakah ada field message di dalam respons JSON
            if "message" in result:
                logger.info("Berhasil mendapatkan respons dari Simsimi.")
                return result.get("message", "Maaf, tidak bisa merespons sekarang.")
            else:
                logger.error(f"Tidak ada field 'message' di dalam respons Simsimi: {result}")
                return "Error: Response tidak valid dari Simsimi API."

        except Exception as e:
            logger.error(f"Error saat mengirim permintaan ke Simsimi API: {str(e)}")
            return f"Error: {str(e)}"

# Handler untuk semua pesan teks
@Client.on_message(filters.text & ~filters.bot & filters.me)
async def chatbot_response(client, message):
    global chatbot_active

    text = message.text

    # Periksa perintah "cukup" atau "diem" untuk mematikan chatbot
    if "cukup" in text or "diem" in text:
        chatbot_active = False
        logger.info("Chatbot telah dinonaktifkan.")
        await message.reply("dih")
        return

    # Periksa perintah "kemana lu" atau "woi" untuk mengaktifkan chatbot
    if "kemana lu" in text or "woi" in text:
        chatbot_active = True
        logger.info("Chatbot telah diaktifkan.")
        await message.reply("hah?")
        return

    # Periksa perintah "update" untuk melakukan update userbot
    if "update" in text:
        logger.info("Memulai proses update userbot.")
        try:
            pros = await message.reply(
                f"<i>Memeriksa pembaruan resources {ubot.me.mention}...</i>"
            )
            out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
            last_commit = subprocess.check_output(
                ["git", "log", "-1", "--pretty=format:%h %s"]
            ).decode("UTF-8").strip()

            teks = f"<b>❒ Status resources: {ubot.me.mention}</b>\n"
            memeg = f"<b>🎲 Perubahan logs by {client.me.mention}</b>"

            if "🧩 Already up to date." in str(out):
                return await pros.edit(
                    f"<blockquote>{teks}┖ {out}\n<b>Last Commit:</b> {last_commit}</blockquote>"
                )

            if len(out) > 4096:
                await pros.edit("<i>Hasil akan dikirimkan dalam bentuk file...</i>")
                with open("output.txt", "w+") as file:
                    file.write(out)
                await client.send_document(
                    message.chat.id,
                    "output.txt",
                    caption="<b>Perubahan logs:</b>",
                    reply_to_message_id=message.id,
                )
                os.remove("output.txt")
                return

            format_line = [f"┣ {line}" for line in out.splitlines()]
            if format_line:
                format_line[-1] = f"┖ {format_line[-1][2:]}"
                format_output = "\n".join(format_line)

            await pros.edit(
                f"<blockquote><b>{memeg}</b>\n\n{teks}{format_output}<br>\n\n<b>Last Commit:</b> {last_commit}</blockquote>"
            )
            os.execl(sys.executable, sys.executable, "-m", "Ah")

        except Exception as e:
            await message.reply(f"Terjadi kesalahan saat memperbarui: {e}")
            logger.error(f"Error saat memperbarui userbot: {e}")

        return

    # Cek apakah chatbot sedang aktif sebelum merespons pesan lainnya
    if not chatbot_active:
        logger.info("Chatbot sedang dinonaktifkan, tidak merespons pesan.")
        return

    # Mendapatkan respons dari Simsimi
    simtalk_response = await send_simtalk(text)

    # Mengirimkan respons kembali ke pengguna
    bang = "CibeeKu"
    username = "CibeeKu"  # Ganti dengan username yang valid
    try:
        user = await client.get_users(username)  # Mendapatkan informasi pengguna berdasarkan username
        user_id = user.id
        await message.reply(f"<blockquote>❏ APA INI BANGSAT\n├• {client.me.mention}\n└• {simtalk_response}</blockquote>")
    except Exception as e:
        await message.reply("Terjadi kesalahan saat mendapatkan informasi pengguna.")
        logger.error(f"Error saat mendapatkan informasi pengguna: {e}")

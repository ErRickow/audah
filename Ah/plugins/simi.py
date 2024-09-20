import requests
import logging
from pyrogram import Client, filters
from Ah.bantuan.tools import get_text
from Ah.bantuan.PyroHelpers import ReplyCheck
from Ah import ubot
import re
import asyncio
import os
import sys
import shutil
import subprocess
from git import Repo
from git.exc import InvalidGitRepositoryError
from config import emo

cmd_handler = ""
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
async def send_simtalk(message):
    if len(message) > 1000:
        return "Character too big."
    else:
        params = {"text": message, "lc": "id"}  # Bahasa Indonesia
        try:
            response = requests.post(
                "https://api.simsimi.vn/v2/simtalk",
                data=params,
                timeout=5  # Batas waktu agar tidak menggantung
            )
            # Pastikan status code 200 sebelum mengakses respons
            if response.status_code == 200:
                result = response.json()
                return result.get("message", "Maaf, tidak ada respons dari Simsimi.")
            else:
                return f"Error dari API Simsimi: {response.status_code}"
        except requests.exceptions.Timeout:
            return "Error: Timeout saat menghubungi API Simsimi."
        except Exception as e:
            return f"Error saat menghubungi API Simsimi: {str(e)}"

# Handler untuk semua pesan teks dan command
@Client.on_message(filters.text & filters.command(["er on", "diem", "woi", "cukup", "pull"], cmd_handler) & ~filters.bot & filters.me)
async def chatbot_response(client, message):
    global chatbot_active

    text = message.text

    # Periksa perintah "cukup" atau "diem" untuk mematikan chatbot
    if "cukup" in text or "diem" in text:
        chatbot_active = False
        logger.info("Chatbot telah dinonaktifkan.")
        await message.reply("Chatbot dimatikan.")
        return

    # Periksa perintah "er on" atau "woi" untuk mengaktifkan chatbot
    if "er on" in text or "woi" in text:
        chatbot_active = True
        logger.info("Chatbot telah diaktifkan.")
        await message.reply("Chatbot dihidupkan.")
        return

    # Periksa perintah "pull" untuk melakukan update userbot
    if "pull" in text:
        logger.info("Memulai proses update userbot.")
        try:
            pros = await message.reply(
                f"<i>{emo.proses} Memeriksa pembaruan resources {client.me.mention}...</i>"
            )
            out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
            last_commit = subprocess.check_output(
                ["git", "log", "-1", "--pretty=format:%h %s"]
            ).decode("UTF-8").strip()

            teks = f"<b>❒ Status resources: {ubot.me.mention}</b>\n"
            memeg = f"<b>🎲 Perubahan logs by {client.me.mention}</b>"

            if "Already up to date." in str(out):
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

    # Mendapatkan respons dari Simsimi secara asinkron
    simtalk_response = await send_simtalk(text)

    # Mengirimkan respons kembali ke pengguna
    try:
        await message.reply(
            f"<blockquote>❏ <b>INI APA BANGSAT</b>\n├• {client.me.mention}\n└• {simtalk_response}</blockquote>"
        )
    except Exception as e:
        await message.reply("Terjadi kesalahan saat mengirim respons.")
        logger.error(f"Error saat mengirim respons: {e}")

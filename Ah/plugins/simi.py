import requests
import logging
from pyrogram import Client, filters
from Ah.bantuan.tools import get_text
from Ah.bantuan.PyroHelpers import ReplyCheck
from Ah import ubot
import subprocess
import os
import sys

cmd_handler = ""
chatbot_active = False

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logger = logging.getLogger(__name__)

async def send_simtalk(message):
    if len(message) > 1000:
        return "Character too big."
    params = {"text": message, "lc": "id"}
    try:
        response = requests.post(
            "https://api.simsimi.vn/v2/simtalk",
            data=params,
            timeout=5
        ).json()
        if response.status_code == 200:
            return response.get("message", "Maaf, tidak ada respons dari Simsimi.")
        else:
            return f"Error dari API Simsimi: {response.status_code}"
    except requests.exceptions.Timeout:
        return "Error: Timeout saat menghubungi API Simsimi."
    except Exception as e:
        return f"Error saat menghubungi API Simsimi: {str(e)}"

@Client.on_message(filters.command(["er on", "diem", "woi", "cukup", "pull"], cmd_handler) & ~filters.bot & filters.me)
async def command_handler(client, message):
    global chatbot_active
    text = message.text

    # Periksa perintah untuk mengaktifkan atau menonaktifkan chatbot
    if "cukup" in text or "diem" in text:
        chatbot_active = False
        logger.info("Chatbot telah dinonaktifkan.")
        await message.reply("Chatbot dimatikan.")
        return

    if "er on" in text or "woi" in text:
        chatbot_active = True
        logger.info("Chatbot telah diaktifkan.")
        await message.reply("Chatbot dihidupkan.")
        return

    # Periksa perintah "pull" untuk melakukan update userbot
    if "pull" in text:
        logger.info("Memulai proses update userbot.")
        try:
            pros = await message.reply(f"<i>Memeriksa pembaruan resources {client.me.mention}...</i>")
            out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
            last_commit = subprocess.check_output(
                ["git", "log", "-1", "--pretty=format:%h %s"]
            ).decode("UTF-8").strip()

            teks = f"<b>❒ Status resources: {ubot.me.mention}</b>\n"
            memeg = f"<b>🎲 Perubahan logs by {client.me.mention}</b>"

            if "Already up to date." in str(out):
                return await pros.edit(f"<blockquote>{teks}┖ {out}\n<b>Last Commit:</b> {last_commit}</blockquote>")

            if len(out) > 4096:
                await pros.edit("<i>Hasil akan dikirimkan dalam bentuk file...</i>")
                with open("output.txt", "w+") as file:
                    file.write(out)
                await client.send_document(message.chat.id, "output.txt", caption="<b>Perubahan logs:</b>", reply_to_message_id=message.id)
                os.remove("output.txt")
                return

            format_line = [f"┣ {line}" for line in out.splitlines()]
            if format_line:
                format_line[-1] = f"┖ {format_line[-1][2:]}"
                format_output = "\n".join(format_line)

            await pros.edit(f"<blockquote><b>{memeg}</b>\n\n{teks}{format_output}<br>\n\n<b>Last Commit:</b> {last_commit}</blockquote>")
            os.execl(sys.executable, sys.executable, "-m", "Ah")

        except Exception as e:
            await message.reply(f"Terjadi kesalahan saat memperbarui: {e}")
            logger.error(f"Error saat memperbarui userbot: {e}")

@Client.on_message(filters.text & ~filters.bot & filters.me)
async def chatbot_response(client, message):
    global chatbot_active

    text = message.text
    logger.info(f"Received message: {text}")

    # Cek apakah chatbot aktif sebelum merespons
    if chatbot_active:
        simtalk_response = await send_simtalk(text)
        await message.reply(
            f"<blockquote>❏ <b>INI APA BANGSAT</b>\n├• {client.me.mention}\n└• {simtalk_response}</blockquote>"
        )

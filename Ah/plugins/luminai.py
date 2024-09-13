from pyrogram import Client, filters, enums
from pyrogram.types import Message
import requests
from Ah.bantuan.tools import *

from .help import add_command_help
from Ah import *

async def tanya(text):
    url = "https://lumin-ai.xyz/"
    data = {"content": text}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        data = response.json()
        return data["result"]
    else:
        return f"{response.text}"
 #   else:
 #       return f"{response.text}"

@Client.on_message(filters.me & filters.command("asg", cmd))
async def saya(client: Client, message: Message):
    if len(message.command) > 1:
        prompt = message.text.split(maxsplit=1)[1]
    elif message.reply_to_message:
        prompt = message.reply.text
    else:
        return await message.reply_text("Beri pertanyaan ANJG")
    
    # Memanggil fungsi luminer dan menunggu hasilnya
    result = await tanya(prompt)
    
    if result is None:
        await message.reply_text("API DED.")
    else:
        await message.reply_text(f"<blockquote>{result}</blockquote>")

# Pastikan Anda menambahkan kode untuk menjalankan clien
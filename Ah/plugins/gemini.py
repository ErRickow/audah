import requests
from pyrogram import Client, filters
from pyrogram.types import Message

from Ah import *

async def chatgptold(messagestr):
    url = "https://api.botcahx.eu.org/api/search/blackbox-chat"
    payload = {
        "text": messagestr,
        "apikey": "LwulPck3"
    }
    response = requests.get(url, params=payload)
    if response.status_code != 200:
        return None
    return response.json()

@Client.on_message(filters.command("ask", prefix) & filters.me)
async def chatgpt_old_(client: Client, message: Message):
    if len(message.command) > 1:
        prompt = message.text.split(maxsplit=1)[1]
    elif message.reply_to_message:
        prompt = message.reply_to_message.text
    else:
        return await message.reply_text("Give ask from CHATGPT-3")
    
    try:
        messager = await chatgptold(prompt)
        if messager is None:
            return await message.reply_text("No response")
        
        # Asumsikan struktur respons dari API baru ini sesuai dengan yang Anda butuhkan
        output = messager.get("result")  # Ganti "result" dengan kunci yang sesuai dari API baru

        if len(output) > 4096:
            with open("chat.txt", "w+", encoding="utf8") as out_file:
                out_file.write(output)
            await message.reply_document(
                document="chat.txt",
                disable_notification=True
            )
            os.remove("chat.txt")
        else:
            await message.reply_text(output)
    except Exception as e:
        # Kirim pesan kesalahan ke pengguna
        await message.reply_text(f"Terjadi kesalahan: {str(e)}")
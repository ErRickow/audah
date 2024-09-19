import requests
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, Message
import io
from Ah import *
from .help import add_command_help

async def ambil_gambar(message):
    url = f"https://api.waifu.pics/nsfw/neko"
    headers = {'accept': 'image/jpeg'}
  
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        file_path = 'bokep.jpg'
        with open(file_path, 'wb') as f:
            f.write(response.content)

        await message.reply_photo(photo=file_path, caption=f"Gambar dari API {text}")
        
        os.remove(file_path)
    else:
        await message.reply("Gagal mengunduh gambar.")

await ambil_gambar(message, text="malaysia")
@Client.on_message(filters.command("ppcp", cmd) & filters.me)
async def handle_ppcp(client: Client, message: Message):
    await ambil_ppcp(message)  # Panggil dengan objek message yang benar
add_command_help(
    "couple",
    [
        ["ppcp", "Cari foto profil untuk couple."]
    ],
)
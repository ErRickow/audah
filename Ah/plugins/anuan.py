import requests
import os  # Tambahkan import os untuk menghapus file
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, Message
from Ah import *
from .help import add_command_help

async def ambil_gambar(message):
    url = f"https://api.waifu.pics/nsfw/neko"
    headers = {'accept': 'image/jpeg'}
  
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        file_path = 'neko_image.jpg'  # Nama file yang lebih umum
        with open(file_path, 'wb') as f:
            f.write(response.content)
        await message.reply_photo(photo=file_path, caption="Berikut gambar dari API.")
        
        os.remove(file_path)  # Hapus file setelah mengirim gambar
    else:
        await message.reply("Gagal mengunduh gambar.")

@Client.on_message(filters.command("wibu", cmd) & filters.me)
async def handle_wibu(client: Client, message: Message):
    await ambil_gambar(message)  # Panggil dengan objek message yang benar

add_command_help(
    "NSFW",
    [
        ["wibu", "Cari foto profil untuk couple."]
    ],
)

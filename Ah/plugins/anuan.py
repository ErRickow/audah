import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from Ah import *
from .help import add_command_help

# Fungsi untuk mengambil gambar dari API dan mengirimkannya sebagai balasan
async def ambil_gambar(client: Client, message: Message, url: str):
    try:
        # Mengambil gambar dari API
        res = requests.get(url)
        data = res.json()
        image_url = data['url']
        
        # Mengirimkan gambar sebagai foto
        await message.reply_photo(image_url)
    except Exception as e:
        await message.reply(f"Gagal mengambil gambar: {str(e)}")

# Handler untuk perintah 'wibu' yang mengambil gambar dari API sfw/waifu
@Client.on_message(filters.command("wibu", cmd) & filters.me)
async def handle_wibu(client: Client, message: Message):
    url = "https://api.waifu.pics/sfw/waifu"  # API untuk gambar SFW
    await ambil_gambar(client, message, url)

# Handler untuk perintah 'waifu' yang mengambil gambar dari API nsfw/waifu
@Client.on_message(filters.command("waifu", cmd) & filters.me)
async def handle_waifu(client: Client, message: Message):
    url = "https://api.waifu.pics/nsfw/waifu"  # API untuk gambar NSFW
    await ambil_gambar(client, message, url)

# Menambahkan bantuan untuk perintah
add_command_help(
    "NSFW",
    [
        ["wibu", "Cari gambar SFW waifu dari waifu API."],
        ["waifu", "Cari gambar NSFW waifu dari waifu API."]
    ],
)

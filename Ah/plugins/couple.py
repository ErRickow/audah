import requests
from pyrogram.types import InputMediaPhoto
import io
from pyrogram import Client, filters
from Ah import *
from Ah.bantuan.tools import *

async def ambil_ppcp(message):
    url = "https://widipe.com/ppcp"
    headers = {'accept': 'application/json'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Menangani kesalahan HTTP
        data = response.json()

        if data.get('status'):
            male_url = data.get('male')
            female_url = data.get('female')
            
            def download_image(url):
                img_response = requests.get(url)
                img_response.raise_for_status()  # Menangani kesalahan HTTP
                return io.BytesIO(img_response.content)

            male_image = download_image(male_url)
            female_image = download_image(female_url)
            
            media = [
                InputMediaPhoto(male_image, caption="Foto Profil Laki-laki"),
                InputMediaPhoto(female_image, caption="Foto Profil Perempuan")
            ]
            
            await message.reply_media_group(media)

@Client.on_message(filters.command("ppcp", cmd) & filters.me)
async def handle_ppcp(client: Client, message: Message):
    await ambil_ppcp(f"<blockquote>{message}</blockquote>")
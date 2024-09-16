import requests
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, Message
import io

from Ah import *

async def ambil_ppcp(message: Message):
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
        else:
            await message.reply("Gambar tidak ditemukan.")
    
    except requests.exceptions.RequestException as e:
        await message.reply(f"Terjadi kesalahan saat mengambil gambar: {str(e)}")
    except Exception as e:
        await message.reply(f"Kesalahan: {str(e)}")

@Client.on_message(filters.command("ppcp", cmd) & filters.me)
async def handle_ppcp(client: Client, message: Message):
    await ambil_ppcp(message)  # Panggil dengan objek message yang benar

    # Jika Anda ingin mengirim balasan setelah memanggil ambil_ppcp
    await message.reply("<blockquote>Done ✔️</blockquote>")
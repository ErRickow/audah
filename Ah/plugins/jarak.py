import requests
from pyrogram.types import InputMediaPhoto
import os

async def ambil_gambar(message, text):
    url = f"https://widipe.com/{text}"
    headers = {'accept': 'image/jpeg'}
  
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        file_path = 'indonesia_image.jpg'
        with open(file_path, 'wb') as f:
            f.write(response.content)

@Client.on_message(filters.command("rn", cmd))
        await message.reply_photo(photo=file_path, caption=f"Gambar dari API {text}")
        
        os.remove(file_path)
    else:
        await message.reply("Gagal mengunduh gambar.")

await ambil_gambar(message, text="malaysia")
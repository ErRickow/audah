import requests
from pyrogram.types import InputMediaPhoto
import io

async def ambil_ppcp(message):
    url = "https://widipe.com/ppcp"
    headers = {'accept': 'application/json'}
    
    response = requests.get(url, headers=headers)
    data = response.json()

    if data.get('status'):
        male_url = data.get('male')
        female_url = data.get('female')
        
        def download_image(url):
            img_response = requests.get(url)
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

await ambil_ppcp(message)
import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from Ah import *
from Ah.bantuan.tools import *

async def tanya(asal, tujuan):
    url = "https://widipe.com/jarak"
    params = {'dari': asal, 'ke': tujuan}
    headers = {'accept': 'application/json'}
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if data.get('status'):
        if 'url' in data and 'data' in data['url']:
            gambar_url = data['url']['data']
            deskripsi = data['url']['desc']
            return gambar_url, deskripsi
    return None, None

@Client.on_message(filters.command("jarak", cmd))
async def mbuh(client, message: Message):
    text = message.text.split(" ")
    
    if len(text) < 3:
        return await message.reply("Kasih teks GOBLOK!! Contoh: /jarak asal tujuan")
    
    asal = text[1]
    tujuan = text[2]
    
    gambar_url, deskripsi = await tanya(asal, tujuan)

    if gambar_url:
        await message.reply_photo(photo=gambar_url, caption=f"> Jarak dari {asal} ke {tujuan} = <code>{deskripsi}</code>")
    else:
        await message.reply("Gambar tidak tersedia atau tidak ada hasil.")

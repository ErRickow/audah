eval import requests

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

@Client.on_message(filters.command("jarak", cmd))
async def mbuh(client, message: Message):
    text = get_text(message)
    if not tujuan:
        return await message.reply("Kasih teks GOLBOK!!")
    await message.reply_photo(photo=gambar_url, caption=f"> Jarak dari {asal} ke {tujuan} = <code>{deskripsi}</code>")
        else:
           await message.reply("Gambar tidak tersedia.")
    else:
      await message.reply("Tidak ada hasil.")
    asal = tanya(asal)
    tujuan = tanya(tujuan)
    await tanya(asal, tujuan)
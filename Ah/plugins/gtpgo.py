import requests

async def tanya(text):
  url = "https://widipe.com/gptgo"
  text = "resep seblak yang gurih kuah kare"
  params = {'text': text}
  headers = {'accept': 'application/json'}
  response = requests.get(url, headers=headers, params=params)
  if response.status_code == 200:
        data = response.json()
  if 'result' in data:
    return data['result'])
else:
    return f"{response.text}"
    
@Client.on_message(filters.command("gtp", cmd))
async def _(client, message):
    text = get_text(message)
    if not text:
        return await message.reply("Kasih teks GOLBOK!!")
    
    hasil = await tanya(text)
    return await message.reply(hasil)
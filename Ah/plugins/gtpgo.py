import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from Ah.bantuan.tools import *

from Ah import *

async def tanya(text):
    url = "https://widipe.com/gptgo"
    params = {'text': text}
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
          # Memastikan status code 200
        data = response.json()
    if 'result' in data:
        return data['result']
    else:
        return f"{response.text}"
#    except requests.exceptions.RequestException as e:
#        return f"Error: {str(e)}"

@Client.on_message(filters.command("gtp", cmd) & filters.me)
async def gtp(client, message: Message):
    text = get_text(message)
    if not text:
        return await message.reply("Kasih teks GOLBOK!!")
    pros = await message.reply("Sabar njing ..")
    hasil = await tanya(text)
    return await pros.edit(hasil)

#########################
async def kotol(text):
    url = "https://widipe.com/openai"
    params = {'text': text}
    headers = {'accept': 'application/json'}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
          # Memastikan status code 200
        data = response.json()
    if 'result' in data:
        return data['result']
    else:
        return f"{response.text}"
#    except requests.exceptions.RequestException as e:
#        return f"Error: {str(e)}"

@Client.on_message(filters.command("gpt", cmd) & filters.me)
async def gtp(client, message: Message):
    text = get_text(message)
    if not text:
        return await message.reply("Kasih teks GOLBOK!!")
    hasil = await kotol(text)
    return await message.reply(f"<blockquote>{hasil}</blockquote>")
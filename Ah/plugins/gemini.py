import os

from pyrogram import Client, filters, enums
from pyrogram.types import Message

from Ah.bantuan.tools import import_library
from config import gemini_key

import google.generativeai as genai

genai.configure(api_key=gemini_key)

model = genai.GenerativeModel("gemini-1.5-flash-latest")


@Client.on_message(filters.command("gemini", prefix) & filters.me)
async def say(_, message: Message):
    try:
        await message.edit_text("<code>Please Wait...</code>")

        if len(message.command) > 1:
            prompt = message.text.split(maxsplit=1)[1]
        elif message.reply_to_message:
            prompt = message.reply_to_message.text
        else:
            await message.edit_text(
                f"<b>Usage: </b><code>{prefix}gemini [prompt/reply to message]</code>"
            )
            return

        chat = model.start_chat()
        response = chat.send_message(prompt)

        await message.edit_text(
            f"**Question:**`{prompt}`\n**Answer:** {response.text}",
            parse_mode=enums.ParseMode.MARKDOWN,
        )
    except Exception as e:
        await message.edit_text(f"An error occurred: {(e)}")


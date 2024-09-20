from Ah import ubot
from pyrogram import filters


@ubot.on_message(filters.command("start") & filters.private)
async def start(client, message):
   await message.reply_text("gtw")

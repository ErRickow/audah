from Ah import *
import time
from datetime import datetime
from pyrogram import *
from Ah.bantuan.tools import *

@Client.on_message(filters.me & filters.command("ping", cmd))
async def pingme(client, message):
    uptime = await readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await message.reply(
        f"❏ **PONG!!🏓**\n"
        f"├• **Pinger** - `%sms`\n"
        f"├• **Uptime -** `{uptime}` \n"
        f"└• **Owner :** {client.me.mention}" % (duration)
    )
# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from pyrogram import *
from pyrogram import filters
from pyrogram.errors import YouBlockedUser
from pyrogram.types import *

from config import PREFIX as cmd
from Ah.bantuan.basic import edit_or_reply
from Ah.utils import extract_user

from .help import add_command_help


@Client.on_message(filters.command(["sg", "sa", "sangmata"], cmd) & filters.me)
async def sg(client: Client, message: Message):
    args = await extract_user(message)
    lol = await message.reply("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            return await lol.edit(f"`User Tidak Valid! Anjeng!`")
    bot = "SangMata_beta_bot"
    try:
        await client.send_message(bot, f"{user.id}")
    except YouBlockedUser:
        await client.unblock_user(bot)
        await client.send_message(bot, f"{user.id}")
    await asyncio.sleep(1)

    async for stalk in client.search_messages(bot, query="Name", limit=1):
        if not stalk:
            await lol.edit_text("**Orang Ini Belum Pernah Mengganti Namanya**")
            return
        elif stalk:
            await lol.edit(stalk.text)
            await stalk.delete()

    async for stalk in client.search_messages(bot, query="Username", limit=1):
        if not stalk:
            return
        elif stalk:
            await lol.edit(stalk.text)
            await stalk.delete()


add_command_help(
    "sangmata",
    [
        [
            f"{cmd}sg <reply/userid/username>",
            "Untuk Mendapatkan Riwayat Nama Pengguna selama di telegram.",
        ],
    ],
)

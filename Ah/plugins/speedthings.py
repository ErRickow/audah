# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import time
import asyncio
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)
from datetime import datetime

import speedtest
from pyrogram import Client, filters
from pyrogram.raw import functions

from config import BOT_VER, BRANCH as brch
from Ah import CMD_HELP, StartTime
from Ah.bantuan.basic import edit_or_reply
from Ah.bantuan.constants import WWW
from Ah import *
from Ah.bantuan.PyroHelpers import SpeedConvert
from Ah.utils.tools import get_readable_time
from Ah.plugins.bot.inline import get_readable_time
from Ah.bantuan.adminHelpers import DEVS

from config import emo
from .help import add_command_help

modules = CMD_HELP

@Client.on_message(filters.command(["speed", "speedtest"], cmd) & filters.me)
async def speed_test(client: Client, message: Message):
    new_msg = await message.reply(f"{emo.load} `Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await new_msg.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@Client.on_message(filters.command("dc", cmd) & filters.me)
async def nearest_dc(client: Client, message: Message):
    dc = await client.send(functions.help.GetNearestDc())
    await edit_or_reply(
        message, WWW.NearestDC.format(dc.country, dc.nearest_dc, dc.this_dc)
    )


@Client.on_message(
    filters.command("ceping", cmd) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command(["ping"], "k") & filters.me)
async def module_ping(client: Client, message: Message):
    cmd = message.command
    help_arg = ""
    bot_username = (await ubot.get_me()).username
    if len(cmd) > 1:
        help_arg = " ".join(cmd[1:])
    elif not message.reply_to_message and len(cmd) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="ping")
            await asyncio.gather(
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id
                ),
            )
        except BaseException as e:
            print(f"{e}")


@Client.on_message(filters.command("er", cmd) & filters.me)
async def module_karman(client: Client, message: Message):
    cdm = message.command
    help_arg = ""
    bot_username = (await ubot.get_me()).username
    if len(cdm) > 1:
        help_arg = " ".join(cdm[1:])
    elif not message.reply_to_message and len(cdm) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="kar")
            await asyncio.gather(
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id),
            )
        except BaseException:
            pass


add_command_help(
    "speedtest",
    [
        ["dc", "Untuk melihat DC Telegram anda."],
        [
            f"speedtest `atau` {cmd}speed",
            "Untuk megetes Kecepatan Server anda.",
        ],
    ],
)


add_command_help(
    "ping",
    [
        ["ping", "Untuk Menunjukkan Ping Bot Anda."],
        ["kping", "Untuk Menunjukkan Ping Bot Anda ( Beda animasi doang )."],
    ],
)

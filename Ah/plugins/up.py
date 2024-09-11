import re
import os
import sys
import asyncio
import subprocess

from git import Repo
from git.exc import (
    GitCommandError,
    InvalidGitRepositoryError,
    NoSuchPathError
)

from pyrogram import Client
from pyrogram.types import Message

from Ah import *
  # TODO: write code...
  
@HAKU.CHA("up")
async def ngapdate(client, message):
    pros = await message.reply(
        f"<blockquote><b>Memeriksa pembaruan resources {app.BotMention} ..</b></blockquote>"
    )
    out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
    teks = f"<b>❒ Status resources {app.BotMention}:</b>\n"
    memeg = f"<b>Change logs {app.BotMention}</b>"
    if "Already up to date." in str(out):
        return await pros.edit(f"<blockquote>{teks}┖ {out}</blockquote>")
    elif len(out) > 4096:
        anuk = await pros.edit(
            f"<blockquote><b>Hasil akan dikirimkan dalam bentuk file ..</b></blockquote>"
        )
        with open("output.txt", "w+") as file:
            file.write(out)

        X = f"<blockquote><b>Change logs {app.BotMention}</b></blockquote>"
        await client.send_document(
            message.chat.id,
            "output.txt",
            caption=f"{X}",
            reply_to_message_id=message.id,
        )
        await anuk.delete()
        os.remove("output.txt")
    else:
        format_line = [f"┣ {line}" for line in out.splitlines()]
        if format_line:
            format_line[-1] = f"┖ {format_line[-1][2:]}"
        format_output = "\n".join(format_line)

        await pros.edit(f"<blockquote>{memeg}\n\n{teks}{format_output}</blockquote>")
    os.execl(sys.executable, sys.executable, "-m", "bangke")
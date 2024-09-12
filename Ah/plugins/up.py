import re
import asyncio
import os
import sys
import shutil
import subprocess

from git import Repo
from git.exc import InvalidGitRepositoryError

from pyrogram import Client, filters
from pyrogram.types import Message

from Ah import *
from config import *


def check_command(command):
    return shutil.which(command) is not None

@Client.on_message(filters.command("up", prefix) & filters.me)
async def ngapdate(client, message):
    pros = await message.reply(
        f"<b>Memeriksa pembaruan resources {client.me.mention}...</b>"
    )
    
    # Melakukan pull dari repository git
    out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
    
    # Mendapatkan commit terakhir
    last_commit = subprocess.check_output(["git", "log", "-1", "--pretty=format:%h %s"]).decode("UTF-8").strip()
    
    teks = "<b>Status resources:</b><br>"
    memeg = f"<b>Perubahan logs by {client.me.mention}</b>"
    
    if "Already up to date." in str(out):
        return await pros.edit(f"<pre>{teks}┖ {out}</pre><br><b>Last Commit:</b> {last_commit}")

    if len(out) > 4096:
        await pros.edit(
            "<b>Hasil akan dikirimkan dalam bentuk file...</b>"
        )
        with open("output.txt", "w+") as file:
            file.write(out)
        # Kirim file jika output terlalu panjang
        await client.send_document(
            message.chat.id,
            "output.txt",
            caption="<b>Perubahan logs:</b>",
            reply_to_message_id=message.id,
        )
        os.remove("output.txt")
        return

    # Format output untuk ditampilkan
    format_line = [f"┣ {line}" for line in out.splitlines()]
    if format_line:
        format_line[-1] = f"┖ {format_line[-1][2:]}"
        format_output = "<br>".join(format_line)
        
    await pros.edit(f"<b>{memeg}</b><br><br>{teks}\n{format_output}<br><b>Last Commit:</b> {last_commit}")
    
    os.execl(sys.executable, sys.executable, "-m", "Ah")
from subprocess import Popen, PIPE, TimeoutExpired
import os
from time import perf_counter

from pyrogram import Client, filters
from pyrogram.types import Message

from Ah import *
from config import *

@Client.on_message(filters.command(["shell", "sh"], prefix) & filters.me)
async def shell(_, message: Message):
    if len(message.command) < 2:
        return await message.reply("<b>Specify the command in message text</b>")
    cmd_text = message.text.split(maxsplit=1)[1]
    cmd_args = cmd_text.split()
    cmd_obj = Popen(
        cmd_args,
        stdout=PIPE,
        stderr=PIPE,
        text=True,
    )

    char = "#" if os.getuid() == 0 else "$"
    text = f"<pre><b>{char}</b> <code>{cmd_text}</code></pre>\n\n"

    anu = await message.reply(text + "<b>Running...</b>")
    try:
        start_time = perf_counter()
        stdout, stderr = cmd_obj.communicate(timeout=60)
    except TimeoutExpired:
        text += "<pre><b>Timeout expired (60 seconds)</b></pre>"
    else:
        stop_time = perf_counter()
        if stdout:
            text += f"<pre><b>Output:</b>\n<code>{stdout}</code></pre>\n\n"
        if stderr:
            text += f"<pre><b>Error:</b>\n<code>{stderr}</code></pre>\n\n"
        text += f"<pre><b>Completed in {round(stop_time - start_time, 5)} seconds with code {cmd_obj.returncode}</b></pre>"
    await anu.edit(text)
    cmd_obj.kill()

from uvloop import install
import asyncio
import importlib
import logging
from aiohttp import ClientSession
from tqdm import tqdm
from pyrogram import idle
from Ah import ubot, BOTLOG, LOGGER, bots, ids, LOOP
from Ah.plugins.basic import join
from Ah.plugins import ALL_MODULES
from config import *

BOT_VER = "0.1.0"
PREFIX = [".", ",", "?", "!"]
MSG_ON = """
💢 **PyroKar Telah Hidup** 💢
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
❍▹ **Userbot Version -** `{}`
❍▹ **Ketik** `{}alive` **untuk Mengecek Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""

async def main():
    await ubot.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module("Ah.plugins" + all_module)
        print(f"Successfully Imported {all_module} ")
    for bot in bots:
        try:
            await ubot.start()
            ex = await ubot.get_me()
            await join(ubot)
            try:
                await ubot.send_message(BOTLOG, MSG_ON.format(BOT_VER, PREFIX))
            except BaseException:
                pass
            print(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Er Anjing").info("The-Ubot Telah Hidup")
    install()
    LOOP.run_until_complete(main())

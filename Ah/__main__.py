from uvloop import install
import asyncio
import importlib
import logging
from aiohttp import ClientSession as aiosession
from tqdm import tqdm
from pyrogram import idle
from Ah import ubot, BOTLOG, LOGGER, bots, ids, LOOP
from Ah.plugins.basic import join
from Ah.plugins import ALL_MODULES
from config import *

BOT_VER = "0.1.0"
PREFIX = ["."]
MSG_ON = """
💢 Ubot Telah Hidup 💢
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
❍▹ Userbot Version - {}
❍▹ Ketik {}alive untuk Mengecek Bot
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


# Fungsi untuk menjalankan tindakan bot
async def main():
    await ubot.start()
    print("LOG: Founded Bot token Booting..")

    for all_module in ALL_MODULES:
        try:
            importlib.import_module("Ah.plugins" + all_module)
            print(f"Successfully Imported {all_module} ")
        except Exception as e:
            LOGGER("Module Error").error(f"Error loading module {all_module}: {e}")

    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await ubot.send_message(BOTLOG, MSG_ON.format(BOT_VER, PREFIX))
            except BaseException as e:
                LOGGER("Bot Log Error").error(f"Error sending message to BOTLOG: {e}")
            print(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            LOGGER("Bot Start Error").error(f"Error starting bot: {e}")

    await asyncio.sleep(100)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Er Anjing").info("The-Ubot Telah Idup")
    install()
    LOOP.run_until_complete(main()) 
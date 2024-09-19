from uvloop import install
import asyncio
import importlib
import logging
import traceback
from aiohttp import ClientSession as aiosession
from tqdm import tqdm
from pyrogram import idle
from Ah import ubot, BOTLOG, LOGGER, bots, ids, LOOP
from Ah.plugins.basic import join
from Ah.plugins import ALL_MODULES
from config import *

BOT_VER = "3.R.0.R"
PREFIX = [""]
MSG_ON = """
💢 Ubot Telah Hidup 💢
╼┅━━━━━━━━━━━━━━━┅╾
❍▹ Userbot Version - {}
❍▹ Ketik {}alive untuk Mengecek Bot
╼┅━━━━━━━━━━╍━━━━┅╾
"""

# Fungsi untuk menjalankan tindakan bot
async def main():
    await ubot.start()
    print("LOG: Founded Bot token Booting..")

    # Load semua modul dari ALL_MODULES
    for all_module in ALL_MODULES:
        try:
            importlib.import_module("Ah.plugins" + all_module)
            print(f"Successfully Imported {all_module}")
        except Exception as e:
            # Menangkap traceback error dan mencatatnya
            error_traceback = traceback.format_exc()
            LOGGER("Module Error").error(f"Error loading module {all_module}: {e}\nTraceback:\n{error_traceback}")

    # Memulai bot dan menangani logika terkait
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await ubot.send_message(BOTLOG, MSG_ON.format(BOT_VER, PREFIX))
            except BaseException as e:
                LOGGER("Bot Log Error").error(f"Error sending message to BOTLOG: {e}")
            print(f"Started as {ex.first_name} | {ex.id}")
            ids.append(ex.id)
        except Exception as e:
            # Menangkap traceback error dan mencatatnya
            error_traceback = traceback.format_exc()
            LOGGER("Bot Start Error").error(f"Error starting bot: {e}\nTraceback:\n{error_traceback}")

    await asyncio.sleep(100)
    await idle()
    await aiosession.close()

if __name__ == "__main__":
    LOGGER("Er Anjing").info("The-Ubot Telah Idup")
    install()
    LOOP.run_until_complete(main())

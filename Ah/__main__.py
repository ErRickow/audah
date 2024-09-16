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
PREFIX = [".", ",", "?", "!"]
MSG_ON = """
💢 PyroKar Telah Hidup 💢
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
❍▹ Userbot Version - {}
❍▹ Ketik {}alive untuk Mengecek Bot
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


# Fungsi untuk menjalankan tindakan bot
async def handle_bot_actions(bot):
    try:
        await bot.start()
        LOGGER.info(f"Started bot {bot.name}")
        await bot.send_message(BOTLOG, "Bot has started successfully.")
        await join(bot)
        ex = await bot.get_me()
        await bot.send_message(BOTLOG, MSG_ON.format(BOT_VER, PREFIX))
        LOGGER.info(f"Started as {ex.first_name} | {ex.id}")
        ids.append(ex.id)
    except Exception as e:
        LOGGER.error(f"Error in bot {bot.name}: {e}")

# Main function
async def main():
    await ubot.start()
    LOGGER.info("Founded Bot token Booting..")

    # Import modules dengan tqdm untuk progress bar
    for all_module in tqdm(ALL_MODULES, desc="Loading modules", unit="module"):
        try:
            importlib.import_module("Ah.plugins." + all_module)
            LOGGER.info(f"Successfully imported {all_module}")
        except Exception as e:
            LOGGER.error(f"Failed to import {all_module}: {e}")

    # Mulai semua session bot
    for bot in bots:
        await handle_bot_actions(bot)  

    await idle()
    await asyncio.sleep(500)
    await aiosession.close()


if __name__ == "__main__":
    LOGGER.info("The-Ubot Telah Hidup")
    install()
    LOOP.run_until_complete(main()) 
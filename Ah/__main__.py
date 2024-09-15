from uvloop import install
import asyncio
import importlib
import logging
from aiohttp import ClientSession
from tqdm import tqdm
from pyrogram import *
from pyrogram.errors import FloodWait
from Ah import ubot, BOTLOG, LOGGER, bots, ids, LOOP, logger
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

# Tambahkan sesi aiohttp untuk request async

async def main():
    await ubot.start()
    logger.info("Bot token ditemukan, bot sedang booting...")
    
    # Mulai semua session bot
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            logger.info(f"Bot {ex.first_name} [{ex.id}] berhasil dimulai.")
            ids.append(ex.id)
            await send_message_with_floodwait_handling(bot, BOTLOG, f"Bot {ex.first_name} telah dimulai.")
            await asyncio.sleep(1)  # Penanganan agar tidak terlalu cepat antar bot
        except Exception as e:
            logger.error(f"Error saat memulai bot: {e}")

    await idle()  # Menjaga bot tetap aktif
    await aiosession.close()

if __name__ == "__main__":
    LOGGER("Pyrogram Bot").info("Bot sedang dimulai...")
    LOOP.run_until_complete(main())

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

# Function Definition (Correct client name usage)
async def send_message_with_floodwait_handling(bot_instance, chat_id, message):  # 'bot_instance' makes it clearer
    try:
        await bot_instance.send_message(chat_id, message)  # Use 'bot_instance' instead of 'client'
    except FloodWait as e:
        logger.warning(f"FloodWait detected. Sleeping for {e.x} seconds.")
        await asyncio.sleep(e.x)
        await send_message_with_floodwait_handling(bot_instance, chat_id, message)  # Retry after wait
    except Exception as e:
        logger.error(f"Error while sending message: {e}")

# Inside the main() function (Update call with correct argument name)
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
            # Pass the bot instance to the function
            await send_message_with_floodwait_handling(bot, BOTLOG, f"Bot {ex.first_name} telah dimulai.")
            await asyncio.sleep(1)  # Penanganan agar tidak terlalu cepat antar bot
        except Exception as e:
            logger.error(f"Error saat memulai bot: {e}")

    await idle()  # Menjaga bot tetap aktif
    await ClientSession.close()

if __name__ == "__main__":
    LOGGER("Pyrogram Bot").info("Bot sedang dimulai...")
    LOOP.run_until_complete(main())

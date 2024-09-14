# Created By HakutakaID # TELEGRAM t.me/hakutakaid
import asyncio
import importlib
import logging
from pyrogram import idle
from Ah import ubot, BOTLOG, LOGGER, bots, ids
from Ah.plugins.basic import join
from Ah.plugins import ALL_MODULES

BOT_VER = "0.1.0"
CMD_HANDLER = ["." , "," , "?" , "!"]
MSG_ON = """
💢 **PyroKar Telah Hidup** 💢
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
❍▹ **Userbot Version -** `{}`
❍▹ **Ketik** `{}alive` **untuk Mengecek Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start_bot():
    # Import semua modul dari Ah.plugins
    for all_module in ALL_MODULES:
        try:
            importlib.import_module(f"Ah.plugins.{all_module}")
            logger.info(f"Module {all_module} imported")
        except Exception as e:
            logger.error(f"Error importing {all_module}: {e}")

    # Mulai bot dengan penanganan floodwait
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)

            # Kirim pesan hanya jika BOTLOG terdefinisi
            if BOTLOG:
                await asyncio.sleep(1)  # Tambahkan delay kecil untuk menghindari floodwait
                try:
                    await bot.send_message(BOTLOG, MSG_ON.format(BOT_VER, CMD_HANDLER[0]))
                except Exception as e:
                    logger.error(f"Error sending message: {e}")

            logger.info(f"Started as {ex.first_name} | {ex.id}")
            ids.append(ex.id)

        except Exception as e:
            logger.error(f"Failed to start bot: {e}")

    await ubot.start()
    await idle()
    logger.info("Bot is running")

if __name__ == "__main__":
    logger.info("Starting bot")
    asyncio.run(start_bot())
    logger.info("Bot stopped")

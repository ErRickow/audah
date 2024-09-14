#Created By HakutakaID # TELEGRAM t.me/hakutakaid
from uvloop import install
import asyncio
import importlib
import logging
from pyrogram import idle
from Ah import ubot, BOTLOG, LOGGER, bots, ids
from Ah.plugins.basic import join
from Ah.plugins import ALL_MODULES

BOT_VER = "0.1.0"
CMD_HANDLER = [".", ",", "?", "!"]
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
    # Import semua modul terlebih dahulu
    for all_module in ALL_MODULES:
        importlib.import_module("Ah.plugins" + all_module)
        logger.info(f"Module {all_module} imported")

    # Start semua bot dengan penundaan untuk menghindari flood wait
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            
            # Kirim pesan hanya jika bot berhasil start
            try:
                await bot.send_message(BOTLOG, MSG_ON.format(BOT_VER, PREFIX))
            except BaseException as e:
                logger.error(f"Failed to send startup message: {e}")

            print(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
            
            # Tambahkan delay kecil antara start bot untuk menghindari flood wait
            await asyncio.sleep(2)

        except Exception as e:
            logger.error(f"Error starting bot: {e}")

    # Start userbot setelah semua bot lainnya
    await ubot.start()
    logger.info("Userbot started")
    await idle()
    logger.info("Bot is idle")

if __name__ == "__main__":
    logger.info("Starting bot")
    asyncio.run(start_bot())
    logger.info("Bot stopped")

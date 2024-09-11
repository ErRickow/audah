#Created By HakutakaID # TELEGRAM t.me/hakutakaid
from uvloop import install
import asyncio
import importlib
import logging
from pyrogram import idle
from Ah import ubot, BOTLOG, LOGGER, aiosession, bots, ids
from Ah.plugins.basic import join
from Ah.plugins import ALL_MODULES

BOT_VER = "0.1.0"
CMD_HANDLER = ["." "," "?" "!"]
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
    for all_module in ALL_MODULES:
        importlib.import_module("Ah.plugins." + all_module)
        logger.info(f"Module {all_module} imported")
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
            except BaseException:
                pass
            print(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
        
    await ubot.start()
    await idle()
    await aiosession.close()
    logger.info("Bot is sange")

if __name__ == "__main__":
    logger.info("Starting bot")
    asyncio.get_event_loop().run_until_complete(start_bot())
    logger.info("Bot stopped")
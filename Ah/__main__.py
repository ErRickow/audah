from uvloop import install
import asyncio
import importlib
import logging
from tqdm import tqdm
from pyrogram import idle
from Ah import ubot, BOTLOG, LOGGER, bots, ids
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

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start_bot():
    print("LOG: Founded Bot token Booting..")
    for module in tqdm(ALL_MODULES, desc="Loading modules", unit="module"):
        importlib.import_module("Ah.plugins" + module)
        logger.info(f"Module {module} imported")
    
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG, MSG_ON.format(BOT_VER, PREFIX))
            except BaseException:
                pass
            print(f"Started as {ex.first_name} | {ex.id}")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
#        await asyncio.sleep(5)
    await ubot.start()
    await idle()
#    aiosession.close()
    logger.info("Bot is sange")

if __name__ == "__main__":
    logger.info("Starting bot")
    install()
 #   LOOP.run_until_complete(start_bot())
    asyncio.get_event_loop().run_until_complete(start_bot())
    logger.info("Bot stopped")

#Created By HakutakaID # TELEGRAM t.me/hakutakaid
import logging
import time
import sys
import asyncio  # Perlu untuk jeda yang asinkron
from logging.handlers import RotatingFileHandler
from pyrogram.errors import FloodWait  # Import untuk menangani FloodWait
from aiohttp import ClientSession
from datetime import datetime
from pyrogram import Client
from pyrogram import filters as indri
from pyrogram.handlers import CallbackQueryHandler, MessageHandler
from config import *


DATABASE_URL = DB_URL
CMD_HELP = {}
clients = []
ids = []
LOG_FILE_NAME = "logs.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

if (
    not API_ID
):
    LOGGER(__name__).warning("api id missing")
    sys.exit()
if (
    not API_HASH
):
    LOGGER(__name__).warning("api Hashnya missing")
    sys.exit()
if (
    not BOT_TOKEN
):
    LOGGER(__name__).warning("Isilah bot token nya")
    sys.exit()

if (
    not STRING_SESSION1
    and not STRING_SESSION2
    and not STRING_SESSION3
    and not STRING_SESSION4
    and not STRING_SESSION5
):
    LOGGER(__name__).warning("STRING SESSION TIDAK DITEMUKAN, SHUTDOWN BOT!")
    sys.exit()

if BOTLOG:
   BOTLOG = BOTLOG
else:
   BOTLOG = "me"

START_TIME = datetime.now()

StartTime = time.time()

class Ubot(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()
        logger.info("Bot started")

ubot = Ubot(
    name="sange",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Ah/plugins/bot"),
    in_memory=True,
)

# Fungsi untuk menangani floodwait dan memberi jeda antar akun
async def send_message_with_delay(bot, *args, **kwargs):
    try:
        await bot.send_message(*args, **kwargs)
    except FloodWait as e:
        logger.warning(f"FloodWait: Harus menunggu {e.x} detik")
        await asyncio.sleep(e.x)
        await bot.send_message(*args, **kwargs)

# Mengirim pesan secara bergantian dengan jeda antar bot
async def send_message_to_all_bots(chat_id, text):
    for bot in bots:
        try:
            await send_message_with_delay(bot, chat_id, text)
        except Exception as e:
            logger.error(f"Error saat mengirim pesan dengan {bot.name}: {e}")
        await asyncio.sleep(5)  # Jeda 1 detik antar setiap bot

bots = [
    Client(
        name=f"bot{i+1}",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=globals().get(f"STRING_SESSION{i+1}"),
        plugins=dict(root="Ah/plugins"),
    )
    for i in range(10)
    if globals().get(f"STRING_SESSION{i+1}")
]

# Memulai semua bot
async def start_bots():
    for bot in bots:
        await bot.start()
        logger.info(f"{bot.name} started")

# Fungsi untuk menghentikan semua bot
async def stop_bots():
    for bot in bots:
        await bot.stop()
        logger.info(f"{bot.name} stopped")

# Mulai bot utama dan bot tambahan lainnya
async def main():
    await start_bots()

    # Misalnya untuk mengirim pesan ke semua bot
    await send_message_to_all_bots("some_chat_id", "Halo, ini pesan dari semua bot!")

    await stop_bots()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot dihentikan")

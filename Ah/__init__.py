# Created By HakutakaID # TELEGRAM t.me/hakutakaid
import logging
import asyncio
import sys
import time
from logging.handlers import RotatingFileHandler
from aiohttp import ClientSession
from pyrogram import Client
from pyrogram.handlers import CallbackQueryHandler, MessageHandler
from pyrogram.errors import FloodWait
from datetime import datetime
from config import *

DATABASE_URL = DB_URL
CMD_HELP = {}
clients = []
ids = []
LOG_FILE_NAME = "logs.txt"

# Konfigurasi logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
logging.getLogger("pyrogram.session.auth").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session.session").setLevel(logging.CRITICAL)

logger = logging.getLogger(__name__)
LOOP = asyncio.get_event_loop()

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

# Memastikan API_ID, API_HASH, dan BOT_TOKEN tersedia
if not API_ID:
    LOGGER(__name__).warning("API ID missing")
    sys.exit()
if not API_HASH:
    LOGGER(__name__).warning("API Hash missing")
    sys.exit()
if not BOT_TOKEN:
    LOGGER(__name__).warning("Isilah bot token nya")
    sys.exit()

# Memastikan minimal satu session string terdefinisi
if not any([STRING_SESSION1, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4, STRING_SESSION5]):
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
        logger.info("Bot Aktif Anjing")

ubot = Ubot(
    name="sange",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Ah/plugins/bot"),
    in_memory=True,
)

# Membuat daftar bots berdasarkan session string
bot1 = (
    Client(
        name="bot1",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION1,
        plugins=dict(root="Ah/plugins"),
    )
    if STRING_SESSION1
    else None
)

bot2 = (
    Client(
        name="bot2",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION2,
        plugins=dict(root="Ah/plugins"),
    )
    if STRING_SESSION2
    else None
)

bot3 = (
    Client(
        name="bot3",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION3,
        plugins=dict(root="Ah/plugins"),
    )
    if STRING_SESSION3
    else None
)

bot4 = (
    Client(
        name="bot4",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION4,
        plugins=dict(root="Ah/plugins"),
    )
    if STRING_SESSION4
    else None
)

bot5 = (
    Client(
        name="bot5",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION5,
        plugins=dict(root="Ah/plugins"),
    )
    if STRING_SESSION5
    else None
)

bot6 = (
    Client(
        name="bot6",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION6,
        plugins=dict(root="Ah/plugins"),
    )
    if STRING_SESSION6
    else None
)

bot7 = (
    Client(
        name="bot7",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION7,
        plugins=dict(root="Ah/plugins"),
    )
    if STRING_SESSION7
    else None
)

bot8 = (
    Client(
        name="bot8",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION8,
        plugins=dict(root="Ah/plugins"),
    )
    if STRING_SESSION8
    else None
)

bot9 = (
    Client(
        name="bot9",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION9,
        plugins=dict(root="Ah/plugins"),
    )
    if STRING_SESSION9
    else None
)

bot10 = (
    Client(
        name="bot10",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=STRING_SESSION10,
        plugins=dict(root="Ah/plugins"),
    )
    if STRING_SESSION10
    else None
)


bots = [bot for bot in [bot1, bot2, bot3, bot4, bot5, bot6, bot7, bot8, bot9, bot10] if bot]

# Fungsi untuk mengirim pesan dengan penanganan FloodWait
async def send_message_with_floodwait_handling(client, chat_id, message):
    try:
        await client.send_message(chat_id, message)
    except FloodWait as e:
        logger.warning(f"FloodWait detected. Sleeping for {e.x} seconds.")
        await asyncio.sleep(e.x)
        await send_message_with_floodwait_handling(client, chat_id, message)  # Retry after wait
    except Exception as e:
        logger.error(f"Error while sending message: {e}")

# Fungsi untuk join channel/group dengan penanganan FloodWait
async def join_channel_with_floodwait_handling(client, channel_id):
    try:
        await client.join_chat(channel_id)
    except FloodWait as e:
        logger.warning(f"FloodWait detected while joining chat. Sleeping for {e.x} seconds.")
        await asyncio.sleep(e.x)
        await join_channel_with_floodwait_handling(client, channel_id)  # Retry after wait
    except Exception as e:
        logger.error(f"Error while joining chat: {e}")

# Fungsi contoh untuk handle bot
async def handle_bot_actions(bot):
    # Menangani bot action dengan penanganan FloodWait dan logging error
    try:
        await bot.start()
        logger.info(f"Started bot {bot.name}")

        # Replace dengan aksi bot seperti mengirim pesan atau join channel
        await send_message_with_floodwait_handling(bot, BOTLOG, "Bot has started successfully.")
        await join_channel_with_floodwait_handling(bot, "@example_channel")

    except Exception as e:
        logger.error(f"Unhandled exception in bot {bot.name}: {e}")

# Kamu bisa menjalankan handle_bot_actions di tempat di mana kamu memulai bot, tanpa membuat fungsi start_bot baru

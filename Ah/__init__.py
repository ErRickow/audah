# Created By HakutakaID # TELEGRAM t.me/hakutakaid
import logging
import asyncio
import sys
import time
import datetime
from logging.handlers import RotatingFileHandler
from pyrogram.handlers import CallbackQueryHandler, MessageHandler
from aiohttp import ClientSession
from pyrogram import Client
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

ubot = Ubot(
    name="sange",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Ah/plugins/bot"),
    in_memory=True,
)

# Membuat daftar bots berdasarkan session string
bots = [
    Client(
        name=f"bot{i+1}",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=globals().get(f"STRING_SESSION{i+1}"),
        plugins=dict(root="Ah/plugins"),
    )
    for i in range(10) if globals().get(f"STRING_SESSION{i+1}")
]


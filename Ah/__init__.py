#Created By HakutakaID # TELEGRAM t.me/hakutakaid
import logging
import time
from datetime import datetime
from pyrogram import Client as mecha
from pyrogram import filters as indri
from pyrogram.handlers import CallbackQueryHandler, MessageHandler
from config import *

DATABASE_URL = DB_URL
CMD_HELP = {}
SUDO_USER = SUDO_USERS
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

class Ubot(mecha):
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
    session_string=SESSION,
    in_memory=True,
)

from Ah.bantuan import *

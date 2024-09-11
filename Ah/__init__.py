#Created By HakutakaID # TELEGRAM t.me/hakutakaid
import logging
import time
from datetime import datetime
from pyrogram import Client as mecha
from pyrogram import filters as indri
from pyrogram.handlers import CallbackQueryHandler, MessageHandler
from config import *
from Ah.bantuan import *


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

aiosession = ClientSession()

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
    bot_token=BOT_TOKEN,
    plugins=dict(root="Ah/plugins/bot"),
    in_memory=True,
)
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

from base64 import b64decode as jandigantinantierornanges
from distutils.util import strtobool
from os import getenv
from PyroKar.helpers.cmd import cmd

from dotenv import load_dotenv

load_dotenv("config.env")

API_HASH = getenv("API_HASH")
API_ID = int(getenv("API_ID", ""))
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001473548283, -1001812143750]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "1.1.5@main"
BRANCH = getenv("BRANCH", "main")
CMD_HNDLR = cmd
OWNER_ID = getenv("OWNER_ID", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
CHANNEL = getenv("CHANNEL", "Pamerdong")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "sqlite:///tron.db")
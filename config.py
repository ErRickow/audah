import os
from base64 import b64decode as jandigantinantierornanges
from distutils.util import strtobool
from os import getenv
from Ah.bantuan.cmd import cmd

from dotenv import load_dotenv

load_dotenv()
API_ID = os.getenv["API_ID"]
API_HASH = os.getenv["API_HASH"]
BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
if not BLACKLIST_CHAT:
    BLACKLIST_CHAT = [-1001473548283, -1001812143750]
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BOT_VER = "1.1.5@main"
BRANCH = getenv("BRANCH", "main")
CMD_HNDLR = cmd
OWNER_ID = getenv("OWNER_ID", "")
BOT_TOKEN = getenv("BOT_TOKEN")
CHANNEL = getenv("CHANNEL", "Pamerdong")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "sqlite:///tron.db")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    jandigantinantierornanges("").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "obrolansuar")
PMPERMIT_PIC = getenv("PMPERMIT_PIC", None)
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
REPO_URL = getenv("REPO_URL", "https://github.com/ErRickow/audah")
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))

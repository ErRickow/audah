import os
from dotenv import load_dotenv

from Ah.bantuan.cmd import cmd

load_dotenv(".env")

API_ID = os.getenv("API_ID")

API_HASH = os.getenv("API_HASH")

SESSION = os.getenv("SESSION")

BOTLOG_CHATID = os.getenv("BOTLOG_CHATID")
BOT_VER = "1.1.5@main"
BRANCH = getenv("BRANCH", "main") #don't change
prefix = cmd
OWNER_ID = getenv("OWNER_ID", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OPENAI_API = getenv("OPENAI_API", "")
CHANNEL = getenv("CHANNEL", "Karc0de")
CMD_HANDLER = getenv("CMD_HANDLER", ".")
DB_URL = getenv("DATABASE_URL", "")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    jandigantinantierornanges("").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "obrolansuar")

DEVS = [1831850761]

BLACKLIST_GCAST = [-1001921519384, -1002053287763, -1002044997044, -1002022625433, -1002050846285]

if not all([API_ID, API_HASH, SESSION]):
    raise ValueError("Missing one or more environment variables: API_ID, API_HASH, SESSION")
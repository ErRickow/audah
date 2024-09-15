from base64 import b64decode as jandigantinantierornanges
from distutils.util import strtobool
import os 
from os import getenv
from dotenv import load_dotenv

from Ah.bantuan.cmd import cmd

load_dotenv(".env")

API_ID = os.getenv("API_ID")

API_HASH = os.getenv("API_HASH")

BOTLOG = os.getenv("BOTLOG")
BOT_VER = "1.1.5@main"
BRANCH = getenv("BRANCH", "main") #don't change
CMD_HAND = cmd
OWNER_ID = getenv("OWNER_ID", "6607703424")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL = getenv("CHANNEL", "Pamerdong")
PREFIX = getenv("PREFIX", "x")
DB_URL = getenv("DATABASE_URL", "sqlite:///tron.db")
GIT_TOKEN = getenv(
    "GIT_TOKEN",
    jandigantinantierornanges("").decode(
        "utf-8"
    ),
)
GROUP = getenv("GROUP", "Pamerdong")

gemini_key = os.getenv("GEMINI_KEY")
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

DEVS = [1448273246, 6607703424]

BLACKLIST_GCAST = [-1001921519384, -1002053287763, -1002044997044, -1002022625433, -1002050846285]

DWL_DIR = "./downloads/"
TEMP_DIR = "./temp/"
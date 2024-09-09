import asyncio
import logging
import os
import random
import re
import string
import time
from datetime import datetime as dt
from inspect import getfullargspec
import sqlite3
import platform
import subprocess
import asyncio
import logging
import sys
import time
from datetime import datetime
from logging.handlers import RotatingFileHandler
from typing import Any, Dict


from aiohttp import ClientSession
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from gpytranslate import Translator
from pyrogram import Client

from config import (
    API_HASH,
    API_ID,
    DB_URL,
    BOTLOG_CHATID,
    STRING_SESSION1,
    STRING_SESSION2,
    STRING_SESSION3,
    STRING_SESSION4,
    STRING_SESSION5,
    STRING_SESSION6,
    STRING_SESSION7,
    STRING_SESSION8,
    STRING_SESSION9,
    STRING_SESSION10,
    SUDO_USERS,
    BOT_TOKEN
)
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
logging.getLogger("asyncio").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)
logging.getLogger("pyrogram.session.auth").setLevel(logging.CRITICAL)
logging.getLogger("pyrogram.session.session").setLevel(logging.CRITICAL)

import importlib
from pyrogram import idle
from uvloop import install

from Ah.plugins import ALL_MODULES
from Ah import BOTLOG_CHATID, LOGGER, LOOP, aiosession, app, bots, ids
from Ah.plugins.basic import join
from PyroKar.helpers.misc import heroku
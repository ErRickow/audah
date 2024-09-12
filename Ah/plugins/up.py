import re
import os
import sys
import asyncio
import subprocess

from git import Repo
from git.exc import (
    GitCommandError,
    InvalidGitRepositoryError,
    NoSuchPathError
)

from pyrogram import *
from pyrogram.types import Message

from Ah.bantuan.restart import *
from Ah import *
from config import Config
  # TODO: write code...
  
@Client.on_message(filters.me & filters.command("up", cmd))
async def update_bot(_, message: Message):
    anji = await message.reply(message, "**🔄 Sabar nyet...**")

    if len(message.command) < 2:
        status, repo, force = await initialize_git(Config.REPO_URL)
        if not status:
            return await message.error(anji, repo)

        active_branch = repo.active_branch.name
        upstream = repo.remote("upstream")
        upstream.fetch(active_branch)

        changelogs = await gen_changelogs(repo, f"HEAD..upstream/{active_branch}")
        if not changelogs and not force:
            repo.__del__()
            return await anji.edit("__Gada update tersedia.__"
            )

        if force:
            return await anji.edit(
                f"Force-sync...... sabar dulu ya njink.\n\n{changelogs}",
                disable_web_page_preview=True,
            )

        return await anji.edit(
            f"**🍂 𝖴𝗉𝖽𝖺𝗍𝖾 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝖿𝗈𝗋 𝖯𝗅𝗎𝗀𝗂𝗇𝗌:**\n\n{changelogs}",
            disable_web_page_preview=True,
        )

    anu = message.command[1].lower()
    if anu == "y":
            await anji.edit(
                "**🔄 M e n g u p d a t e!** \n__B o t A k a n S t a r t D a l a m B e b e r a p a M e n i t.__"
            )
            return await restart(update=True)
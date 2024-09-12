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

from Ah import *
  # TODO: write code...
  
@Client.on_message(filters.me & filters.command("up", cmd))
async def update_bot(_, message: Message):
    anji = await message.reply(message, "**🔄 𝖨𝗇 𝖯𝗋𝗈𝗀𝗋𝖾𝗌𝗌...**")

    if len(message.command) < 2:
        status, repo, force = await initialize_git(Config.PLUGINS_REPO)
        if not status:
            return await hellbot.error(hell, repo)

        active_branch = repo.active_branch.name
        upstream = repo.remote("upstream")
        upstream.fetch(active_branch)

        changelogs = await gen_changelogs(repo, f"HEAD..upstream/{active_branch}")
        if not changelogs and not force:
            repo.__del__()
            return await hellbot.delete(
                hell, "__There are no updates available right now.__"
            )

        if force:
            return await hell.edit(
                f"Force-Sync in progress... Please wait for a moment and try again.\n\n{changelogs}",
                disable_web_page_preview=True,
            )

        return await hell.edit(
            f"**🍂 𝖴𝗉𝖽𝖺𝗍𝖾 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝖿𝗈𝗋 𝖯𝗅𝗎𝗀𝗂𝗇𝗌:**\n\n{changelogs}",
            disable_web_page_preview=True,
        )

    cmd = message.command[1].lower()
    if cmd == "plugins":
        if HEROKU_APP:
            try:
                heroku = heroku3.from_key(Config.HEROKU_APIKEY)
                app = heroku.apps()[Config.HEROKU_APPNAME]
                await hell.edit(
                    "**🔄 𝖴𝗉𝖽𝖺𝗍𝖾𝖽 𝖯𝗅𝗎𝗀𝗂𝗇𝗌 𝗋𝖾𝗉𝗈!** \n__𝖡𝗈𝗍 𝗐𝗂𝗅𝗅 𝗌𝗍𝖺𝗋𝗍 𝗐𝗈𝗋𝗄𝗂𝗇𝗀 𝖺𝖿𝗍𝖾𝗋 1 𝗆𝗂𝗇𝗎𝗍𝖾.__"
                )
                app.restart()
            except Exception as e:
                return await hellbot.error(message, f"`{e}`")
        else:
            await hell.edit(
                "**🔄 𝖴𝗉𝖽𝖺𝗍𝖾𝖽 𝖯𝗅𝗎𝗀𝗂𝗇𝗌 𝗋𝖾𝗉𝗈!** \n__𝖡𝗈𝗍 𝗐𝗂𝗅𝗅 𝗌𝗍𝖺𝗋𝗍 𝗐𝗈𝗋𝗄𝗂𝗇𝗀 𝖺𝖿𝗍𝖾𝗋 1 𝗆𝗂𝗇𝗎𝗍𝖾.__"
            )
            return await restart(update=True)

    elif cmd == "deploy":
        if HEROKU_APP:
            os.chdir("/app")
            status, repo, _ = await initialize_git(Config.DEPLOY_REPO)
            if not status:
                return await hellbot.error(hell, repo)

            active_branch = repo.active_branch.name
            upstream = repo.remote("upstream")
            upstream.fetch(active_branch)

            heroku = heroku3.from_key(Config.HEROKU_APIKEY)
            app = heroku.apps()[Config.HEROKU_APPNAME]

            await hell.edit(
                "**🔄 𝖣𝖾𝗉𝗅𝗈𝗒𝗂𝗇𝗀 𝖨𝗇 𝖯𝗋𝗈𝗀𝗋𝖾𝗌𝗌...**\nThis might take upto 5 minutes to complete!"
            )
            repo.git.reset("--hard", "FETCH_HEAD")
            heroku_git = app.git_url.replace(
                "https://", f"https://api:{Config.HEROKU_APIKEY}@"
            )

            if "heroku" in repo.remotes:
                remote = repo.remote("heroku")
                remote.set_url(heroku_git)
            else:
                remote = repo.create_remote("heroku", heroku_git)

            try:
                remote.push(f"HEAD:refs/heads/master", force=True)
            except BaseException as e:
                repo.__del__()
                return await hellbot.error(hell, f"__Invalid Heroku Creds:__ `{e}`")

            build = app.builds(order_by="created_at", sort="desc")[0]
            if build.status == "failed":
                return await hellbot.error(
                    hell,
                    "__There were some problems with the update! Make sure your heroku api and app name are correct.__",
                )

            try:
                remote.push("master:main", force=True)
            except BaseException as e:
                repo.__del__()
                return await hellbot.error(hell, f"__Invalid Heroku Creds:__ `{e}`")
        else:
            await hell.edit(
                "**🔄 𝖣𝖾𝗉𝗅𝗈𝗒𝗂𝗇𝗀 𝖨𝗇 𝖯𝗋𝗈𝗀𝗋𝖾𝗌𝗌...**\n\n__Please wait for a minute or two.__"
            )
            return await restart(update=True)
    else:
        return await hellbot.delete(
            hell, f"**[ ⚠️ ]** __Invalid update argument:__ `{cmd}`"
        )

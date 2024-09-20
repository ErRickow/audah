#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#
# Ported by @mrismanaziz
# FROM PyroMan-Userbot < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# t.me/Lunatic0de & t.me/SharingUserbot
#

import asyncio
import socket
import sys
from datetime import datetime
from os import environ, execle, path, remove

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from pyrogram import Client, filters
from pyrogram.types import Message

from config import BRANCH
from config import PREFIX as cmd
from config import GIT_TOKEN, REPO_URL, emo
from Ah.bantuan.adminHelpers import DEVS
from Ah.bantuan.basic import edit_or_reply
from Ah.bantuan.tools import get_arg
from Ah.utils.misc import restart
from Ah.utils.pastebin import PasteBin
from Ah.utils.tools import bash
from Ah import ubot

from .help import add_command_help

if GIT_TOKEN:
    GIT_USERNAME = REPO_URL.split("com/")[1].split("/")[0]
    TEMP_REPO = REPO_URL.split("https://")[1]
    UPSTREAM_REPO = f"https://{GIT_USERNAME}:{GIT_TOKEN}@{TEMP_REPO}"
    UPSTREAM_REPO_URL = UPSTREAM_REPO
else:
    UPSTREAM_REPO_URL = REPO_URL

requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), "requirements.txt"
)


async def gen_chlog(repo, diff):
    ch_log = ""
    d_form = "%d/%m/%y"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"• [{c.committed_datetime.strftime(d_form)}]: {c.summary} <{c.author}>\n"
        )
    return ch_log


async def updateme_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


@Client.on_message(
    filters.command("edup", ["r"]) & filters.user(DEVS) & ~filters.me
)
@Client.on_message(filters.command("git", cmd) & filters.me)
async def upstream(client: Client, message: Message):
    status = await message.reply(f"`{emo.proses} Mengecek Pembaruan, Tunggu Sebentar...`")
    conf = get_arg(message)
    off_repo = UPSTREAM_REPO_URL
    try:
        txt = (
            "**ANJENG Pembaruan Tidak Dapat Di Lanjutkan sattt "
            + "Terjadi Beberapa ERROR BANGSAT**\n\n**LOGTRACE:**\n"
        )
        repo = Repo()
    except NoSuchPathError as error:
        await status.edit(f"{txt}\n**Directory** `{error}` **Tidak Dapat Di Temukan.**")
        repo.__del__()
        return
    except GitCommandError as error:
        await status.edit(f"{txt}\n**Gagal kek Satt!** `{error}`")
        repo.__del__()
        return
    except InvalidGitRepositoryError:
        if conf != "deploy":
            pass
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        repo.create_head(
            BRANCH,
            origin.refs[BRANCH],
        )
        repo.heads[BRANCH].set_tracking_branch(origin.refs[BRANCH])
        repo.heads[BRANCH].checkout(True)
    ac_br = repo.active_branch.name
    if ac_br != BRANCH:
        await status.edit(
            f"**[UPDATER]:** `Looks like you are using your own custom branch ({ac_br}). in that case, Updater is unable to identify which branch is to be merged. please checkout to main branch`"
        )
        repo.__del__()
        return
    try:
        repo.create_remote("upstream", off_repo)
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)
    changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    if "pull" not in conf:
        if changelog:
            changelog_str = f"<blockquote>yhi {client.me.mention}\n\n**{emo.warn} Tersedia Update\n\nCHANGELOG:**\n\n`{changelog}`</blockquote>"
            if len(changelog_str) > 4096:
                await status.edit("**Changelog terlalu besar, dikirim sebagai file.**")
                file = open("output.txt", "w+")
                file.write(changelog_str)
                file.close()
                await client.send_document(
                    message.chat.id,
                    "output.txt",
                    caption=f"<b><i>from {ubot.me.mention} {emo.cntng}</i></b>",
                    reply_to_message_id=status.id,
                )
                remove("output.txt")
            else:
                return await status.edit(
                    f"{changelog_str}<blockquote>from {ubot.me.mention} {emo.cntng}</blockquote>",
                    disable_web_page_preview=True,
                )
        else:
            await status.edit(
                f"\n`BOT LU is` **up-to-date** {emo.cntng}\n",
                disable_web_page_preview=True,
            )
            repo.__del__()
            return
    try:
        ups_rem.pull(ac_br)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await updateme_requirements()
    await status.edit(
        f"<blockquote>{ubot.me.mention} `Telah Diupdate! {emo.cntng}\n Userbot bisa di Gunakan Lagi.`</blockquote>",
    )
    args = [sys.executable, "-m", "Ah"]
    execle(sys.executable, *args, environ)
    return


@Client.on_message(filters.command("cupdate", ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("goupdate", cmd) & filters.me)
async def updaterman(client: Client, message: Message):
    response = await message.reply(f"{emo.proses} Checking for available updates...")
    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit(f"{emo.gagal} Git Command Error")
    except InvalidGitRepositoryError:
        return await response.edit(f"{emo.gagal} Invalid Git Repsitory")
    to_exc = f"git fetch origin {BRANCH} &> /dev/null"
    await bash(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]  # main git repository
    for checks in repo.iter_commits(f"HEAD..origin/{BRANCH}"):
        verification = str(checks.count())
    if verification == "":
        return await response.edit(f"Bot is up-to-date! {emo.cntng}")
    updates = ""
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[(format // 10 % 10 != 1) * (format % 10 < 4) * format % 10 :: 4],
    )
    for info in repo.iter_commits(f"HEAD..origin/{BRANCH}"):
        updates += f"<blockquote><b>➣ #{info.count()}: [{info.summary}]({REPO_}/commit/{info}) by -> {info.author}</b>\n\t\t\t\t<b>➥ Commited on:</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}</blockquote>\n\n"
    _update_response_ = f"<blockquote><b>{emo.warn} A new update is available for the Bot!</b>\n\n➣ Pushing Updates Now</code>\n\n<b><u>Updates:</u></b></blockquote>\n\n"
    _final_updates_ = _update_response_ + updates
    if len(_final_updates_) > 4096:
        url = await PasteBin(updates)
        nrs = await response.edit(
            f"<blockquote><b>{emo.warn} Tersedia Update!</b>\n\n➣ Update lah sekarang</code>\n\n**<u>Updates:</u>**\n\n[Cek Update]({url})</blockquote>"
        )
    else:
        nrs = await response.edit(_final_updates_, disable_web_page_preview=True)
    await bash("git stash &> /dev/null && git pull")
    await bash("pip3 install -r requirements.txt")
    await response.edit(f"Successfully Updated Userbot {emo.cntng}")
    args = [sys.executable, "-m", "Ah"]
    execle(sys.executable, *args, environ)
    return


add_command_help(
    "update",
    [
        ["git", "Untuk melihat list pembaruan terbaru dari Bot."],
        ["git pull", "Untuk mengupdate userbot."],
    ],
)


@Client.on_message(filters.command("restart", cmd) & filters.me)
async def restart_(client: Client, message: Message):
    await message.reply_text(f"`{emo.proses} {ubot.me.mention} sedang direstart...`")
    args = [sys.executable, "-m", "Ah"]
    execle(sys.executable, *args, environ)
    return


@Client.on_message(filters.command("shutdown", cmd) & filters.me)
async def shutdown_(client: Client, message: Message):
    await message.reply_text(f"`{ubot.me.mention} dimatikan! {emo.cntng}`")
    sys.exit(0)

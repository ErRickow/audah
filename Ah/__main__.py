from uvloop import install
import asyncio
import importlib
import logging
import traceback
from aiohttp import ClientSession as aiosession
from tqdm import tqdm
from pyrogram import idle
from Ah import ubot, BOTLOG, LOGGER, bots, ids, LOOP
from Ah.plugins.basic import join
from Ah.plugins import ALL_MODULES
from config import *

BOT_VER = "3.R.0.R"
PREFIX = [""]
MSG_ON = """<blockquote>
💢 {mention} **AKTIF**
Bot Version: {bot_ver}
Prefix: {prefix}
╼┅━━━━━━━━━━━━━━━┅╾</blockquote>
"""

async def send_error_log(module_name, error_message):
    """
    Mengirimkan pesan error ke BOTLOG jika ada kesalahan dalam memuat modul.
    """
    error_text = f"**Error loading module** `{module_name}`:\n```{error_message}```"
    try:
        await ubot.send_message(BOTLOG, error_text)
    except BaseException as e:
        LOGGER("Bot Log Error").error(f"Error sending error log to BOTLOG: {e}")

# Fungsi untuk menjalankan tindakan bot
async def main():
    await ubot.start()
    print("LOG: Founded Bot token Booting..")

    # Dapatkan informasi pengguna bot setelah memulai
    ubot_me = await ubot.get_me()  # Mendapatkan objek 'me'
    
    # Cek apakah informasi 'me' berhasil diambil
    if ubot_me is None:
        print("Failed to get bot user information.")
        return  # Hentikan eksekusi jika gagal mendapatkan info pengguna

    # Load semua modul dari ALL_MODULES
    for all_module in ALL_MODULES:
        try:
            importlib.import_module("Ah.plugins" + all_module)
            print(f"Successfully Imported {all_module}")
        except Exception as e:
            # Menangkap traceback error dan mencatatnya
            error_traceback = traceback.format_exc()
            LOGGER("Module Error").error(f"Error loading module {all_module}: {e}\nTraceback:\n{error_traceback}")
            # Mengirim log error ke botlog
            await send_error_log(all_module, error_traceback)

    # Pesan untuk menginformasikan bot yang berhasil diaktifkan
    startup_message = MSG_ON.format(
        mention=ubot_me.mention,
        bot_ver=BOT_VER,
        prefix=', '.join(PREFIX)
    )

    # Menggabungkan daftar bot yang berhasil diaktifkan ke dalam satu pesan
    active_bots = []
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            active_bots.append(f"{ex.first_name} | ID: {ex.id}")
            ids.append(ex.id)
        except Exception as e:
            # Menangkap traceback error dan mencatatnya
            error_traceback = traceback.format_exc()
            LOGGER("Bot Start Error").error(f"Error starting bot: {e}\nTraceback:\n{error_traceback}")

    # Jika ada bot yang berhasil diaktifkan, tambahkan ke pesan startup
    if active_bots:
        startup_message += "\n\n💡 **Active Bots**:\n"
        startup_message += "\n".join(active_bots)

    # Mengirim pesan startup sekaligus
    try:
        await ubot.send_message(BOTLOG, startup_message)
    except BaseException as e:
        LOGGER("Bot Log Error").error(f"Error sending startup message to BOTLOG: {e}")

    await asyncio.sleep(100)
    await idle()
    await aiosession.close()

if __name__ == "__main__":
    LOGGER("Er Anjing").info("The-Ubot Telah Idup")
    install()
    LOOP.run_until_complete(main())

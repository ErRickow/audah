from uvloop import install
import asyncio
import importlib
import logging
from aiohttp import ClientSession
from tqdm import tqdm
from pyrogram import idle
from pyrogram.errors import FloodWait
from Ah import ubot, BOTLOG, LOGGER, bots, ids, LOOP
from Ah.plugins.basic import join
from Ah.plugins import ALL_MODULES
from config import *

BOT_VER = "0.1.0"
PREFIX = [".", ",", "?", "!"]
MSG_ON = """
💢 **PyroKar Telah Hidup** 💢
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
❍▹ **Userbot Version -** `{}`
❍▹ **Ketik** `{}alive` **untuk Mengecek Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""

# Tambahkan sesi aiohttp untuk request async
aiosession = ClientSession()

# Fungsi untuk menangani FloodWait saat bot mengirim pesan
async def send_message_with_floodwait_handling(client, chat_id, message):
    try:
        await client.send_message(chat_id, message)
    except FloodWait as e:
        LOGGER("FloodWait").warning(f"FloodWait detected. Sleeping for {e.x} seconds.")
        await asyncio.sleep(e.x)
        await send_message_with_floodwait_handling(client, chat_id, message)  # Coba lagi setelah FloodWait selesai
    except Exception as e:
        LOGGER("Error").error(f"Error while sending message: {e}")

# Fungsi untuk join channel dengan FloodWait handling
async def join_channel_with_floodwait_handling(client, channel_id):
    try:
        await client.join_chat(channel_id)
    except FloodWait as e:
        LOGGER("FloodWait").warning(f"FloodWait detected while joining chat. Sleeping for {e.x} seconds.")
        await asyncio.sleep(e.x)
        await join_channel_with_floodwait_handling(client, channel_id)  # Coba lagi setelah FloodWait selesai
    except Exception as e:
        LOGGER("Error").error(f"Error while joining chat: {e}")

# Fungsi untuk menjalankan tindakan bot dengan penanganan FloodWait
async def handle_bot_actions(bot):
    try:
        await bot.start()
        LOGGER("Bot Start").info(f"Started bot {bot.name}")

        # Contoh penggunaan fungsi FloodWait handling saat mengirim pesan atau bergabung dengan channel
        await send_message_with_floodwait_handling(bot, BOTLOG, "Bot has started successfully.")
        await join_channel_with_floodwait_handling(bot, "@example_channel")

    except Exception as e:
        LOGGER("Error").error(f"Unhandled exception in bot {bot.name}: {e}")

# Main function
async def main():
    await ubot.start()
    LOGGER("LOG").info("Founded Bot token Booting..")
    
    # Import modules dengan tqdm untuk progress bar
    for all_module in tqdm(ALL_MODULES, desc="Loading modules", unit="module"):
        importlib.import_module("Ah.plugins" + all_module)
        LOGGER("Modules").info(f"Successfully Imported {all_module} ")

    # Mulai semua session bot
    for bot in bots:
        try:
            await handle_bot_actions(bot)  # Menggunakan fungsi handle_bot_actions untuk setiap bot
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG, MSG_ON.format(BOT_VER, PREFIX))
            except BaseException:
                pass
            LOGGER("Bot Info").info(f"Started as {ex.first_name} | {ex.id}")
            ids.append(ex.id)
        except Exception as e:
            LOGGER("Error").error(f"{e}")

    await idle()
    await aiosession.close()

if __name__ == "__main__":
    LOGGER("Er Anjing").info("The-Ubot Telah Hidup")
    install()
    LOOP.run_until_complete(main())

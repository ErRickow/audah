import importlib
from pyrogram import idle
from uvloop import install

from Ah.plugins import ALL_MODULES
from Ah import BOTLOG_CHATID, LOGGER, LOOP, aiosession, app, bots, ids
from Ah.plugins.basic import join

BOT_VER = "0.1.0"
CMD_HANDLER = "."  # Atau gunakan CMD_HANDLER = [".", "?", "!"] jika mendukung lebih dari satu handler
MSG_ON = """
💢 **PyroKar Telah Hidup** 💢
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
❍▹ **Userbot Version -** `{}`
❍▹ **Ketik** `{}alive` **untuk Mengecek Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        try:
            importlib.import_module("Ah.plugins." + all_module)
            print(f"Successfully Imported {all_module} ")
        except ModuleNotFoundError as e:
            print(f"Failed to import {all_module}: {e}")
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
            except Exception as e:
                print(f"Failed to send message in BOTLOG_CHATID: {e}")
            print(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            print(f"Error during bot start: {e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("ErUserbot").info("Er Ubot Telah Idup")
    install()
    LOOP.run_until_complete(main())

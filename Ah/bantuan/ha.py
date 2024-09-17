from pyrogram import filters, Client

from Ah import *


class FIL:
    ME = filters.me
    GROUP = filters.group
    PRIVATE = filters.private
    OWNER = filters.user(OWNER_ID)
    SUDO = filters.user(USER_ID)
    ME_GROUP = filters.me & filters.group
    ME_OWNER = filters.me & filters.user(OWNER_ID)
    ME_USER = filters.me & filters.user(USER_ID)


class ER:
    def BOT(command, filter=FIL.PRIVATE):
        def wrapper(func):
            @ubot.on_message(filters.command(command) & filter)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def GC():
        def wrapper(func):
            @Client.on_message(
                filters.group & filters.incoming & filters.mentioned & ~filters.bot
            )
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def PC():
        def wrapper(func):
            @Client.on_message(
                filters.private
                & filters.incoming
                & ~filters.me
                & ~filters.bot
                & ~filters.service
            )
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def PM():
        def wrapper(func):
            @Client.on_message(
                filters.private
                & filters.incoming
                & ~filters.me
                & ~filters.bot
                & ~filters.via_bot
                & ~filters.service,
            )
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def UBOT(command, filter=FIL.ME):
        def wrapper(func):
            @Client.on_message(filters.command(command, "^") & filters.user(USER_ID))
            @Client.on_message(anjay(command) & filter)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def INLINE(command):
        def wrapper(func):
            @ubot.on_inline_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def CALLBACK(command):
        def wrapper(func):
            @ubot.on_callback_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

import traceback

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from Ah import CMD_HELP, ubot
from Ah.bantuan.data import Data
from Ah.bantuan.inline import cb_wrapper, paginate_help
from Ah import ids as users

@Client.on_callback_query()
async def _callbacks(_, callback_query: CallbackQuery):
    query = callback_query.data.lower()
    await ubot.get_me()
    if query == "helper":
        buttons = paginate_help(0, CMD_HELP, "helpme")
        await ubot.edit_inline_text(
            callback_query.inline_message_id,
            Data.text_help_menu,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif query == "close":
        await ubot.edit_inline_text(callback_query.inline_message_id, "<b>— CLOSED</b>")
        return
    elif query == "close_help":
        if callback_query.from_user.id not in users:
           return
        await ubot.edit_inline_text(
            callback_query.inline_message_id,
            "<b>— CLOSED MENU HELP</b>",
            reply_markup=InlineKeyboardMarkup(Data.reopen),
        )
        return
    elif query == "closed":
        try:
            await callback_query.message.delete()
        except BaseException:
            pass
        try:
            await callback_query.message.reply_to_message.delete()
        except BaseException:
            pass
    elif query == "make_basic_button":
        try:
            bttn = paginate_help(0, CMD_HELP, "helpme")
            await ubot.edit_inline_text(
                callback_query.inline_message_id,
                Data.text_help_menu,
                reply_markup=InlineKeyboardMarkup(bttn),
            )
        except Exception as e:
            e = traceback.format_exc()
            print(e, "Callbacks")


@ubot.on_callback_query(filters.regex("ub_modul_(.*)"))
@cb_wrapper
async def on_plug_in_cb(_, callback_query: CallbackQuery):
    modul_name = callback_query.matches[0].group(1)
    commands: dict = CMD_HELP[modul_name]
    this_command = f"<blockquote>──「 <b>Bantuan untuk {str(modul_name).upper()}</b> 」──\n\n"
    for x in commands:
        this_command += f"  •  <b>Command:</b> <code>.{str(x)}</code>\n  •  <b>Function:</b> <code>{str(commands[x])}</code>\n\n"
    this_command += "© er?</blockquote>"
    bttn = [
        [InlineKeyboardButton(text="Return", callback_data="reopen")],
    ]
    reply_pop_up_alert = (
        this_command
        if this_command is not None
        else f"{module_name} No documentation has been written for the module."
    )
    await ubot.edit_inline_text(
        callback_query.inline_message_id,
        reply_pop_up_alert,
        reply_markup=InlineKeyboardMarkup(bttn),
    )


@ubot.on_callback_query(filters.regex("reopen"))
@cb_wrapper
async def reopen_in_cb(_, callback_query: CallbackQuery):
    buttons = paginate_help(0, CMD_HELP, "helpme")
    await ubot.edit_inline_text(
        callback_query.inline_message_id,
        Data.text_help_menu,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@ubot.on_callback_query(filters.regex("helpme_prev\((.+?)\)"))
@cb_wrapper
async def on_plug_prev_in_cb(_, callback_query: CallbackQuery):
    current_page_number = int(callback_query.matches[0].group(1))
    buttons = paginate_help(current_page_number - 1, CMD_HELP, "helpme")
    await ubot.edit_inline_text(
        callback_query.inline_message_id,
        Data.text_help_menu,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@ubot.on_callback_query(filters.regex("helpme_next\((.+?)\)"))
@cb_wrapper
async def on_plug_next_in_cb(_, callback_query: CallbackQuery):
    current_page_number = int(callback_query.matches[0].group(1))
    buttons = paginate_help(current_page_number + 1, CMD_HELP, "helpme")
    await ubot.edit_inline_text(
        callback_query.inline_message_id,
        Data.text_help_menu,
        reply_markup=InlineKeyboardMarkup(buttons),
    )

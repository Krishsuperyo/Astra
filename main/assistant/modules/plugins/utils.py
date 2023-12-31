from main.userbot.client import app

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton





@app.bot.on_message(filters.command("id"), group=0)
async def bot_getids_handler(_, m):
    reply = m.reply_to_message
    if not reply:
        await app.bot.send_message(
            m.chat.id,
            f"**{m.from_user.first_name}:** `{m.from_user.id}`\n**{m.chat.title}:** `{m.chat.id}`"
        )
    elif reply:
        await app.bot.send_message(
            m.chat.id,
            f"**{m.from_user.first_name}:** `{m.from_user.id}`\n**{m.chat.title}:** `{m.chat.id}`\n**{reply.from_user.first_name}:** `{reply.from_user.id}`"
        )




@app.bot.on_message(filters.command("quote"), group=1)
async def bot_animequote_handler(_, m):
    await app.bot.send_message(
        m.chat.id,
        app.animeQuote(),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "More", callback_data="animequote-tab"
                    )
                ],
            ]
        )
    )



"""
Inline assistant page for help menu.
"""

from pyrogram import filters

from pyrogram.types import (
	InlineKeyboardMarkup,
	InputMediaPhoto,
        InputMediaVideo,
	CallbackQuery
)

from main.userbot.client import app





@app.bot.on_callback_query(filters.regex("assistant-tab"))
@app.alert_user
async def _assistant(_, cb: CallbackQuery):
    await cb.edit_message_media(
        media=InputMediaPhoto(
            media="main/core/resources/videos/nora.png",
            caption=app.assistant_tab_string()
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                app.bot.BuildKeyboard(
                    (
                        ["Home", "close-tab"],
                        ["Back", "home-tab"]
                    )
                )
            ]
        )
    )

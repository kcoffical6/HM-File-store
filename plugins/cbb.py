#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"╭─《 🔰𝔸𝔹𝕆𝕌𝕋 𝕄𝔼🔰 》\n├  CREATOR: <a href='tg://user?id={OWNER_ID}'>🅷🅸🆃🅻🅴🆁</a>\n├  CHANNEL: <a href='https://t.me/Kan_Serial'>Serial Adda</a>\n├ LANGUAGE USED: Python\n╰  𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔❤️",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

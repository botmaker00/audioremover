from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatAction, ParseMode
import asyncio
import random
import logging
from utils import user_selections, safe_telegram_call

logger = logging.getLogger(__name__)

# Sticker
stickers = [
    "CAACAgUAAxkBAAEOXBhoCoKZ76jevKX-Vc5v5SZhCeQAAXMAAh4KAALJrhlVZygbxFWWTLw2BA"
]

welcome_text = "<i><blockquote>Wᴇʟᴄᴏᴍᴇ, ʙᴀʙʏ… ɪ’ᴠᴇ ʙᴇᴇɴ ᴄʀᴀᴠɪɴɢ ʏᴏᴜʀ ᴘʀᴇsᴇɴᴄᴇ ғᴇᴇʟs ᴘᴇʀғᴇᴄᴛ ɴᴏᴡ ᴛʜᴀᴛ ʏᴏᴜ’ʀᴇ ʜᴇʀᴇ.</blockquote></i>"

def create_main_buttons():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about"),
            InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ", url="https://t.me/clutch008"),
        ],
        [
            InlineKeyboardButton("Dᴇᴠᴇʟᴏᴩᴇʀ", url="https://t.me/clutch008"),
        ],
    ])

def register_status_handlers(app: Client):
    @app.on_message(filters.command("status"))
    async def show_status(client: Client, message: Message):
        chat_id = message.chat.id

        # Animated intro
        await client.send_chat_action(chat_id, ChatAction.TYPING)
        msg = await safe_telegram_call(message.reply_text, welcome_text, parse_mode=ParseMode.HTML)
        await asyncio.sleep(0.1)
        await safe_telegram_call(msg.edit_text, "<b><i><pre>Cʜᴇᴄᴋɪɴɢ sᴛᴀᴛᴜs...</pre></i></b>", parse_mode=ParseMode.HTML)
        await asyncio.sleep(0.1)
        await safe_telegram_call(msg.delete)

        # Sticker
        await client.send_chat_action(chat_id, ChatAction.CHOOSE_STICKER)
        await safe_telegram_call(message.reply_sticker, random.choice(stickers))

        # Status message
        status_text = []
        for uid in user_selections.get(chat_id, {}):
            if not isinstance(user_selections[chat_id][uid], dict):
                continue
            try:
                user = await client.get_users(uid)
                user_name = user.username if user.username else user.first_name
                user_name = user_name.replace("_", "\\_")  # Escape underscores for Markdown
                status_text.append(f"User [{user_name}](tg://user?id={uid}) ({uid}): {user_selections[chat_id][uid].get('status', 'Idle')}")
            except Exception as e:
                logger.error(f"Error fetching user {uid}: {str(e)}")
                status_text.append(f"User {uid}: {user_selections[chat_id][uid].get('status', 'Idle')} (Name unavailable)")
        status_message = "\n".join(status_text) if status_text else "No active processes."

        caption = (
            f"<pre>Sᴛᴀᴛᴜs Uᴩᴅᴀᴛᴇ</pre>\n"
            f"<b><blockquote>{status_message}</b></blockquote>"
        )

        await safe_telegram_call(
            app.send_message,
            chat_id=chat_id,
            text=caption,
            reply_markup=create_main_buttons(),
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True
        )

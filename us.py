from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatAction, ParseMode
import asyncio
import random
import logging
from config import DAILY_LIMIT_FREE, DAILY_LIMIT_PREMIUM, PREMIUM_USERS
from utils import user_selections, daily_limits, safe_telegram_call, sanitize_filename

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

def register_us_handlers(app: Client):
    @app.on_message(filters.command("us"))
    async def set_user_settings(client: Client, message: Message):
        try:
            chat_id, user_id = message.chat.id, message.from_user.id

            # Animated intro
            await client.send_chat_action(chat_id, ChatAction.TYPING)
            msg = await message.reply_text(welcome_text, parse_mode=ParseMode.HTML)
            await asyncio.sleep(0.1)
            await msg.edit_text("<b><i><pre>Sᴇᴛᴛɪɴɢ ᴜᴩ...</pre></i></b>", parse_mode=ParseMode.HTML)
            await asyncio.sleep(0.1)
            await msg.delete()

            # Sticker
            await client.send_chat_action(chat_id, ChatAction.CHOOSE_STICKER)
            await message.reply_sticker(random.choice(stickers))

            args = message.text.split(maxsplit=2)[1:]
            if chat_id not in user_selections:
                user_selections[chat_id] = {}
            if user_id not in user_selections[chat_id]:
                user_selections[chat_id][user_id] = {'status': 'Idle', 'last_percent': 0}
            
            if not args:
                config = user_selections[chat_id][user_id]
                limit = DAILY_LIMIT_PREMIUM if user_id in PREMIUM_USERS else DAILY_LIMIT_FREE
                daily_data = daily_limits.get(user_id, {'count': 0})
                remaining = max(0, limit - daily_data['count'])
                user = await client.get_users(user_id)
                user_name = user.username if user.username else user.first_name
                response = (
                    f"<pre>Uᴤᴇʀ Cᴏɴғɪɢᴜʀᴀᴛɪᴏɴ</pre>\n"
                    f"<b><blockquote>User: {user_name} ({user_id})\n"
                    f"- Default Filename: {config.get('default_name', 'Not set')}\n"
                    f"- Default Caption: {config.get('default_caption', 'Not set')}\n"
                    f"- Daily Limit: {limit} videos\n"
                    f"- Remaining Today: {remaining} videos\n"
                    f"- Status: {config.get('status', 'Idle')}</blockquote></b>"
                )
                await safe_telegram_call(
                    app.send_message,
                    chat_id=chat_id,
                    text=response,
                    reply_markup=create_main_buttons(),
                    parse_mode=ParseMode.HTML
                )
                return
            
            if len(args) < 2:
                await safe_telegram_call(
                    app.send_message,
                    chat_id=chat_id,
                    text=(
                        f"<pre>Eʀʀᴏʀ</pre>\n"
                        f"<b><blockquote>Usage: /us &lt;filename&gt; &lt;caption&gt;</blockquote></b>"
                    ),
                    reply_markup=create_main_buttons(),
                    parse_mode=ParseMode.HTML
                )
                return
            
            default_name, default_caption = sanitize_filename(args[0]), args[1]
            user_selections[chat_id][user_id]['default_name'] = default_name
            user_selections[chat_id][user_id]['default_caption'] = default_caption
            await safe_telegram_call(
                app.send_message,
                chat_id=chat_id,
                text=(
                    f"<pre>Sᴇᴛᴛɪɴɢs Uᴩᴅᴀᴛᴇᴅ</pre>\n"
                    f"<b><blockquote>Filename: {default_name}\nCaption: {default_caption}</blockquote></b>"
                ),
                reply_markup=create_main_buttons(),
                parse_mode=ParseMode.HTML
            )
        except Exception as e:
            logger.error(f"Error in set_user_settings: {str(e)}")
            await safe_telegram_call(
                app.send_message,
                chat_id=chat_id,
                text=(
                    f"<pre>Eʀʀᴏʀ</pre>\n"
                    f"<b><blockquote>An error occurred: {str(e)}</blockquote></b>"
                ),
                reply_markup=create_main_buttons(),
                parse_mode=ParseMode.HTML
            )

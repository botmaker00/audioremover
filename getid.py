from pyrogram import Client, filters
from pyrogram.types import Message
import logging
from utils import safe_telegram_call

logger = logging.getLogger(__name__)

def register_getid_handlers(app: Client):
    @app.on_message(filters.command("getid"))
    async def get_chat_id(client: Client, message: Message):
        await safe_telegram_call(message.reply, f"Chat ID: {message.chat.id}, Chat Type: {message.chat.type}")

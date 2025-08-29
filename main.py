import os
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import logging
from start import register_start_handlers
from status import register_status_handlers
from us import register_us_handlers
from video import register_video_handlers
from cancel import register_cancel_handlers
from getid import register_getid_handlers

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Pyrogram client
app = Client("audio_selector_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def main():
    """Main function to start the bot."""
    register_start_handlers(app)
    register_status_handlers(app)
    register_us_handlers(app)
    register_video_handlers(app)
    register_cancel_handlers(app)
    register_getid_handlers(app)
    logger.info("Starting bot...")
    app.run()

if __name__ == "__main__":
    main()

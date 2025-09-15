Audio Selector Bot
Overview
This is a Telegram bot built using Pyrogram that allows users to upload video files, select specific audio tracks from the video, and process/export the video with the chosen audio tracks. It supports formats like MP4 (video) and MKV (document). The bot is designed for use in authorized groups or by the owner, with features like daily limits, queuing, and progress tracking.
The bot extracts audio tracks using FFmpeg, lets users select tracks via inline keyboards, and re-muxes the video with selected audio while copying the video stream unchanged. Temporary files are cleaned up after processing.
Key Features:

Download videos from Telegram (up to 4GB).
Detect and list audio tracks (with language/title tags if available).
Select multiple audio tracks via interactive keyboard.
Choose output format: MP4 (as video) or MKV (as document).
Progress bars for download/upload.
User settings for default filename/caption.
Daily usage limits (15 for free users, 30 for premium).
Queue support for multiple files.
Cancel ongoing processes with /cancel.
Status checks with /status.
Get chat ID with /getid.

Note: This bot is not an anime news bot; it's focused on audio track selection and video processing.
Requirements

Python 3.8+
FFmpeg (for audio extraction and video processing)
Required Python packages:

pyrogram
tqdm (for progress bars)
ffmpeg-python



Installation


Clone the Repository:
textgit clone <your-repo-url>  # Or download the files manually
cd <repo-name>


Install Dependencies:
textpip install -U pyrogram tqdm ffmpeg-python
Install FFmpeg:

On Ubuntu/Debian: sudo apt update && sudo apt install ffmpeg
On Windows: Download from FFmpeg official site and add to PATH.
On macOS: brew install ffmpeg



Setup Configuration:

Edit config.py with your Telegram API credentials:

API_ID: Your API ID from my.telegram.org.
API_HASH: Your API Hash from my.telegram.org.
BOT_TOKEN: Your bot token from @BotFather.
ALLOWED_GROUP_IDS: List of group chat IDs where the bot is allowed (get via /getid).
OWNER_ID: Your Telegram user ID (get via /getid).
PREMIUM_USERS: Set of premium user IDs for higher limits.
DOWNLOAD_DIR: Directory for temporary downloads (default: "downloads").
MAX_FILE_SIZE: Max file size (default: 4GB).



Example config.py snippet:
pythonAPI_ID = 12345678  # Replace with yours
API_HASH = "your_api_hash_here"
BOT_TOKEN = "your_bot_token_here"
ALLOWED_GROUP_IDS = [-1001234567890]  # Add your group IDs
OWNER_ID = 123456789  # Your user ID


Create Directories:
The bot will auto-create downloads/ but ensure write permissions.


Run the Bot:
textpython main.py
The bot will start and log "Starting bot...".


Usage

Start the Bot:

Send /start to the bot in a private chat or authorized group.
It shows a welcome message with buttons for About, Support, and Developer.


Upload a Video:

Send a video file or document (video) in an allowed group.
The bot replies with "Starting download..." and shows a progress bar (updates every 5%).
After download: Tagged notification like "@username your media has been downloaded, now select the tracks."
Inline keyboard appears for track selection (e.g., "✅ English Track 0").


Select Audio Tracks:

Toggle tracks by clicking buttons (✅ indicates selected).
Click "Done" when ready (must select at least one).
Choose output: "Video (MP4)" or "Document (MKV)".


Processing and Upload:

Bot processes the video (keeps video stream, selects audio tracks).
Generates thumbnail.
Uploads with progress bar and default caption/filename (customizable via /us).
Cleans up temporary files.


Commands:

/start: Welcome message.
/us [filename] [caption]: Set default filename and caption (or view current settings).

Example: /us MyVideo %title% (use %title% for dynamic titles if implemented).


/status: Show current processing status for users in the chat.
/cancel: Cancel ongoing process and delete temp files.
/getid: Get chat ID and type.


Queueing:

If processing, new videos are queued. Bot notifies queue position.
Processes next after current finishes.


Limits:

Free users: 15 videos/day.
Premium: 30 videos/day.
Resets daily.


Customization:

Edit us.py or start.py for welcome text/stickers.
Add more groups to ALLOWED_GROUP_IDS.
Modify limits in config.py.



Troubleshooting

Download Fails: Check file size (<4GB), FFmpeg installation, and disk space in DOWNLOAD_DIR.
No Audio Tracks: Ensure video has audio; bot skips invalid files.
Permission Errors: Run with write access to DOWNLOAD_DIR.
Flood Waits: Bot handles Telegram rate limits automatically.
Logs: Check console for errors (logging level: INFO).
Queue Stuck: Use /cancel and restart if needed.
FFmpeg Errors: Verify FFmpeg path; test with ffmpeg -version.

Support

Developer: @clutch008
Channel: ABHI 
Updates: BOTSKINGDOM

License
This bot is provided as-is. Feel free to fork and modify. No warranty.

Note: This README is generated based on the provided code structure. Add screenshots (e.g., track selection keyboard) or deploy instructions if hosting on Heroku/VPS. For advanced features like dynamic titles or more formats, extend utils.py.

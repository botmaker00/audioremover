# 🎵 Audio Selector Bot

A **Telegram bot** built using [Pyrogram](https://docs.pyrogram.org/) that allows users to upload video files, select specific audio tracks, and process/export the video with chosen audio tracks.  
It supports formats like **MP4 (video)** and **MKV (document)**.  

The bot is designed for **authorized groups** or the **owner**, with features like **daily limits, queuing, and progress tracking**.  
It extracts audio tracks using **FFmpeg**, lets users select tracks via **inline keyboards**, and re-muxes the video with selected audio while copying the video stream unchanged.  
Temporary files are cleaned up after processing.

---

## 🚀 Key Features
- 📥 Download videos from Telegram (up to **4GB**).
- 🎧 Detect and list audio tracks (with language/title tags if available).
- ✅ Select multiple audio tracks via interactive inline keyboard.
- 📦 Choose output format: **MP4 (as video)** or **MKV (as document)**.
- 📊 Progress bars for download/upload.
- ⚙️ User settings for default filename/caption.
- ⏳ Daily usage limits (**15 for free users, 30 for premium**).
- 📚 Queue support for multiple files.
- ❌ Cancel ongoing processes with `/cancel`.
- 🔍 Status checks with `/status`.
- 🆔 Get chat ID with `/getid`.

> **Note:** This bot is **not** an anime/news bot – it’s purely for **audio track selection and video processing**.

---

## 🛠 Requirements

- **Python 3.8+**
- **FFmpeg** (for audio extraction and video processing)

### Required Python packages

pip install -U pyrogram tqdm ffmpeg-python


##Install FFmpeg

Ubuntu/Debian:

sudo apt update && sudo apt install ffmpeg


Windows: Download from FFmpeg official site
 and add to PATH.

##macOS:

brew install ffmpeg

⚙️ Installation

##Clone the Repository

git clone <your-repo-url>
cd <repo-name>


##Install Dependencies

pip install -U pyrogram tqdm ffmpeg-python


#Setup Configuration

Edit config.py with your Telegram API credentials:

API_ID = 12345678  # Replace with yours
API_HASH = "your_api_hash_here"
BOT_TOKEN = "your_bot_token_here"

ALLOWED_GROUP_IDS = [-1001234567890]  # Add your group IDs
OWNER_ID = 123456789  # Your user ID
PREMIUM_USERS = {987654321}  # Premium users get higher limits

DOWNLOAD_DIR = "downloads"
MAX_FILE_SIZE = 4 * 1024 * 1024 * 1024  # 4GB


Create Directories

The bot auto-creates downloads/, but ensure it has write permissions.

Run the Bot

python main.py

#📌 Usage
1. Start the Bot

Send /start to the bot in a private chat or an authorized group.

Shows a welcome message with buttons for About, Support, and Developer.

2. Upload a Video

Send a video file or document (video) in an allowed group.

The bot replies:

Starting download...


with a progress bar.

After download:

@username your media has been downloaded, now select the tracks.


Inline keyboard appears for track selection:

✅ English Track 0

3. Select Audio Tracks

Toggle tracks by clicking buttons (✅ = selected).

Click Done when ready (must select at least one).

Choose output:

🎬 Video (MP4)

📂 Document (MKV)

4. Processing and Upload

Bot processes video (copies video stream, selects audio tracks).

Generates thumbnail.

Uploads with progress bar and default caption/filename.

Cleans up temporary files.


🔧 Commands

/start → Welcome message

/us [filename] [caption] → Set default filename and caption

Example:

/us MyVideo %title%


(%title% = dynamic title placeholder)

/status → Show current processing status

/cancel → Cancel ongoing process and delete temp files

/getid → Get chat ID and type

⏳ Queueing & Limits

New uploads are queued if processing is ongoing.

Bot notifies queue position.

Limits:

Free users: 15 videos/day

Premium: 30 videos/day

Resets daily.

🐞 Troubleshooting

Download Fails → Check file size (<4GB), FFmpeg installation, and disk space.

No Audio Tracks → Ensure video has audio.

Permission Errors → Run with write access to DOWNLOAD_DIR.

Flood Waits → Bot handles Telegram rate limits automatically.

Queue Stuck → Use /cancel and restart.

FFmpeg Errors → Verify FFmpeg path, test with:

ffmpeg -version

📢 Support

👨‍💻 Developer: @clutch008

📡 Channel: ABHI

🔔 Updates: BOTSKINGDOM

📜 License

This bot is provided as-is.
Feel free to fork and modify.
No warranty.

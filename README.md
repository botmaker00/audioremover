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
```bash
pip install -U pyrogram tqdm ffmpeg-python

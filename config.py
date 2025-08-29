import os

# Telegram API credentials
API_ID = 29483517  # Replace with your API ID
API_HASH = "e35a05d338376cbcd8162f810aed878d"  # Replace with your API Hash
BOT_TOKEN = "8421689554:AAFQFiefgHXFfXLwimNFEGZZ8SQ4p8UWzjQ"  # Replace with your Bot Token

# Directory for downloads
DOWNLOAD_DIR = "downloads"

# Allowed group IDs
ALLOWED_GROUP_IDS = [
    -1002729239201,  # Your group ID from logs
    # Add more group IDs as needed
]

# Owner user ID
OWNER_ID = 5756495153  # Owner's user ID

# Maximum file size (e.g., 4GB)
MAX_FILE_SIZE = 4 * 1024 * 1024 * 1024  # 4GB in bytes

# Premium users and daily limits
PREMIUM_USERS = {5756495153}  # Add premium user IDs here
DAILY_LIMIT_FREE = 15  # Videos per day for free users
DAILY_LIMIT_PREMIUM = 30  # Videos per day for premium users

# Ensure download directory exists
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
if not os.access(DOWNLOAD_DIR, os.W_OK):
    raise PermissionError(f"No write permission for {DOWNLOAD_DIR}")

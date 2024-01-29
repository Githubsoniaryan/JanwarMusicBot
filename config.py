from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/ec19cf227791a167abedc.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/ec19cf227791a167abedc.jpg")

SESSION = getenv("SESSION", None)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/royalgroupop")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/itsRareBeautySelenaGomez")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Op_king_music_Bot")  

FAILED = "https://te.legra.ph/file/ec19cf227791a167abedc.jpg"

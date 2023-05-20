from os import environ
import re

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

SESSION = environ.get("SESSION", "forward bot")
API_ID = int(environ.get("API_ID", "16491027"))
API_HASH = environ.get("API_HASH", "f98a18193ba4f65024671d973fea32d3")
BOT_TOKEN = environ.get("BOT_TOKEN", "6189880153:AAH5M7ahk5rZJ6bk3Oo7G3rx6TKoZyoCajI")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001700545247"))
PORT = int(environ.get("PORT", "8080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '668692506').split()]
TARGET_DB = int(environ.get("TARGET_DB", "-1001884385825"))
UPSTREAM_REPO = environ.get("UPSTREAM_REPO", "https://github.com/BLVCK-ANGEL/File-Forward-Bot")

import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()




MONGO_DB_URI = "mongodb+srv://anjlnobita:tCUPU9Ty1FFvLumv@cluster0.appf0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DATABASE_URL = "mongodb+srv://anjlnobita:tCUPU9Ty1FFvLumv@cluster0.appf0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"



JOIN_LOGGER = -1002372313866
LOG_GROUP_ID = -1002372313866
EVENT_LOGS = -1002372313866


OWNER_ID = 7335060704


DRAGONS = 7335060704
DEV_USERS = 7335060704
DEMONS = 7335060704
TIGERS = 7335060704
WOLVES = 7335060704


DRAGONS = 6777860063
DEV_USERS = 7335060704
DEMONS = 6397808634
MEOW = 7666460878

#OWNER_ID = [DEV_USERS, DRAGONS, DEMONS, MEOW]


OWNER_ID = (6777860063, 7335060704, 6397808634, 7666460878)




AI_API_KEY = "api key "

LOG = 2
LOG_FILE_NAME = "logs.txt"
TEMP_DB_FOLDER = "jane_doe"


EVENT_LOGS = ()  
BL_CHATS = [] 
DRAGONS = [] 
DEV_USERS = []  
DEMONS = []  
TIGERS = [] 
WOLVES = [] 


ALLOW_CHATS = True
ALLOW_EXCL = True
DEL_CMDS = True
INFOPIC = True
LOAD = []
NO_LOAD = []
STRICT_GBAN = True
WORKERS = 8
WEBHOOK = False
URL = None

BAN_STICKER = "" 

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}





#API_ID = int(getenv("API_ID"))
#API_HASH = getenv("API_HASH")


#BOT_TOKEN = getenv("BOT_TOKEN")



DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 888))





HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/anjlnobita/jane_doe",
)



UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
) 

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/noxarion_network")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/anime_societyy")


AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))




SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))



TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))


STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)





START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/kRs.jpg"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/JKS.jpg"
)

PLAYLIST_IMG_URL = "https://envs.sh/oX0.jpg"

STATS_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"

TELEGRAM_AUDIO_URL = "https://envs.sh/r78.jpg"

TELEGRAM_VIDEO_URL = "https://telegra.ph/file/e575ae40d6635250974e1.jpg"

STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"

SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"

YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"



def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
    
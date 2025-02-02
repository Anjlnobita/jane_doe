import logging
import os
import sys
import time
import aiohttp
from aiohttp import ClientSession

import telegram.ext as tg
from pyrogram import Client, errors
from telethon import TelegramClient
import config 


from jane.modules.noxarion import clonebotdb




# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)











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




SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/noxarion_network")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/anime_societyy")





























try:
    OWNER_ID = int(OWNER_ID)
except ValueError:
    raise Exception("Your OWNER_ID variable is not a valid integer.")


try:
    DRAGONS = set(int(x) for x in config.DRAGONS or [])
    DEV_USERS = set(int(x) for x in DEV_USERS or [])
except ValueError:
    raise Exception("Your sudo or dev users list does not contain valid integers.")

try:
    DEMONS = set(int(x) for x in DEMONS or [])
except ValueError:
    raise Exception("Your support users list does not contain valid integers.")

try:
    WOLVES = set(int(x) for x in WOLVES or [])
except ValueError:
    raise Exception("Your whitelisted users list does not contain valid integers.")

try:
    TIGERS = set(int(x) for x in TIGERS or [])
except ValueError:
    raise Exception("Your tiger users list does not contain valid integers.")


DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)



API_ID = 20650066
API_HASH = "7a4f8ed638f1369a40693574c2835217"
#TOKEN = "7963650428:AAGvbf9QIAWsZRhv9QGxka33OqqGQtX4axc"

def load_bot_token():
    default_token = "8007775153:AAGX6U201PrUnl1zGqCxWy_HRMzQ3fKUP9c"
    bot_tokens = clonebotdb.find()
    tokens = [default_token] + [token["token"] for token in bot_tokens]
    return tokens

bot_tokens = load_bot_token()




WORKERS = 8
updater = tg.Updater(bot_tokens, workers=WORKERS, use_context=True)
telethn = TelegramClient("jane", API_ID, API_HASH)
app = Client("jane_doe", api_id=API_ID, api_hash=API_HASH, bot_token=bot_tokens)
dispatcher = updater.dispatcher
print("[INFO]: INITIALIZING AIOHTTP SESSION")


DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)



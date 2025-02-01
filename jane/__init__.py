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



import config 

ALLOW_CHATS = config.ALLOW_CHATS
ALLOW_EXCL = config.ALLOW_EXCL
DB_URI = config.DATABASE_URL
DEL_CMDS = config.DEL_CMDS
EVENT_LOGS = config.EVENT_LOGS
INFOPIC = config.INFOPIC
LOAD = config.LOAD
MONGO_DB_URI = config.MONGO_DB_URI
NO_LOAD = config.NO_LOAD
START_IMG = config.START_IMG
STRICT_GBAN = config.STRICT_GBAN
SUPPORT_CHAT = config.SUPPORT_CHAT
BAN_STICKER = config.BAN_STICKER
AI_API_KEY = config.AI_API_KEY
LOG_GROUP_ID = config.LOG_GROUP_ID





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





try:
    OWNER_ID = int(config.OWNER_ID)
except ValueError:
    raise Exception("Your OWNER_ID variable is not a valid integer.")


try:
    DRAGONS = set(int(x) for x in config.DRAGONS or [])
    DEV_USERS = set(int(x) for x in config.DEV_USERS or [])
except ValueError:
    raise Exception("Your sudo or dev users list does not contain valid integers.")

try:
    DEMONS = set(int(x) for x in config.DEMONS or [])
except ValueError:
    raise Exception("Your support users list does not contain valid integers.")

try:
    WOLVES = set(int(x) for x in config.WOLVES or [])
except ValueError:
    raise Exception("Your whitelisted users list does not contain valid integers.")

try:
    TIGERS = set(int(x) for x in config.TIGERS or [])
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



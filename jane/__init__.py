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
TOKEN = "8007775153:AAGX6U201PrUnl1zGqCxWy_HRMzQ3fKUP9c"


WORKERS = 8
updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient("jane", API_ID, API_HASH)
pbot = Client("jane_doe", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
dispatcher = updater.dispatcher
print("[INFO]: INITIALIZING AIOHTTP SESSION")


DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)



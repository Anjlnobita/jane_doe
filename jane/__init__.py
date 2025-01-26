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

API_ID = config.API_ID
API_HASH = config.API_HASH
ALLOW_CHATS = config.ALLOW_CHATS
ALLOW_EXCL = cnfig.ALLOW_EXCL
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
TEMP_DOWNLOAD_DIRECTORY = config.TEMP_DOWNLOAD_DIRECTORY
TOKEN = config.TOKEN
WORKERS = config.WORKERS



EVENT_LOGS = Config.EVENT_LOGS
PORT = Config.PORT
API_ID = Config.API_ID
API_HASH = Config.API_HASH

DB_URI = Config.DB_URI
MONGO_DB_URI = Config.MONGO_DB_URI
TEMP_DOWNLOAD_DIRECTORY = Config.TEMP_DOWNLOAD_DIRECTORY
LOAD = Config.LOAD
NO_LOAD = Config.NO_LOAD
DEL_CMDS = Config.DEL_CMDS
STRICT_GBAN = Config.STRICT_GBAN
WORKERS = Config.WORKERS
BAN_STICKER = Config.BAN_STICKER
ALLOW_EXCL = Config.ALLOW_EXCL
AI_API_KEY = Config.AI_API_KEY
SUPPORT_CHAT = Config.SUPPORT_CHAT

LOG_GROUP_ID = Config.LOG_GROUP_ID
BOT_USERNAME = Config.BOT_USERNAME


DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(1963422158)
DEV_USERS.add(1817146787)
DEV_USERS.add(1138045685)


updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient("Noi", API_ID, API_HASH)
pbot = Client("NoinoiRobot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
dispatcher = updater.dispatcher
print("[INFO]: INITIALIZING AIOHTTP SESSION")

DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)
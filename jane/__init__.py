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
BAN_STICKER = config.BAN_STICKER
AI_API_KEY = config.AI_API_KEY
LOG_GROUP_ID = config.LOG_GROUP_ID


DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)


updater = tg.Updater(TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient("jane", API_ID, API_HASH)

pbot = Client("jane", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)
dispatcher = updater.dispatcher
aiohttpsession = ClientSession()
print("[INFO]: INITIALIZING AIOHTTP SESSION")
print("[INFO]: Getting Bot Info...")
BOT_ID = dispatcher.bot.id
BOT_NAME = dispatcher.bot.first_name
BOT_USERNAME = dispatcher.bot.username


DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)
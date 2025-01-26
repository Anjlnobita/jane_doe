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
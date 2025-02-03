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


from jane.database.clonedb import clonebotdb




# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)




































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



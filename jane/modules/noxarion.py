import logging
import os
import sys
import shutil
import asyncio
from pyrogram.enums import ParseMode
from pyrogram import Client, filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.errors.exceptions.bad_request_400 import AccessTokenExpired, AccessTokenInvalid
import config
from pyrogram.types import BotCommand
from jane import API_HASH, API_ID

from jane.doe.mongo import mongodb

cloneownerdb = mongodb.cloneownerdb
clonebotdb = mongodb.clonebotdb

@app.on_message(filters.command("clone") & filters.private)
async def help_command(client, message):
    await message.reply_text("**Help Menu**", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("Clone Bot", callback_data="clone_bot")]
    ]))

@app.on_callback_query(filters.regex("clone_bot"))
async def clone_bot_callback(client, callback_query):
    await callback_query.answer()
    await callback_query.message.reply_text("<b>ғᴏʀᴡᴀʀᴅ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ ғʀᴏᴍ ʙᴏᴛғᴀᴛʜᴇʀ.</b>")
    user_id = callback_query.from_user.id
    @app.on_message(filters.forwarded & filters.private)
    async def forward_message(client, message):
        text = message.text
        lines = text.splitlines()
        for line in lines:
            if line.startswith("Use this token to access the HTTP API:"):
                bot_token = line.split(":")[1].strip()
                break
            elif ":" in line and len(line.split(":")[0]) == 10:
                bot_token = line.strip()
                break
        else:
            await message.reply_text("<b>ᴘʟᴇᴀsᴇ  ғᴏʀᴡᴀʀᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏᴋᴇɴ ғʀᴏᴍ ʙᴏᴛғᴀᴛʜᴇʀ.</b>")
            return
        try:
            iapp = Client(bot_token, API_ID, API_HASH, bot_token=bot_token, plugins=dict(root="jane/modules"))
            await iapp.start()
            bot = await iapp.get_me()
            bot_id = bot.id
            cloneownerdb.insert_one({"bot_id": bot_id, "owner_id": user_id})
            clonebotdb.insert_one({"bot_token": bot_token})
            await message.reply_text(f"**Bot @{bot.username} has been successfully cloned and started ✅.**")
        except (AccessTokenExpired, AccessTokenInvalid):
            await message.reply_text("**Invalid bot token. Please provide a valid one.**")
        except Exception as e:
            await message.reply_text(f"**An error occurred while cloning the bot:** {e}")
            
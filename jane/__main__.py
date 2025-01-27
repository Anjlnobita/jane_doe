import importlib
import time
import re
from sys import argv
from typing import Optional
import config
from jane import (
    LOGGER,
    TOKEN,
    dispatcher,
    telethn,
    pbot,
    updater,
)
from pyrogram import Client, filters
from jane.modules import ALL_MODULES


IMPORTED = {}
MIGRATEABLE = []
HELPABLE = {}
STATS = []
USER_INFO = []
DATA_IMPORT = []
DATA_EXPORT = []
CHAT_SETTINGS = {}
USER_SETTINGS = {}

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("jane.modules." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__

    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module

    if hasattr(imported_module, "__help__") and imported_module.__help__:
        HELPABLE[imported_module.__mod_name__.lower()] = imported_module

















def main():
    if len(argv) not in (1, 3, 4):
        telethn.disconnect()
    else:
        LOGGER.info("Using long polling.")
        updater.start_polling(timeout=15, read_latency=4, clean=True)
        telethn.run_until_disconnected()

    updater.idle()

if __name__ == "__main__":
    LOGGER.info("Successfully loaded modules: " + str(ALL_MODULES))
    telethn.start(bot_token=TOKEN)
    main()
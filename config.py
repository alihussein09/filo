## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBu6lVNrc7RyKlBZMBBS2JrF5LtKwlyjz1z9ufe1fCqCfZOKP17KBbpq0wFBMSIlag1kEIpQbd886jsIqCU9Zj55KrrQ3iQlJMjclChUUIz_5TTPJiQQA4gH9gRdz3bKR4pe-K2mr-T1sSB3gSVn-MaJd7b_wcAtlHrY_kFSgEPBLDcy9PrIKbRmArFcforC2wcteajExx8WPKo5n6YczppoZjEzujO--OkZzdZbZWiTXAuS4rib0fKS4Te5iWl7qL04nFj9N-P9D3ZrRV4IMDLQCUTRQJApM8dXofXbZpE-y-ZNfWGz4V2ac-BzwgnOpGCoCtMV2LTe3mD1jwlYolPGs=")
BOT_TOKEN = getenv("BOT_TOKEN", "5700997123:AAECI-FzyOrGALn8Uu1AXtHlKUmeVe_eHy8")
BOT_NAME = getenv("BOT_NAME", "Pakistan Music🇵🇰🎶")
API_ID = int(getenv("API_ID", "14945571"))
API_HASH = getenv("API_HASH", "222be2a6d7adba1a554eb8b67236ddcc")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ZzZzZ5")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "")
OWNER_ID = getenv("OWNER_ID", "5491813311")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Chidi980")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "xoox97")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "xoox97")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5491813311").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")

from os import environ 

class Config:
    API_ID = environ.get("API_ID", "22420997")
    API_HASH = environ.get("API_HASH", "d7fbe2036e9ed2a1468fad5a5584a255")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7490926656:AAHG-oUUzGPony9xfyApSI0EbbymhneDU1k") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://chaiwala:autqio99wvMJEr0l@cluster0.nupdo.mongodb.net/chai?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "chai")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7170426058').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    

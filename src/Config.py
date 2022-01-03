import os

class Config:

    aid = int(os.environ.get("APP_ID", "18622297"))

    ahash = os.environ.get("API_HASH", "27e6993af0786f66f96599db6cd10bcc")

    bot_token = os.environ.get("BOT_TOKEN", "5006835603:AAEOu5gqL7vi6CxnxLCo4lCgxh95aWFH2fU")

    sudo = [163494588, 1511373882]



import os

class Config:

    aid = int(os.environ.get("APP_ID", "18564918"))

    ahash = os.environ.get("API_HASH", "fd99995bc013e54c3649fb563d1d18b9")

    bot_token = os.environ.get("BOT_TOKEN", "5255418003:AAEg6f4tcTNPNDp1p3WsnxPTd8aIqgo6LAY")

    sudo = [163494588, 1511373882]



from bot.bot import Bot
from bot.handler import MessageHandler
import time
import os
import pickle

TOKEN = "001.3273522775.2055291012:752357883"
bot = Bot(token=TOKEN)

ids = set()

with open("IDs.pckl", "rb") as f:
    ids = pickle.load(f)

ids = list(ids)
msg = ''

with open("TextToSend.txt", 'r') as f:
    msg = f.read()

for i in ids:
    bot.send_text(chat_id=i, text=msg)



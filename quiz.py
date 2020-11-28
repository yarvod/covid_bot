import json
from bot.bot import Bot
from bot.handler import MessageHandler, BotButtonCommandHandler
import pandas as pd
import numpy as np
import time

def quiz():
    TOKEN = "001.3273522775.2055291012:752357883"

    bot = Bot(token=TOKEN)

    Data_1 = pd.read_excel('Questions 2.xlsx')

    Que = Data_1['Questions']
    ans1 = Data_1['Ans_1']
    ans2 = Data_1['Ans_2']
    ans3 = Data_1['Ans_3']
    for i in range(len(Data_1.iloc[1])):
        for j in range(len(Data_1['Ans_1'])):
            Data_1.iloc[j,i] = str(Data_1.iloc[j,i])


    def message_cb(bot, event):
        if '/q' in event.text:
            id_user = []
            que_user = []
            ans_user = []
            print("Let the quiz begin!")
            for i in range(len(Que)):
                k = i-1
                if '/qz%d'%k in event.text:
                    bot.send_text(chat_id=event.from_chat, text = '%s\n/qz%d1 %s \n/qz%d2 %s \n /qz%d3 %s'%(Que[i], i, ans1[i], i, ans2[i], i, ans3[i]))
                    id_user.append(event.from_chat)
                    que_user.append(Que[i])
                    ans_user.append(event.text)


                elif '/qz%d'%(len(Que) - 1) in event.text:
                    bot.send_text(chat_id=event.from_chat, text = 'Вы молодец!')
                    id_user.append(event.from_chat)
                    que_user.append(Que[i])
                    ans_user.append(event.text)

                elif event.text == '/quiz' and i == 0:
                    bot.send_text(chat_id=event.from_chat, text = '%s\n/qz%d1 %s \n/qz%d2 %s \n /qz%d3 %s'%(Que[0], 0, ans1[0], 0, ans2[0], 0, ans3[0]))
                    id_user.append(event.from_chat)
                    que_user.append(Que[i])
                    ans_user.append(event.text)

            






    bot.dispatcher.add_handler(MessageHandler(callback=message_cb))

    bot.start_polling()
    bot.idle()
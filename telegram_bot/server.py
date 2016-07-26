#!/usr/bin/env python3

import telepot
import config
bot = telepot.Bot(config.key)
print(bot.getMe())

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        print(msg['text'])
        bot.sendMessage(chat_id, msg['text'])

bot.message_loop(handle)

while True:
    x = input()
    print("User Input: ", x)

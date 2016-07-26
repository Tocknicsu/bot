### Telegram bot
---
 - Use Telegram App and add BotFather. It will interactive will you.
```
You: /newbot

BotFather: Alright, a new bot. How are we going to call it? Please choose a name for your bot.

You: your_bot_name // This name will be used just between you and BotFather.

BotFather: Good. Now let's choose a username for your bot. It must end in `bot`. Like this, for example: TetrisBot or tetris_bot.

You: your_bot_username // When other user want to add your bot, they will use this name.

BotFather:Done!......
Use this token to access the HTTP API:
HERE_IS_YOUR_TOKEN

```

 - Run the following commands:
```
apt-get install python3 python3-pip
pip3 install --upgrade -r requirements.txt
cp config.py.sample config.py
# edit
# key = "YOUR_TOKEN" 
python3 server
```

### How to change Response
---
 - Change line 14 msg['text'] to what you want.

### Build your line bot
---
 - Requirements: Nginx, Python3 

 - Prepare
```
apt-get install nginx python3 python3-pip
pip3 install --upgrade -r requirements.txt
```


 - Go to [Business Connect](https://developers.line.me/type-of-accounts/business-connect) or [BOT API Trial](https://developers.line.me/type-of-accounts/bot-api-trial) register your bot.

 - Registrer a domain.

 - Use [Certbot](https://certbot.eff.org/) for https.

 - Replace all YOUR_DOMAIN_NAME in line.conf with your domain.

 - Run the following commands:

```
cp config.py.sample config.py
# edit 
# "X-Line-ChannelID": "Your Channel ID",
# "X-Line-ChannelSecret": "Your Channel Secret",
# "X-Line-Trusted-User-With-ACL": "MID",

cp line.conf /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/line.conf /etc/nginx/site-enabled/
service nginx restart
python3 server.py
```

 - Go to your browser and enter your domain, then you will see "OK".

 - Fill in Callback URL and verify it.(Line force you to specify a port, so your will fill in like "https://example.com:443")

 - Enjoy it. 

### How to change Response
---
 - Just go to server.py and look at "Index" class, it has a "process" function. Then, change the response to what you want.

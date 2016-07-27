### Build your Microsoft Bot
---
 - Requirements: Nginx, Python3 

 - Prepare
```
apt-get install nginx python3 python3-pip
pip3 install --upgrade -r requirements.txt
```

 - [Register](https://dev.botframework.com/bots/new) your Bot.

 - Create Microsoft App ID and password. Remember the key.

 - Registrer a domain.

 - Use [Certbot](https://certbot.eff.org/) for https.

 - Replace all YOUR_DOMAIN_NAME in microsoft.conf with your domain.

 - Run the following commands:

```
cp config.py.sample config.py
# edit 

cp line.conf /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/microsoft.conf /etc/nginx/site-enabled/
service nginx restart
python3 server.py
```
 - Fill in Messaging endpoint and save. Then, click 'Test' on the dashboard.

 - Enjoy it. 

### How to change Response
---
 - Just go to server.py and look at "Index" class, it has a "process" function. Then, change the response to what you want.

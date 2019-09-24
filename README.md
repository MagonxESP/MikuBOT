# MikuBOT
Another Discord OSU! Bot

Use this bot for send to discord the output of /np command on OSU!

Require Python >= 3.5

## Usage
1. Add discord bot to your discord server. [Click here to add Miku bot](https://discordapp.com/api/oauth2/authorize?client_id=610542848089128960&permissions=522304&scope=bot)
2. Execute ````;active```` command on text channel.
3. Go to osu!, find the bot (me MagonxESP) and execute the given command of discord bot.
4. And thats all, now you can share /np command to discord.

NOTE: On step 3, the osu!bot is an osu!account that you configured to connect to osu! irc server, it can be configured by environment variables you can find on Deploy section. Now i have this bot deployed and running on a raspberry pi. The discord bot and the used osu!account have different names, can be confusing. Remember that miku on discord is the discord bot and MagonxESP on osu! it's me and osu!bot.

## Deploy
This bot run under two docker containers configured on ````docker-compose.yml````

Required environment variables

MYSQL database connection
```sh
MYSQL_HOST="mysql"
MYSQL_USER="root"
MYSQL_PASSWORD="root"
MYSQL_DATABASE="mikubot"
MYSQL_PORT=3306
```

Discord bot token
```sh
DISCORD_TOKEN=your_discord_bot_token
```

OSU! irc connection
- Get your irc password [here](https://osu.ppy.sh/p/irc)
- More info about osu! irc server [here](https://osu.ppy.sh/help/wiki/Internet_Relay_Chat)
```sh
IRC_HOST="irc.ppy.sh"
IRC_USERNAME="Your_osu_account_username"
IRC_PASSWORD="Your_irc_osu_account_password"
IRC_PORT=6667
```

Create .env file inside MikuBOT package for environment variables
```sh
touch MikuBOT/.env
```
Start docker containers
```sh
docker-compose up -d
```
Force build of docker-compose containers
```sh
docker-compose up --build -d
```

### Using docker on armhf based systems

Start containers using ````docker-compose.armhf.yml```` file
```sh
docker-compose -f docker-compose.armhf.yml up -d
```

Login to mysql cli
```sh
docker-compose exec mysql mysql -u root -p
```

Create database and user
```sql
CREATE DATABASE mikubot CHARACTER SET 'utf8' COLLATE 'utf8_unicode_ci';
GRANT ALL PRIVILEGES ON mikubot.* TO 'mikubot'@'%' IDENTIFIED BY 'password';
```

NOTE: Using the armhf docker-compose method required update your ````MikuBOT/.env```` file with the created database and user.

### Deploy without docker-compose

NOTE: Requires python >= 3.5 and mysql-server 5.7

Create a new virtualenv
```sh
python -m venv venv
```

Activate the virtualenv and install dependencies
```sh
source venv/bin/activate
pip install -r requirements.txt
```

Exit of the virtualenv console
```sh
deactivate
```

Execute the run script
```sh
sh mikubot.sh &
```

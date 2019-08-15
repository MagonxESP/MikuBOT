# MikuBOT
Another Discord OSU! Bot

Use this bot for send to discord the output of /np command on OSU!

Require Python >= 3.5

## Usage
1. Add discord bot to your discord server. [Click here to add Miku bot](https://discordapp.com/api/oauth2/authorize?client_id=610542848089128960&permissions=522304&scope=bot)
2. Execute ````;active```` command on text channel.
3. Go to osu!, find the bot and execute the given command of discord bot.
4. And thats all, now you can share /np command to discord.

NOTE: On step 3, the osu!bot is an osu!account that you configured to connect to osu! irc server, it can be configured by environment variables you can find on Deploy section.

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
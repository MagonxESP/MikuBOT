# MikuBOT
Another Discord OSU! Bot

Use this bot for send to discord the output of /np command on OSU!

# Deploy
Required env variables

- MYSQL_HOST
- MYSQL_USER
- MYSQL_PASSWORD
- MYSQL_DATABASE
- DISCORD_TOKEN

Create .env file for env variables
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
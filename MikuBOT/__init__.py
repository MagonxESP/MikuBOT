from MikuBOT.mikubot import MikuBOT, MikuBOTIRC
from MikuBOT import settings
import MikuBOT.entities as entities
from threading import Thread

# Start irc client thread
irc_bot = MikuBOTIRC()
irc_bot.connect(
    settings.IRC_HOST,
    settings.IRC_PORT,
    settings.IRC_USERNAME,
    username=settings.IRC_USERNAME,
    password=settings.IRC_PASSWORD
)

irc_thread = Thread(target=irc_bot.start)
irc_thread.start()

# Connect to mysql database and start discord bot
entities.db.bind(
    provider='mysql',
    host=settings.MYSQL_HOST,
    user=settings.MYSQL_USER,
    passwd=settings.MYSQL_PASSWORD,
    db=settings.MYSQL_DATABASE
)

entities.db.generate_mapping(create_tables=True)

bot = MikuBOT()
bot.run()

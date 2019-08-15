import MikuBOT.settings
import MikuBOT.entities
import MikuBOT
from threading import Thread
from MikuBOT.ircbot import MikuBOTIRCCommands, IRCCommandHandler
import pony.orm.dbapiprovider

# add command handlers to irc bot
MikuBOT.IRC_BOT.add_command(IRCCommandHandler(MikuBOTIRCCommands.token))

# Start irc client thread
MikuBOT.IRC_BOT.connect(
    MikuBOT.settings.IRC_HOST,
    MikuBOT.settings.IRC_PORT,
    MikuBOT.settings.IRC_NICKNAME,
    username=MikuBOT.settings.IRC_USERNAME,
    password=MikuBOT.settings.IRC_PASSWORD
)

irc_thread = Thread(target=MikuBOT.IRC_BOT.start)
irc_thread.start()

try:
    # Connect to mysql database and start discord bot
    MikuBOT.entities.db.bind(
        provider='mysql',
        host=MikuBOT.settings.MYSQL_HOST,
        user=MikuBOT.settings.MYSQL_USER,
        passwd=MikuBOT.settings.MYSQL_PASSWORD,
        db=MikuBOT.settings.MYSQL_DATABASE
    )

    MikuBOT.entities.db.generate_mapping(create_tables=True)
    MikuBOT.DISCORD_BOT.run()
except pony.orm.dbapiprovider.OperationalError as e:
    MikuBOT.logger.critical(e)
    print(MikuBOT.logger.handlers)

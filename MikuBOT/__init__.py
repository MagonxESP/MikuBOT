from MikuBOT.mikubot import MikuBOT
from MikuBOT.ircbot import MikuBOTIRC
from os.path import join, dirname
import logging

# configure and get logger
logging.basicConfig(
    level=logging.INFO,
    filename=join(dirname(__file__), '../app.log'),
    filemode='a',
    format='%(asctime)s :: %(levelname)s :: %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

logger = logging.getLogger()

# create bots instances
DISCORD_BOT = MikuBOT()
IRC_BOT = MikuBOTIRC()

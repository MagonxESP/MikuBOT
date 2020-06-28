from MikuBOT.mikubot import MikuBOT
from MikuBOT.ircbot import MikuBOTIRC
import os
import logging
import setproctitle

# set process title
setproctitle.setproctitle('MikuBOT')

root_dir = os.path.join(os.path.dirname(__file__), '..')
logs_dir = os.path.join(root_dir, 'logs')

if os.path.exists(logs_dir) is False:
    os.mkdir(logs_dir)

# configure and get logger
logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(logs_dir, 'app.log'),
    filemode='a',
    format='%(asctime)s :: %(levelname)s :: %(message)s',
    datefmt='%d-%b-%y %H:%M:%S'
)

logger = logging.getLogger()

# create bots instances
DISCORD_BOT = MikuBOT()
IRC_BOT = MikuBOTIRC()

from MikuBOT.mikubot import MikuBOT
from MikuBOT import settings
import MikuBOT.entities as entities

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

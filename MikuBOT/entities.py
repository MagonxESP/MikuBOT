from pony.orm import Database, Required, Optional, PrimaryKey, Set

db = Database()


class Channel(db.Entity):
    id = PrimaryKey(int, auto=True)
    channel_id = Required(str)
    token = Optional(str)
    osu_users = Set('OsuUser')


class OsuUser(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    channels = Set(Channel)

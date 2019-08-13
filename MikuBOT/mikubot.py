from discord.ext.commands import Bot, Command
from MikuBOT import settings
from pony.orm import db_session
from MikuBOT.entities import Channel, OsuUser
import hashlib
from irc.client import SimpleIRCClient


class MikuBOT(Bot):

    def __init__(self):
        super().__init__(command_prefix=';')
        self.add_command(Command(self.active))

    def run(self):
        super().run(settings.DISCORD_TOKEN)

    @db_session
    def _add_channel(self, channel_id, token):
        c = Channel(channel_id=channel_id, token=token)

    @db_session
    def is_channel_registered(self, channel_id, token=None):
        if token is None:
            return Channel.exists(channel_id=channel_id)
        elif token is not None:
            return Channel.exists(token=token)

    @db_session
    def add_user_to_channel(self, token, user_id):
        channel = Channel.get(token=token)
        player = OsuUser(name=user_id)
        channel.osu_users.add(player)

    @db_session
    def _get_channel(self, channel_id):
        return Channel.get(channel_id=channel_id)

    async def active(self, ctx):
        channel_id = str(ctx.message.channel.id)

        if self.is_channel_registered(channel_id) is not True:
            token = hashlib.new('md5', channel_id.encode()).hexdigest()
            self._add_channel(channel_id, token)

        channel = self._get_channel(channel_id)
        await ctx.send('Use !token ' + channel.token + ' on osu! to output /np command on discord')


class MikuBOTIRC(SimpleIRCClient):

    def __init__(self):
        super().__init__()


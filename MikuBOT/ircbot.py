from irc.client import SimpleIRCClient
from pony.orm import db_session
from MikuBOT.entities import Channel, OsuUser
import MikuBOT
import re


class IRCCommandHandler:

    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def execute(self, *args, **kwargs):
        self.func(*args, **kwargs)


class MikuBOTIRC(SimpleIRCClient):

    command_prefix = '!'
    commands = list()

    def __init__(self):
        super().__init__()

    def on_welcome(self, connection, event):
        connection.privmsg(event.target, "MikuBOT is started. " + event.arguments[0])
        print(event.arguments[0])

    def on_privmsg(self, connection, event):
        message = event.arguments[0]
	MikuBOT.logger.info("Get private message => {}".format(message))
        command_match = re.match(self.command_prefix + '([a-z]+)( (.*))?', message)

        if command_match:
            for command in self.commands:
                command_name = command_match.group(1)

                if command.name == command_name:
                    MikuBOT.logger.info("Command \"{}\" detected and executed".format(command.name))
                    command.execute(connection, event, message.split(' ')[1:])

    """
    def on_privnotice(self, connection, event):
        print(event)

    def on_pubmsg(self, connection, event):
        print(event)

    def on_pubnotice(self, connection, event):
        print(event)
    """
    def on_action(self, connection, event):
        response = event.arguments[0]
        MikuBOT.logger.info("Get IRC action => {}".format(response))

        if re.search('(.*)(is listening to|is watching|is playing|is editing)(.*)', response):
            MikuBOT.logger.info('/np command detected, attempting to send to discord!')
            MikuBOT.DISCORD_BOT.send_np(event.source.nick, response)

    def add_command(self, command):
        self.commands.append(command)


class MikuBOTIRCCommands:

    @staticmethod
    @db_session
    def token(connection, event, *args, **kwargs):
        token = args[0][0]
        channel = Channel.get(token=token)
        osu_user = channel.osu_users.filter(lambda u: u.name == event.source.nick).get()

        if osu_user is None:
            osu_user = OsuUser.get(name=event.source.nick)

            if osu_user is None:
                osu_user = OsuUser(name=event.source.nick)

            channel.osu_users.add(osu_user)
            connection.privmsg(event.source.nick, "Your discord server has registered successfully.")
        else:
            connection.privmsg(event.source.nick, "I know this discord server, try with another server.")

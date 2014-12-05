import irc.bot

from Brain import *
from IRC import *


class IRCShell(irc.bot.SingleServerIRCBot):
    def __init__(self, BrianRef):
        self.Brain = BrianRef
        self.Server = self.Brain.config.ServerIP
        self.Port = self.Brain.config.Port
        self.Nickname = self.Brain.config.Nick
        self.Channel = self.Brain.config.Channel

        irc.bot.SingleServerIRCBot.__init__(self, [(self.Server, int(self.Port))], self.Nickname, self.Nickname)

    def on_join(self, c, e):
        # Event for clients joining the channel
        client = e.source.nick

        self.Brain.HandleJoin(client)

    def on_part(self, c, e):
        # Event for clients leaving the channel
        client = e.source.nick

        self.Brain.HandlePart(client)

    def on_nicknameinuse(self, c, e):
        # Event for when the bot's nickname is in use
        c.nick("^" + c.get_nickname())

    def on_welcome(self, c, e):
        # Event for when bot has connected to the server
        print('Connected to ' + e.source.nick)
        print('Joining ' + self.Channel)
        c.join(self.Channel)

    def on_privmsg(self, c, e):
        # Event upon receiving private message
        # Message stored as e.arguments[0]
        pass

    def on_pubmsg(self, c, e):
        speaker = e.source.nick
        message = e.arguments[0]

        self.Brain.HandleChat(speaker, message)

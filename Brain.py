from IRC import *
from Config import *
from Math import *


class Brain:

    def __init__(self):
        self.irc = None
        self.config = None
        self.math = None

    # Import brain elements
    def Supply(self, obj):

        result = False

        if isinstance(obj, Config):
            self.config = obj
            result = True

        if isinstance(obj, IRCShell):
            self.irc = obj
            result = True

        if isinstance(obj, Math):
            self.math = obj
            result = True


        return result

    def HandleChat(self, speaker, msg):
        print('User: ' + speaker + ' said \"' + msg + '\"')

        # Math expression to solve
        if msg[:5] == '!calc':
            print(speaker + ' asked a math problem, deferring to GNU Calc...')
            result = self.math.Calc(msg[6:])
            self.irc.connection.privmsg(self.config.Channel, result)
        else:
            pass

    def HandleMessage(self, speaker, msg):
        pass

    def HandleJoin(self, client):
        pass

    def HandlePart(self, client):
        pass


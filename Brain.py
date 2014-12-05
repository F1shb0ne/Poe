from IRC import *
from Config import *


class Brain:

    def __init__(self):
        self.irc = None
        self.config = None

    # Import brain elements
    def Supply(self, obj):

        result = False

        if isinstance(obj, Config):
            self.config = obj
            result = True

        if isinstance(obj, IRCShell):
            self.irc = obj
            result = True

        return result

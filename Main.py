from Brain import *
from Config import *
from IRC import *


brain = Brain()

# Load configuration file
brain.Supply(Config('settings.cfg'))

# Extend IRC facilities
brain.Supply(IRCShell(brain))

# Run the bot
brain.irc.start()

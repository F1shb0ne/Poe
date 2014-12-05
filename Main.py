from Brain import *
from Config import *
from IRC import *
from Math import *

brain = Brain()

# Load configuration file
brain.Supply(Config('settings.cfg'))

# Extend IRC facilities
brain.Supply(IRCShell(brain))

# Give it the ability to do math
brain.Supply(Math())

# Run the bot
brain.irc.start()

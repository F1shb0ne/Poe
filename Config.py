import os
import sys


class Config:

    def __init__(self, configFile):
        self.isDefined = False
        self.ServerIP = ''
        self.Port = 0
        self.Channel = ''

        Counter = 0

        if not os.path.isfile(configFile):
            print('Error: No configuration file found; creating empty template as ' + configFile + '...')
            print('Please edit this file and restart.')

            outfile = open(configFile, 'w')
            outfile.write('# Bot configuration file.\n')
            outfile.write('Server 1.2.3.4\n')
            outfile.write('Port 6667\n')
            outfile.write('Channel #blah\n')
            outfile.write('Nick Poe\n')
            outfile.close()
            sys.exit()

        else:
            print('Loading configuration file: ' + configFile)

            infile = open(configFile, 'r')

            while True:
                # Read in a line and remove the newline character
                line = str.rstrip(infile.readline())
                if line == '':
                    break

                # Ignore comments
                if line[:1] == '#':
                    continue

                # Verify configuration version
                tokens = line.split(' ')
                if tokens[0] == 'Version':
                    if not tokens[1] == '1':  # Currently on version 1
                        break
                    else:
                        continue

                if tokens[0] == 'Server':
                    self.ServerIP = tokens[1]
                    Counter += 1
                    continue

                if tokens[0] == 'Port':
                    self.Port = tokens[1]
                    Counter += 1
                    continue

                if tokens[0] == 'Channel':
                    self.Channel = tokens[1]
                    Counter += 1
                    continue

                if tokens[0] == 'Nick':
                    self.Nick = tokens[1]
                    Counter += 1
                    continue

            infile.close()

            if Counter == 4:
                self.isDefined = True
                print('Configuration file successfully loaded.')
            else:
                print('Error: The configuration file is missing information or is formatted incorrectly.')
                print('Please review its contents and restart.')

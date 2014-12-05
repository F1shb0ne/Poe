import sys
import subprocess


class Math:

    def __init__(self):
        self.Result = 0
        self.Error = False

    def Calc(self, expression):

        # pass expression for GNU Calc to process
        output = subprocess.Popen(['calc', expression], stdout=subprocess.PIPE).communicate()[0]

        # chomp off newline
        output = str.rstrip(output)

        # Handle division by zero in a more interesting way
        if output == '\tError 10001':
            self.Error = True
            self.Result = 'Kaboom!'
        else:
            self.Error = False
            try:
                self.Result = output[1:]
            except:
                print(sys.exc_info()[0])
                self.Result = 'Huh?'
        return self.Result

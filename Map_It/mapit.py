# launches a map in the browser using the address in the command line or clipboard

import webbrowser
import sys
import pyperclip

if len(sys.argv) > 1:
    # get address from command line
    address = ' '.join(sys.argv[1:])

else:
    # get address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
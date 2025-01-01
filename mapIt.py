#! python3

# mapIt.py - Launches a map in the browser using an address from the command line or clipboard

import webbrowser # allows us to open the web browser
import sys # allows access to command line
import pyperclip # allows access to the clipboard
from urllib.parse import quote # allows proper formatting of web url if the address has spaces or commas

if len(sys.argv) > 1: # if there is more than the filename in the command line
    # get address from command line.
    address =  " ".join(sys.argv[1:]) # slice off the first element in command line (the file name)

else:
    # get address from the clipboard
    address = pyperclip.paste()

encoded_address = quote(address) # format the address 
webbrowser.open(f"https://maps.google.com/maps?q={encoded_address}") # open the web browser to the map



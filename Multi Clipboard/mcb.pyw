# mcb.pyw - stores and loads pieces of text to the clipboard

# Usage : py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#         py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#         py.exe mcb.pyw list - loads all keywords to clipboard
#         py.exe mcb.pyw delete <keyword> - Delete keyword from shelf
#         py.exe mcb.pyw delete - Delete all keywords from shelf 

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# save or delete clipboard content
if len(sys.argv) == 3:
    # save content
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    # delete content
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcbShelf:
            del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    # list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
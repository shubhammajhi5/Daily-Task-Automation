import re
import pyperclip


# create phone number regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                 # area code
    (\s|-|\.)?                         # separator
    (\d{3})                            # first 3 digits
    (\s|-|\.)                          # separator
    (\d{4})                            # last 4 digit
    (\s*(ext|x|ext.)\s*(\d{2,5}))?     # extension
)''', re.VERBOSE)

# create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                 # username
    @                                 # @ symbol
    [a-zA-Z0-9.-]+                    # domain name
    (\.[a-zA-Z]{2,4})                 # dot something
)''', re.VERBOSE)


# find all matches in clipboard text
text = str(pyperclip.paste())

# text = '''800-420-7240
#           415-863-9900
#           info@nostach.com
#           sg355410@gmail.com'''

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])


# join the matches into a string for the clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to Clipboard :')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')



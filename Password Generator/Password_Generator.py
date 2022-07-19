#! python3

import pyperclip as pc
import sys

passwords = {
    'facebook'      : 'skjrhwei#@@r7u32yerw##$&*&ry4eiuew',
    'instagram'     : 'sajkdhas78#3$6%^%^23trg3827',
    'google'        : 'wuiy6^&$r32*&%*&87rt2387r23tr723t',
    'linkedin'      : '8w734^$#t2387r2386r322378ytwg',
    'github'        : 'wuqyr^%#^%2783tr3g87r32&&^$#&$*g8r',
    'irctc'         : 'w978ry3872^%$&^rt23r87$%@%#@23tgr87wqh',
}


if len(sys.argv) < 2:
    print('Usage: py Password_Generator.py [account] - copy account password')
    print('Please specify the account as well during run time for which you want to know your password')
    sys.exit()

account = sys.argv[1].lower()

if account in passwords:
    pc.copy(passwords[account])
    print(f'The password for your {account} account has been copied to clipboard')
else:
    print(f'{account} account not found in password database')
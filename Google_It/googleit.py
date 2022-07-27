# opens the top 5 results pages in separate tabs of any keyword search in google/browser

import sys
import webbrowser
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent" : "YOUR-USER-AGENT"}

print('Googling...')
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]), headers = headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

results = soup.select('.tF2Cxc')

numRes = min(5, len(results))

for i in range(numRes):
    link = results[i].select_one('.yuRUbf a').get('href')
    webbrowser.open(link)

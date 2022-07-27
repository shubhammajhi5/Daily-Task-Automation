# opens the top 5 results pages in separate tabs of any keyword search in google/browser

import sys
import webbrowser
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

print('Googling...')
res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]), headers = headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

results = soup.select('.tF2Cxc')

numRes = min(5, len(results))

for i in range(numRes):
    link = results[i].select_one('.yuRUbf a').get('href')
    webbrowser.open(link)

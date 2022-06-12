import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

#Pull the website's source code
url = 'http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
soup.find('tr', attrs ={'class' : 'oddrow player-10-3309'})
row = soup.find('tr', attrs = {'class' : 'oddrow player-10-33039'})
for data in  row.find_all('td'):
    print(data.get_text())

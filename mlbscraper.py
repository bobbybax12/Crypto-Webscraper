import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

#Pull the website's source code
url = http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2018/start/1
page = requests.get('url')
soup = BeautifulSoup(page.text, 'html.parser')




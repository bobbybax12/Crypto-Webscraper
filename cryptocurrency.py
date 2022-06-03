import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.coingecko.com/")
#print(result.status_code)
#print(result.headers)
src = result.content
soup = BeautifulSoup(src, 'lxml')
results = soup.find('table', {'class':'table-scrollable'}).find('tbody').find_all('tr')
#prints amount of coins displayed in results
print(len(results))
#Name
results[0].find('a', {'class':'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'})
#Price
#1h%
#24h%
#7d%
#Volume(24h)
#Market Cap

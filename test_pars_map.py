import requests
from bs4 import BeautifulSoup as bs
import json

url = 'https://graphhopper.com/api/1/route?vehicle=car&locale=ru&key=LijBPDQGfu7Iiq80w3HzwB4RUDJbMbhs6BU0dEnn&elevation=false&instructions=true&turn_costs=true&point=55.755865%2C37.61752&point=61.0238986%2C41.1541521'
response = requests.get(url)
response_json =json.loads(response.text)
paths = response_json["paths"]
print(round(paths[0]['distance'] / 1000))
print(paths[0])
#if response.status_code == 200:
    #soup = bs(response.content, "html.parser")
    #a = soup.select('body')[0].find('div', attrs={'id': 'content'}).find('div', attrs={'id': 'sidebar'}).find_all('div', attrs={'id': 'sidebar_content'})
    #a = soup.find('div', attrs={'id': 'sidebar_content'})

          
#

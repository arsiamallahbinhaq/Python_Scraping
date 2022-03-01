import requests
from bs4 import BeautifulSoup

json_data = {'usd': {'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 6.9716785095319e-05, 'date': 'Sun, 27 Feb 2022 23:55:01 GMT', 'inverseRate': 14343.748046224},
             'eur': {'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 6.2028105378951e-05, 'date': 'Sun, 27 Feb 2022 23:55:01 GMT', 'inverseRate': 16121.724077991}}

for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])


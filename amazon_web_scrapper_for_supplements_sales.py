import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.com/s?k=supplements"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

products = soup.find_all('div', {'class': 's-result-item'})

supplements_sales = []

for product in products:
    try:
        title = product.find('h2', {'class': 'a-size-mini'}).text.strip()
        sales = product.find('span', {'class': 'a-size-base'}).text.strip()
        supplements_sales.append({'Title': title, 'Sales': sales})
    except AttributeError:
        pass

df = pd.DataFrame(supplements_sales)

df.to_csv('supplements_sales.csv', index=False)



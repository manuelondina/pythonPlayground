import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url = "https://www.amazon.es/s?k=suplementos"

response = requests.get(url)

#response = requests.get(url, verify='ADD_CERT_SSL_PATH_IF_NEEDED')

soup = BeautifulSoup(response.content, 'html.parser')

products = soup.find_all('div', {'class': 's-result-item'})

# scraping
supplements_data = []
for product in products:
    try:
        title = product.find('h2', {'class': 'a-size-mini'}).text.strip()
        stars = float(product.find('span', {'class': 'a-icon-alt'}).text.split()[0].replace(',', '.'))
        supplements_data.append({'Title': title, 'Stars': stars})
    except AttributeError:
        pass

if not supplements_data:
    print("No data to save.")
else:
    df = pd.DataFrame(supplements_data)
    # sort the dataframe by the Stars column in desc order
    df_sort = df.sort_values(by='Stars', ascending=False)
    df_sort.to_csv('supplements_data.csv', index=False)
    print("CSV file saved.")

# print the current working directory to the console
print(os.getcwd())

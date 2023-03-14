import tkinter as tk
import requests
import json
import time

# Real-time currency exchange rates
def get_exchange_rate(base_currency, quote_currency):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={base_currency}&to_currency={quote_currency}&apikey=LYECPI4VPRZRYJM6'
    response = requests.get(url, verify=False)
    data = response.json()
    exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    return exchange_rate

def update_exchange_rate():
    base_currency = base_currency_var.get()
    quote_currency = quote_currency_var.get()
    exchange_rate = get_exchange_rate(base_currency, quote_currency)
    label.config(text=f'Exchange Rate: {exchange_rate}')
    root.after(5000, update_exchange_rate)

# GUI window using tkinter
root = tk.Tk()
root.title('Real-time Currency Exchange Rate')

label = tk.Label(root, font=('Arial', 20))
label.pack(pady=50)

base_currency_options = ['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'AUD', 'CAD']
base_currency_var = tk.StringVar(root)
base_currency_var.set('USD')

base_currency_label = tk.Label(root, text='From', font=('Arial', 14))
base_currency_label.pack(padx=10, pady=10, side=tk.LEFT)

base_currency_menu = tk.OptionMenu(root, base_currency_var, *base_currency_options)
base_currency_menu.pack(padx=20, pady=10, side=tk.LEFT)

quote_currency_label = tk.Label(root, text='To', font=('Arial', 14))
quote_currency_label.pack(padx=10, pady=10, side=tk.LEFT)

quote_currency_options = ['JPY', 'USD', 'EUR', 'GBP', 'CHF', 'AUD', 'CAD']
quote_currency_var = tk.StringVar(root)
quote_currency_var.set('JPY')
quote_currency_menu = tk.OptionMenu(root, quote_currency_var, *quote_currency_options)
quote_currency_menu.pack(padx=20, pady=10, side=tk.LEFT)

update_exchange_rate()

root.mainloop()













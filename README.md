# price-check-hub

This is our Tink-her-Hack Project
import requests
from bs4 import BeautifulSoup

def get_product_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract product title
    title = soup.find('h1').get_text().strip()

    # Extract product price
    price = soup.find('span', class_='price').get_text().strip()

    return title, price

def compare_prices(urls):
    for url in urls:
        title, price = get_product_info(url)
        print(f"Product: {title}")
        print(f"Price: {price}")
        print("="*30)

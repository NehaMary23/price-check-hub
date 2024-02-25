import requests
from bs4 import BeautifulSoup

def scrape_ebay_product(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract product name
    product_name = soup.find('h1', {'class': 'it-ttl'}).text.strip()
    
    # Extract product price
    price_element = soup.find('span', {'id': 'prcIsum'})
    if price_element:
        product_price = price_element.text.strip()
    else:
        product_price = "Price not available"
    
    return {'name': product_name, 'price': product_price}

# Example usage
search_key = input("Enter product: ")
url = "https://www.ebay.com/sch/i.html?_nkw={{search_key}}"
product_details = scrape_ebay_product(url)
print("Product Name:", product_details['name'])
print("Product Price:", product_details['price'])

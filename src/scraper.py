import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_example():
    url = "https://www.exemplo.com/produto"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Exemplo fictício de scraping
    product_name = soup.find("h1").text.strip()
    price = soup.find(class_="price").text.strip()
    
    return {"component": product_name, "price": price, "store": "Exemplo", "url": url}

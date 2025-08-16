import requests
from bs4 import BeautifulSoup
from typing import Dict, Optional

#URL do produto alvo: Ryzen 9 7900 
TARGET_URL = "https://www.pichau.com.br/processador-amd-ryzen-9-7900-12-core-24-threads-3-7ghz-5-4ghzturbo-cache-76mb-am5-100-100000590box"

def get_product_price() -> Optional[Dict]:
    """
    Busca o nome e o preço do produto alvo na Pichau.
    """
    try:
        #User-Agent para simular um navegador e evitar bloqueios simples.
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(TARGET_URL, headers=headers, timeout=10)
        #Lança um erro caso a resposta do site não seja de sucesso.
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        name_element = soup.find("h1", class_="mui-vrkxks-product_info_title")
        product_name = name_element.text.strip() if name_element else None
        
        price_element = soup.find("div", class_="mui-1q2ojdg-price_vista")
        product_price = price_element.text.strip() if price_element else None
        
        if not product_name or not product_price:
            #Se não encontrar o nome ou o preço, retornar None.
            print("Não foi possível encontrar o nome ou o preço do produto no HTML.")
            return None

        return {
            "component": product_name, 
            "raw_price": product_price, 
            "store": "Pichau", 
            "url": TARGET_URL
        }

    except requests.RequestException as e:
        print(f"Erro ao acessar a URL {TARGET_URL}: {e}")
        return None
    except AttributeError as e:
        print(f"Erro ao fazer o parse do HTML. A estrutura do site pode ter mudado: {e}")
        return None
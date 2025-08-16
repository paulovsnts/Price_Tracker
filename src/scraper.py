import requests
from bs4 import BeautifulSoup
from typing import Dict, Optional

# URL do produto alvo: Ryzen 9 7900
TARGET_URL = "https://www.pichau.com.br/processador-amd-ryzen-9-7900-12-core-24-threads-3-7ghz-5-4ghzturbo-cache-76mb-am5-100-100000590box"

def get_product_price() -> Optional[Dict]:
    """
    Busca o nome e o preço do produto alvo na Pichau.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(TARGET_URL, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # TODO: Implementar a lógica de extração do nome e do preço
        product_name = None
        product_price = None

        # =====================================================================
        # LÓGICA DE EXTRAÇÃO ENTRARÁ AQUI
        # =====================================================================
        
        if not product_name or not product_price:
            # Se não encontrar o nome ou o preço, retorna None.
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
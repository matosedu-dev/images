import requests
import os
from urllib.parse import urlparse
from urls import urls


def download_image(url, folder_path="images"):
    try:
        # Criar pasta se não existir
        os.makedirs(folder_path, exist_ok=True)
        
        # Fazer download da imagem
        response = requests.get(url)
        response.raise_for_status()
        
        # Extrair nome do arquivo da URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        # Se não houver extensão, adicionar .jpg como padrão
        if not filename or '.' not in filename:
            filename = f"image_{hash(url) % 10000}.jpg"
        
        # Salvar arquivo
        filepath = os.path.join(folder_path, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        print(f"Imagem salva: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"Erro ao baixar {url}: {e}")
        return None

# Exemplo de uso


# urls = [

#     "https://cambuci.vtexassets.com/arquivos/ids/1505567-1200-auto?v=638774862252200000&width=1200&height=auto&aspect=true",
#     "https://cambuci.vtexassets.com/arquivos/ids/1500865-1200-auto?v=638763652107270000&width=1200&height=auto&aspect=true"
# ]

for url in urls:
    download_image(url)
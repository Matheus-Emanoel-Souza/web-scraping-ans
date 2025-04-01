#pip install requests beautifulsoup4 tqdm
#Base para o código rodar.
import os.path
import requests
from bs4 import BeautifulSoup
import urllib.parse

download_folder = "downloads"
os.makedirs(download_folder, exist_ok=True)


url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

pdf_links = []

for link in soup.find_all('a', href=True):
    href = link['href']
    if href.lower().endswith(".pdf") and ("anexo_i" in href.lower() or "anexo_ii" in href.lower()):
        full_url = urllib.parse.urljoin(url, href)
        pdf_links.append(full_url)

#printar o link para verificar.
print("Links dos PDFs encontrados:")
for link in pdf_links:
    print(link)

#Baixar o conteudo dos links
for pdf_url in pdf_links:
    pdf_name = os.path.join(download_folder, pdf_url.split("/")[-1])#por nome no arquivo
    print(f"Baixando:{pdf_url}->{pdf_name}")

    with requests.get(pdf_url, stream=True) as r:
        r.raise_for_status()
        with open(pdf_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

print("Download concluído!")
#Código concluido, estava buscando na pagina errada.
#mudar para buscar pelo link e terminar em .pdf
#retorno com muitos PDF'S, Filtrar por anexo.
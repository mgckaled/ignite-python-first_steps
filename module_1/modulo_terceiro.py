import requests

print("\nImportação e uso de um módulo de terceiros")

URL = "https://www.exemple.com"
response = requests.get(URL)
print(f"Solicitacao HTTP para {URL} retornou o status {response.status_code}")

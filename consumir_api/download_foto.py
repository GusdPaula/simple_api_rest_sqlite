import requests

url = 'http://localhost:3001/images/1684683480544_12773.png'
nome_arquivo = url.split('/')[-1]

response = requests.get(url=url)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print('Status code:', response.status_code)
    print('Reason:', response.reason)

    with open(nome_arquivo, 'wb') as file:
        file.write(response.content)

else:
    # Sem sucesso - Erros
    print('Status code:', response.status_code)
    print('Reason:', response.reason)
import requests
from pprint import pprint

print 

url = 'http://127.0.0.1:3001/tokens'

user_data = {
	"password": "senha válida",
	"email": "email_valid2o@email.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print('Status code:', response.status_code)
    print('Reason:', response.reason)
    print('JSON:', response.json())

    response_data = response.json()
    token = response_data['token']

    with open('token.txt', 'w') as file:
        file.write(token)

else:
    # Sem sucesso - Erros
    print('Status code:', response.status_code)
    print('Reason:', response.reason)
    print('Texto:', response.text)

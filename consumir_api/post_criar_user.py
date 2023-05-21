import requests
from pprint import pprint

print 

url = 'http://127.0.0.1:3001/users'

user_data = {
	"nome": "nome válido",
	"password": "senha válida",
	"email": "email_valid2o@email.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print('Status code:', response.status_code)
    print('Reason:', response.reason)
    print('JSON:', response.json())

else:
    # Sem sucesso - Erros
    print('Status code:', response.status_code)
    print('Reason:', response.reason)
    print('Texto:', response.text)

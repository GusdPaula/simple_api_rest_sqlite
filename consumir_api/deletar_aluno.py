import requests
from pprint import pprint
from get_token import TOKEN

print 

url = 'http://127.0.0.1:3001/alunos/2'

headers = {
    'Authorization': TOKEN
}

aluno_data = {}

response = requests.delete(url=url, json=aluno_data, headers=headers)

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

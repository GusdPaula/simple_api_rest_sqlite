import requests
from pprint import pprint
from get_token import TOKEN

print 

url = 'http://127.0.0.1:3001/alunos'

headers = {}

aluno_data = {}

response = requests.get(url=url)

if response.status_code >= 200 and response.status_code <= 299:
    # Sucesso
    print('Status code:', response.status_code)
    print('Reason:', response.reason)
    pprint(response.json())

else:
    # Sem sucesso - Erros
    print('Status code:', response.status_code)
    print('Reason:', response.reason)
    pprint(response.text)

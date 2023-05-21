import requests
from pprint import pprint
from get_token import TOKEN
from mimetypes import MimeTypes
from requests_toolbelt import MultipartEncoder

url = 'http://127.0.0.1:3001/fotos'

mimetypes_ = MimeTypes()
nome_arquivo = 'py.png'
mimetypes_arquivo = mimetypes_.guess_type(nome_arquivo)[0]

multipart = MultipartEncoder(fields={
    "aluno_id": "1",
	"foto": ('nome_arquivo', open(nome_arquivo, 'rb'), mimetypes_arquivo)
})

headers = {
    'Authorization': TOKEN,
    'Content-Type': multipart.content_type
}


if 'png' in mimetypes_arquivo or 'jpg' in mimetypes_arquivo:

    response = requests.post(url=url, headers=headers, data=multipart)

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

else:
    raise TypeError('Imagem não possui formato adequado.')

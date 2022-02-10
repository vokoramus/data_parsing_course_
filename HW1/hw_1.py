import requests
import json
from token_container import github_token

username = 'vokoramus'

# USER = 'vokoramus'
USER = 'jwasham'

# service = 'https://api.github.com/user'
service = 'https://api.github.com/users/' + USER + '/repos'

req = requests.get(f'{service}', auth=(username, github_token))

data = json.loads(req.text)

# for k, v in req.headers.items():
#     print(k, ': ',  v)

# print('Заголовки: \n',  req.headers)
# print('Ответ: \n',  req.text)

# Получить список репозиториев
for repo in req.json():
    if not repo['private']:
        print(repo['html_url'])

# Сохраняем в файл json
json_string = json.dumps(data)
# print(json_string)
with open('json_data.json', 'w') as f:
    f.write(json_string)

# Читаем из файла json
with open('json_data.json') as json_file:
    data = json.load(json_file)
    # print(data)

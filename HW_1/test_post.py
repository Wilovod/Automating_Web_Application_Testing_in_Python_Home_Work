'''
Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост, а потом проверяется его наличие
на сервере по полю «описание».

Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts с передачей параметров
title, description, content.
'''


import requests
import yaml

S = requests.Session()

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    address = data['address2']


def test_post(user_login):
    print(S.post(url=address, headers={'X-Auth-Token': user_login}, data={'title': data['titlee'],
                                                                          'description': data['descriptionn'],
                                                                          'content': data['contentt']}).json())
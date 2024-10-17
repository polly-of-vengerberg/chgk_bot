import requests
import config


def get_id(name: str, surname: str) -> list:
    response = requests.get(url=config.url, params={'name': name, 'surname': surname})
    response_j = response.json()
    if not response_j:
        return []
    return [f"{i['id']} {i['name']} {i.get('patronymic', '')} {i['surname']}".strip() for i in response_j]


def get_name(text: str) -> dict:
    text_list = text.split()
    if len(text_list) != 2:
        return {}
    name_dict = {'name': text_list[0], 'surname': text_list[1]}
    return name_dict

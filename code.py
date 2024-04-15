import requests
import config


def get_id(name: str, surname: str) -> int:
    response = requests.get(url=config.url, params={'name': name, 'surname': surname})
    response_j = response.json()
    if len(response_j) == 0:
        return 0
    id_number = response_j[0]['id']
    return id_number


def get_name(text: str) -> dict:
    text_list = text.split()
    if len(text_list) != 2:
        return {}
    name_dict = {'name': text_list[0], 'surname': text_list[1]}
    return name_dict

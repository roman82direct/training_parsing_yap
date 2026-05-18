import requests
from pprint import pprint
from time import sleep

import requests_cache

TIME_API_URL = 'https://time.now/developer/api/'

if __name__ == '__main__':
    # response = requests.get('https://time.now/developer/api/timezone/Antarctica/Vostok')
    # data = response.json()
    # pprint(f'Часовой пояс антарктической станции «Восток»:: {data}')

    session = requests_cache.CachedSession()
    vostok_url = TIME_API_URL + 'timezone/Antarctica/Vostok'
    # Загружаем текущее время станции "Восток" пять раз.
    for iteration in range(5):
        # После третьей загрузки — очистка кеша.
        if iteration > 2:
            session.cache.clear()
        response = session.get(url=vostok_url)
        # Ответ от сервера приходит в формате JSON,
        # поэтому нужно преобразовать его методом .json(),
        # чтобы дальше работа велась с данными, как со словарём.
        data = response.json()
        print(iteration, data.get('datetime'))
        sleep(1)
    print('Часовой пояс антарктической станции «Восток»:',
          data.get('utc_offset'))

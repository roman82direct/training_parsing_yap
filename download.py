import re
from pathlib import Path
from urllib.parse import urljoin

import requests_cache
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).parent

DOWNLOADS_URL = 'https://docs.python.org/3/download.html'
link_pattern = r'.+text\.zip$'

if __name__ == '__main__':
    # Варим суп.
    session = requests_cache.CachedSession()
    response = session.get(DOWNLOADS_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')

    # Получаем нужную ссылку.
    archive_url = urljoin(
        DOWNLOADS_URL,
        soup.find('a', attrs={'href': re.compile(link_pattern)})['href']
    )

    # Создаем директорию для хранения скачанных файлов.
    # путь до директории downloads.
    downloads_dir = BASE_DIR / 'downloads'
    # Создайте директорию.
    downloads_dir.mkdir(exist_ok=True)
    # Получите путь до архива, объединив имя файла с директорией.
    archive_path = downloads_dir / archive_url.split('/')[-1]

    # Загрузка архива по ссылке.
    response = session.get(archive_url)

    # В бинарном режиме открывается файл на запись по указанному пути.
    with open(archive_path, 'wb') as file:
        # Полученный ответ записывается в файл.
        file.write(response.content)

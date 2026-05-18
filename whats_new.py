from urllib.parse import urljoin

import requests_cache
from bs4 import BeautifulSoup
from tqdm import tqdm

WHATS_NEW_URL = 'https://docs.python.org/3/whatsnew/'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(WHATS_NEW_URL)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, features='lxml')

    main_div = soup.find('section', attrs={'id': 'what-s-new-in-python'})
    div_with_ul = main_div.find('div', attrs={'class': 'toctree-wrapper'})
    sections_by_python = div_with_ul.find_all('li',
                                              attrs={'class': 'toctree-l1'})

    results = []
    for section in tqdm(sections_by_python):
        version_link = urljoin(WHATS_NEW_URL, section.find('a')['href'])
        response = session.get(version_link)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, features='lxml')
        results.append(
            (
                version_link,
                soup.find('h1').text,
                soup.find('dl').text.replace('\n', ' ')
            )
        )
    for result in results:
        print(*result)

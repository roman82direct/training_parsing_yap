import requests
from bs4 import BeautifulSoup

LOGIN_URL = 'http://130.193.59.87/login/'

if __name__ == '__main__':
    data = {
        'username': 'test_parser_user',
        'password': 'testpassword',
    }

    session = requests.session()
    get_csrf_response = session.get(LOGIN_URL)
    get_csrf_response.encoding = 'utf-8'
    soup = BeautifulSoup(get_csrf_response.text, features='lxml')
    csrf = soup.find('input', attrs={'name': 'csrfmiddlewaretoken'})['value']

    data.update({'csrfmiddlewaretoken': csrf})

    login_response = session.post(LOGIN_URL, data=data)
    login_response.encoding = 'utf-8'
    print(login_response.text)
    print(session.cookies.get_dict())  # получаем словарь кук
    print(login_response.status_code)

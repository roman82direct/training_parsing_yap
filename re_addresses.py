import re

addresses = [
    ('Он проживал в городе Иваново на улице Наумова. '
     'Номер дома 125 был зеркальной копией его номера квартиры 521'),
    'Адрес: город Новосибирск, улица Фрунзе, дом 321, квартира 15.'
]

pattern = (
    r'город\w*[\s,]*(?P<city>\w+).*'
    r'улиц\w*[\s,]*(?P<street>\w+).*'
    r'дом\w*[\s,]*(?P<house>\d+).*'
    r'квартир\w*[\s,]*(?P<apt>\d+)'
)

for address in addresses:
    # Примените метод регулярных выражений, который
    # найдёт шаблон pattern в строке address.
    # address_match = re.search(pattern, address)
    # print(
    #     address_match.group('city'), address_match.group('street'),
    #     address_match.group('house'), address_match.group('apt')
    # )
    print(*re.search(pattern, address).groups())

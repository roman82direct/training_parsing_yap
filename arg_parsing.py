import argparse
import sys

MURZIK = '=^..^=______/'

if __name__ == '__main__':
    # Инициализация парсера аргументов с описанием.
    parser = argparse.ArgumentParser(description='Вежливый скрипт')
    # Добавление позиционного аргумента для имени.
    parser.add_argument('name', help='Имя')
    # Добавление именованного аргумента для фамилии.
    parser.add_argument('-s', '--surname', help='Фамилия')
    # Извлечение аргументов командной строки в переменную args.
    parser.add_argument(
        '-c',
        '--city',
        help='Город',
        choices=['Chekhov', 'Dublin', 'Minsk', 'Simbirsk'],
    )
    parser.add_argument(
        '-m',
        '--murzik',
        action='store_true',
        help=f'Отправить кота Мурзика {MURZIK}'
    )
    args = parser.parse_args()
    parts = []
    # Добавляем приветствие по имени.
    parts.append(f'Hello, {args.name}')
    # Если указана фамилия, то она тоже добавляется к выводу.
    if args.surname is not None:
        parts.append(args.surname)
    if args.city is not None:
        parts.append(f'from {args.city}')
    # Новое условие для вывода изображения кота Мурзика.
    if args.murzik:
        parts.append(MURZIK)
    # Печатаем через пробел все элементы списка parts.
    print(*parts)

    # python arg_parsing.py Roman -c Chekhov -s Petrovich -m

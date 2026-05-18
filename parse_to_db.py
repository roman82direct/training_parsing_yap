import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declared_attr, Session, declarative_base


PEP_URL = 'https://peps.python.org/numerical/'

# Создайте модель Pep для таблицы pep в декларативном стиле ORM.
# Атрибуты модели:
# 1. id, целочисленное значение, primary key
# 2. type_status, строка с максимальной длиной 2 символа
# 3. number, целочисленное значение, уникальное
# 4. title, строка с максимальной длиной 200 символов
# 5. authors, строка с максимальной длиной 200 символов


# Ваш код - здесь:
# создайте таблицу в БД;
# загрузите страницу PEP_URL;
# создайте объект BeautifulSoup;
# спарсите таблицу построчно и запишите данные в БД.


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)


class Pep(Base):
    type_status = Column(String(2))
    number = Column(Integer, unique=True)
    title = Column(String(200))
    authors = Column(String(200))

    def __repr__(self):
        return f'PEP {self.number} {self.title}'


if __name__ == '__main__':
    engine = create_engine('sqlite:///parse_sqlite.db', echo=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    response = requests.get(PEP_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    rows = soup.select('table.pep-zero-table tbody tr')

    # results = []
    for row in rows:
        status = row.find('td')
        number = status.find_next_sibling('td')
        title = number.find_next_sibling('td')

        session.add(
            Pep(
                type_status=status.text,
                number=int(number.text),
                title=title.text,
                authors=title.find_next_sibling('td').text
            )
        )
        session.commit()
        # results.append(
        #     Pep(
        #         type_status=status.text,
        #         number=int(number.text),
        #         title=title.text,
        #         authors=title.find_next_sibling('td').text
        #     )
        # )

    # session.add_all(results)
    # session.commit()

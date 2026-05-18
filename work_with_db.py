from sqlalchemy import (
    create_engine, Column, Integer, String, delete, insert, select, update
)
from sqlalchemy.orm import declared_attr, registry, Session, declarative_base

# # Вариант 1.
# mapper_registry = registry()
# Base = mapper_registry.generate_base()

# Вариант 2, упрощённая запись с применением "синтаксического сахара":
# Base = declarative_base()


class PreBase:

    @declared_attr
    def __tablename__(cls):
        # В моделях-наследниках свойство __tablename__ будет создано
        # из имени модели, переведённого в нижний регистр.
        # Возвращаем это значение.
        return cls.__name__.lower()

    # В моделях-наследниках будет создана колонка id типа Integer
    id = Column(Integer, primary_key=True)


# Декларативная база включит в себя атрибуты, описанные в классе PreBase.
Base = declarative_base(cls=PreBase)


class Pep(Base):
    # __tablename__ = 'pep'  # Задали имя таблицы в БД.

    # Описываем свойства модели/колонки таблицы:
    # id = Column(Integer, primary_key=True)
    pep_number = Column(Integer, unique=True)
    name = Column(String(200))
    status = Column(String(20))

    # def __str__(self):
    #     # При вызове функции print()
    #     # будут выводиться значения полей pep_number и name.
    #     return f'PEP {self.pep_number} {self.name}'

    def __repr__(self):
        # При представлении объекта класса Pep
        # будут выводиться значения полей pep_number и name.
        return f'PEP {self.pep_number} {self.name}'


if __name__ == '__main__':
    # Создаём движок.
    engine = create_engine('sqlite:///sqlite.db', echo=True)  # echo выводит SQL-запросы в консоль
    Base.metadata.create_all(engine)  # Создаем таблицы в БД

    # Сессия создаётся на основе движка.
    session = Session(engine)

    # pep8 = Pep(
    #     pep_number=8,
    #     name='Style Guide for Python Code',
    #     status='Active'
    # )
    # pep20 = Pep(
    #     pep_number=20,
    #     name='The Zen of Python',
    #     status='Active'
    # )
    # pep216 = Pep(
    #     pep_number=216,
    #     name='Docstring Format',
    #     status='Rejected'
    # )

    # # session.add(pep8)
    # # session.add(pep20)
    # session.add_all(
    #     (pep8, pep20, pep216)
    # )
    # session.commit()

    results = session.query(Pep).all()
    print(results)
    # results = session.query(Pep.name, Pep.status).first()
    # print(results)


    # # Изменение объектов.
    # # Получаем объект из базы:
    # pep8 = session.query(Pep).filter(Pep.pep_number == 8).first()
    # # Заменяем свойство объекта:
    # pep8.status = 'Closed'
    # # Коммитим:
    # session.commit()

    # или изменение для всех объектов в базе:
    session.query(Pep).update(
        {'status': 'Active'}
    )

    session.commit()

    # # Удаление объектов:
    # # одного объекта:
    # pep8 = session.query(Pep).filter(Pep.pep_number == 8).first()
    # session.delete(pep8)
    # session.commit()

    # # коллекции объектов:
    # session.query(Pep).filter(Pep.pep_number > 20).delete()
    # session.commit()

    # В SQLAlchemy есть и другой способ выполнять операции CRUD
    #  — через метод session.execute().
    # В этом случае сначала создаётся выражение с использованием функций
    # insert(), select(), update() или delete().

    result = session.execute(
        select(Pep).where(Pep.status == 'Active')
    )
    print(result.all())

    session.execute(
        insert(Pep).values(
            pep_number='1000',
            name='Pep from Future',
            status='Proposal'
        )
    )
    session.commit()

    session.execute(
        update(Pep).where(Pep.pep_number == 8).values(status='Active')
    )
    session.commit()

    session.execute(
        delete(Pep).where(Pep.status == 'Active')
    )
    session.commit()

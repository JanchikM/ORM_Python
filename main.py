import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale


DSN = 'postgresql://postgres:Dental_67@localhost:5432/HW_ORM'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()

# with open('tests_data.json', 'r') as f:
#     data = json.load(f)
#
#     for record in data:
#         model = {
#             'publisher': Publisher,
#             'shop': Shop,
#             'book': Book,
#             'stock': Stock,
#             'sale': Sale,
#         }[record.get('model')]
#         session.add(model(id=record.get('pk'), **record.get('fields')))
#     session.commit()

def search_info(input_publisher):
    query = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale)
    if input_publisher.isdigit():
        query = query.filter(Publisher.id == input_publisher).all()
    else:
        query = query.filter(Publisher.name == input_publisher).all()
    for title, name, price, date_sale in query:
        print(f"{title} | {name} | {price} | {date_sale}")

search_info(input("Введите данные: "))

session.close()
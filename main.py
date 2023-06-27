import sqlalchemy
import sqlalchemy as sq
import datetime as dt
from sqlalchemy.orm import declarative_base, relationship, sessionmaker



DSN = 'postgresql://postgres:romarchuk@localhost:5432/orm'
engine = sqlalchemy.create_engine(DSN)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Sale(Base):
    __tablename__ = 'Sale'

    id = sq.Column(sq.Integer, unique=True, primary_key=True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.DateTime, default=dt.datetime.now)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("Stock.id"), unique=True)
    count = sq.Column(sq.Integer)

class Stock(Base):
    __tablename__ = 'Stock'

    id = sq.Column(sq.Integer, unique=True, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("Book.id"), unique=True)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("Shop.id"), unique=True)
    count = sq.Column(sq.Integer)

    sale = relationship('Sale', backref='Stock')

class Book(Base):
    __tablename__ = 'Book'

    id = sq.Column(sq.Integer, unique=True, primary_key=True)
    title = sq.Column(sq.Text, nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("Publisher.id"), unique=True)

    stock_book = relationship('Stock', backref='Book')
    stock_shop = relationship('Stock', backref='Book')


class Shop(Base):
    __tablename__ = 'Shop'

    id = sq.Column(sq.Integer, unique=True, primary_key=True)
    name = sq.Column(sq.Text, nullable=False)

class Publisher(Base):
    __tablename__ = 'Publisher'

    id = sq.Column(sq.Integer, unique=True, primary_key=True)
    name = sq.Column(sq.Text, nullable=False)

    book = relationship('Book', backref='Publisher')

    


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)



if __name__ == '__main__':
    session = Session()

    create_tables(engine)

    session.close()
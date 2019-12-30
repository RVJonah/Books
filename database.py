import os
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import mapper

def initiate_database():
    db_URI = os.environ['DATABASE_URI']
    engine = create_engine(db_URI)

    metadata = MetaData()
    class Books(object):
        def __init__(self, id, isbn, title, author, year):
            self.id = id
            self.isbn = isbn
            self.title = title
            self.author = author
            self.year = year

    books = Table('books_data', metadata,
                Column('isbn', String(128), primary_key=True),
                Column('title', String(512)),
                Column('author', String(256)),
                Column('year', String(4))
    )

    class Users(object):
        def __init__(self, username, password_hash, email):
            self.username = username
            self.password_hash = password_hash
            self.email = email

    users = Table('books_users', metadata,
                Column('username', String(128), primary_key=True),
                Column('password_hash', String(512)),
                Column('email', String(512)),
    )
    
    class Reviews(object):
        def __init__(self, review_number, username, isbn, review_title, review_text, review_rating):
            self.review_number = review_number
            self.username = username
            self.isbn = isbn
            self.review_title = review_title
            self.review_text = review_text
            self.review_rating = review_rating

    reviews = Table('books_reviews', metadata,
            Column('review_number', Integer(), primary_key=True),
            Column('username', String(128)),
            Column('isbn', String(512)),
            Column('review_title', String(128)),
            Column('review_text', String(500)),
            Column('review_rating', Integer())
    )

    mapper(Books, books)
    mapper(Users, users)
    mapper(Reviews, reviews)

    metadata.create_all(engine)

    return ({
    'engine': engine,
    'metadata': metadata,
    'books': Books,
    'users': Users,
    'reviews': Reviews
    })
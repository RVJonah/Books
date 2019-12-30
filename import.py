import csv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from database import initiate_database

def main ():
    # initiates database engine and ORM tables
    database = initiate_database()
    db_session = sessionmaker(database['engine'])
    db = db_session()
    Books = database['books']
    books = open('books.csv', newline='')
    bookList = csv.reader(books)
    numberOfBooks = 0
    # for each row(book) adds book to database ignores first row as they are labels
    for book in bookList:
        if numberOfBooks == 0:
            numberOfBooks += 1
        else:
            new_book = Books(id=numberOfBooks,
            isbn=book[0],
            title=book[1],
            author=book[2],
            year=book[3]
            )
            db.add(new_book)
            numberOfBooks += 1
    db.commit()
    print("csv import complete")
    print(f"{numberOfBooks - 1} items successfully added to database")

if __name__ == "__main__":
    main()
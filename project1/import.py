import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

if not os.getenv("DATABASE_URL"):
    os.environ["DATABASE_URL"] = "postgres://jnhdylhrgoontf:bd8b68d76e81fb5b9c7489e2ceddb041320d600a613a19aa45da1aa58697e493@ec2-54-243-208-234.compute-1.amazonaws.com:5432/d61cotnr4krl5v"
    

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    db.execute(
        "CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR NOT NULL, password VARCHAR NOT NULL)")
    db.execute("CREATE TABLE reviews (isbn VARCHAR NOT NULL,review VARCHAR NOT NULL, rating INTEGER NOT NULL,username VARCHAR NOT NULL)")
    db.execute("CREATE TABLE books (isbn VARCHAR PRIMARY KEY,title VARCHAR NOT NULL,author VARCHAR NOT NULL,year VARCHAR NOT NULL)")
    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        if year == "year":
            print('skipped first line')
        else:
            db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:a,:b,:c,:d)", {
                       "a": isbn, "b": title, "c": author, "d": year})

    print("done")
    db.commit()


if __name__ == "__main__":
    main()

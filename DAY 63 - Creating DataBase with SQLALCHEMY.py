from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

##CREATE DATABASE
class Base(DeclarativeBase):
    pass
# Create the extension
db = SQLAlchemy(model_class=Base)

##CREATE TABLE
class Books(db.Model):
    id: Mapped[int] = mapped_column(Integer,primary_key=True)
    title: Mapped[str] = mapped_column(String(250),unique=True,nullable=False)
    author: Mapped[str] = mapped_column(String(250),nullable=False)
    review: Mapped[float] = mapped_column(Float,nullable=False)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)

# Optional: this will allow each book object to be identified by its title when printed.
def __repr__(self):
    return f'<Book {self.title}>'

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
with app.app_context():
    try:
        db.create_all()
        #print("DB created.")
        new_book = Books(title="Nappy Pocker", author="K. T. Tall", review=4.4)
        db.session.add(new_book)
        db.session.commit()
        #print("Book added.")
    except Exception as e:
        print("Error:", e)

# READ RECORD
with app.app_context():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()
# Read A Particular Record By Query
    book = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
    print(book)
    print(all_books)
    print(result)

# UPDATE RECORD
with app.app_context():
    book_to_update = db.session.execute(db.select(Books).where(Books.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

# UPDATE RECORD BY PRIMARY KEY
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit()

# Delete RECORD
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
#import os
#print(os.path.abspath("new-books-collection.db"))
#print(os.getcwd())
#print("Database created!")













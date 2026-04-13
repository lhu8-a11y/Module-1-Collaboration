"""
=================
Book CRUD API
=================
File Name:Module 4 Lab - Python API.py
Author:Lingzhi Hu
Course: 51P-Spring 2026 - Software Development using Python
Module: 4
Description:
    This module implemtns a simple CRUD API for managing a collction
    of books.
    It provides endpoints to create, read, update, and delete book
    records stored in a SQLite database.

    The Book model contains the following fields:
        - id:            (Integer, Primary Key)
        - book_name:     (String, Not Null)
        - author:        (String, Not Null)
        - publisher:     (String, Not Null)
"""

# Import required modules from Flask and SQLAlchemy
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'

db = SQLAlchemy(app)

# Define the Book model (database table structure)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Book(id={self.id},name='{self.book_name}', author='{self.author}', publisher='{self.publisher}')>"

# Root endpoint - provides a simple welcome message
@app.route('/')
def index():
    return 'Welcome to the Book API!'

# GET /books - Retrieve all books
@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        # Create a dictionary for each book
        book_data = {'id': book.id,
                     'book_name': book.book_name,
                     'author': book.author,
                     'publisher': book.publisher
        }
        output.append(book_data)
        
    return {'books': output}

# GET /books/<id> - Retrieve a single book by ID
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id) # Return 404 if book not found
    return {"id": book.id,
            "name": book.book_name,
            "author": book.author,
            "publisher": book.publisher
    }
    
# POST /books - Create a new book
@app.route('/books', methods=['POST'])
def add_book():
    book = Book(
        book_name=request.json['book_name'],
        author=request.json['author'],
        publisher=request.json['publisher']
    )
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

# DELETE /books/<id> - Delete a book by ID
@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if not book:
        return {'message': 'Book not found'}, 404
    db.session.delete(book)
    db.session.commit()
    return {'message': 'Book deleted successfully'}

# PUT /books/<id> - Update an existing book
@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get(id)
    if not book:
        return {'message': 'Book not found'}, 404
    
     # Get JSON data from the request
    data = request.get_json()

    # Update fields if provided; otherwise keep existing values
    book.book_name = data.get('book_name', book.book_name)
    book.author = data.get('author', book.author)
    book.publisher = data.get('publisher', book.publisher)

    db.session.commit() # Save changes to the database

    return {'id': book.id,
            'name': book.book_name,
            'author': book.author,
            'publisher': book.publisher
    }

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, port=5000)
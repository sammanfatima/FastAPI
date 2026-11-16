
import json
import os
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

FILE = "books.json"


# Book model
class Book(BaseModel):
    name: str
    genre: str
    price: float


# Load books from JSON file
def load_books():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as file:
        return json.load(file)


# Save books to JSON file
def save_books(books):
    with open(FILE, "w") as file:
        json.dump(books, file, indent=4)


# Home route
@app.get("/")
def home():
    return {"message": "Welcome to Book Store App!"}


# Get all books
@app.get("/books")
def get_books():
    return load_books()


# Get book by ID
@app.get("/books/{book_id}")
def get_book(book_id: str):
    books = load_books()

    for book in books:
        if str(book["book_id"]) == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found")


# Add a new book
@app.post("/books")
def add_book(book: Book):
    books = load_books()

    new_book = {
        "book_id": str(uuid4()),
        "name": book.name,
        "genre": book.genre,
        "price": book.price
    }

    books.append(new_book)
    save_books(books)

    return new_book


# Delete a book
@app.delete("/books/{book_id}")
def delete_book(book_id: str):
    books = load_books()

    for book in books:
        if str(book["book_id"]) == book_id:
            books.remove(book)
            save_books(books)
            return {"message": "Book deleted successfully"}

    raise HTTPException(status_code=404, detail="Book not found")

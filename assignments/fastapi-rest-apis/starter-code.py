# FastAPI REST API Starter Code
# Install FastAPI and uvicorn: pip install fastapi uvicorn

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Book Management API")

# TODO: Define your Book model using Pydantic BaseModel
class Book(BaseModel):
    pass  # Add fields here

# In-memory storage for books
books = []

# TODO: Implement your API endpoints below

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Book Management API"}


# TODO: GET /books - Get all books


# TODO: GET /books/{book_id} - Get a specific book


# TODO: POST /books - Create a new book


# TODO: PUT /books/{book_id} - Update a book


# TODO: DELETE /books/{book_id} - Delete a book


# To run the server, use: uvicorn starter-code:app --reload

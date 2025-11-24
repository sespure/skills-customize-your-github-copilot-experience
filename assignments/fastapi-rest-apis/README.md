# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a fully functional REST API using the FastAPI framework. You'll learn how to create endpoints, handle different HTTP methods, work with request/response models, and implement basic CRUD operations for a resource.

## 📝 Tasks

### 🛠️	Create a Book Management API

#### Description
Build a REST API that manages a collection of books. The API should support creating, reading, updating, and deleting book records using standard HTTP methods.

#### Requirements
Completed program should:

- Install and set up FastAPI with uvicorn server
- Create a Book model with fields: id (int), title (str), author (str), year (int), and genre (str)
- Implement a GET endpoint `/books` that returns all books in the collection
- Implement a GET endpoint `/books/{book_id}` that returns a specific book by ID
- Implement a POST endpoint `/books` that creates a new book and returns the created book
- Implement a PUT endpoint `/books/{book_id}` that updates an existing book
- Implement a DELETE endpoint `/books/{book_id}` that removes a book from the collection
- Use Pydantic models for request/response validation
- Include proper HTTP status codes (200, 201, 404, etc.)
- Store books in memory using a list or dictionary (no database required)


### 🛠️	Add Query Parameters and Documentation

#### Description
Enhance your API with query parameters for filtering and leverage FastAPI's automatic documentation feature.

#### Requirements
Completed program should:

- Add query parameters to `/books` endpoint to filter by author and/or genre
- Add a query parameter to limit the number of results returned
- Test the API using FastAPI's automatic interactive documentation at `/docs`
- Include docstrings for each endpoint explaining what it does
- Handle edge cases like requesting a book ID that doesn't exist (return 404)
- Return appropriate error messages in a consistent JSON format

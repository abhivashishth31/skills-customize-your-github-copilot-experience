# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, production-ready REST APIs using the FastAPI framework. You'll create a complete API with multiple endpoints, request validation, error handling, and interactive documentation, gaining hands-on experience with backend web development.

## 📝 Tasks

### 🛠️ Set Up FastAPI Project and Create Basic Endpoints

#### Description
Initialize a FastAPI application and create basic GET and POST endpoints to handle simple data operations.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn dependencies
- Create a FastAPI application instance
- Define a GET endpoint that returns a welcome message
- Define a POST endpoint that accepts JSON data and returns a confirmation response
- Run the server locally using Uvicorn (default: `localhost:8000`)
- Document all endpoints with proper path and query parameters

### 🛠️ Implement CRUD Operations for a Resource

#### Description
Expand your API to support full CRUD (Create, Read, Update, Delete) operations on a resource (e.g., a to-do item, book, or user profile).

#### Requirements
Completed program should:

- Create POST endpoint to add new items
- Create GET endpoint to retrieve all items or a single item by ID
- Create PUT endpoint to update an existing item
- Create DELETE endpoint to remove an item
- Use Pydantic models for request/response validation
- Return appropriate HTTP status codes (200, 201, 400, 404, etc.)
- Include error handling with meaningful error messages

### 🛠️ Add Data Validation and Documentation

#### Description
Enhance your API with robust data validation and interactive API documentation.

#### Requirements
Completed program should:

- Use Pydantic models to validate request and response data
- Add field validation constraints (required fields, type checking, string length, etc.)
- Include docstrings for all endpoints describing their purpose
- Access the auto-generated Swagger UI documentation at `/docs`
- Access the alternative ReDoc documentation at `/redoc`
- Handle validation errors gracefully with descriptive error responses

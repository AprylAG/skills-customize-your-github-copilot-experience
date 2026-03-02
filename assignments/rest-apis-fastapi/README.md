# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework. Learn how to create endpoints, handle HTTP methods, validate data, and work with databases to develop a functional web service.

## 📝 Tasks

### 🛠️ Create a Basic Todo API

#### Description
Develop a FastAPI application that implements a complete CRUD (Create, Read, Update, Delete) API for managing todos. The API should handle HTTP requests and return structured JSON responses.

#### Requirements
Completed program should:

- Set up a FastAPI application with proper project structure
- Create endpoints for GET, POST, PUT, and DELETE operations
- Implement request validation using Pydantic models
- Store todos in a database (SQLite or in-memory storage)
- Return appropriate HTTP status codes for different operations
- Include error handling for invalid requests and missing resources
- Provide clear documentation through endpoint descriptions and docstrings

### 🛠️ Add Authentication and Advanced Features

#### Description
Extend the API with user authentication and additional features such as filtering, pagination, and sorting to create a more robust and production-ready application.

#### Requirements
Completed program should:

- Implement basic authentication (bearer token or API key)
- Add filtering capabilities to retrieve todos by status or user
- Implement pagination for list endpoints
- Add sorting options for different fields
- Include request logging and error responses with meaningful messages
- Write unit tests for critical endpoints

# Fastapi and Backend Development Notes

## Basics

### What is an API?

* Application Programming Interface
* Allows different software systems to communicate with each other.
* Defines the methods and data formats that applications can use to request and exchange information.

### REST API

* Representational State Transfer
* An architectural style for building networked applications.
* Key principles:
    1.  Stateless: Each request from a client to a server must contain all the information needed to understand the request. The server does not store any client context between requests.
    2.  Client-Server: A separation of concerns between the client (user interface) and the server (data storage).
    3.  Cacheable: Responses should be cacheable to improve performance.
    4.  Layered System: The architecture can be composed of multiple layers, and a client cannot ordinarily tell whether it is connected directly to the end server or to an intermediary.
    5.  Uniform Interface: This is the core of REST and includes:
        * Identification of resources (URIS)
        * Manipulation of resources through representations (e.g., JSON, XML)
        * Self-descriptive messages (e.g., using media types)
        * Hypermedia as the engine of application state (HATEOAS)

### API Endpoints

* Specific URLS that represent resources or actions in the API.
* Clients interact with these endpoints using HTTP methods (GET, POST, PUT, DELETE, etc.).

## FastAPI

* A modern, fast (high-performance) web framework for building AAPISwith Python 3.8+ based on standard Python type hints.

### Key Features

* **Based on open standards:** Openapi (formerly Swagger) and JSON Schema.
* **Automatic data validation:** Using Pydantic.
* **Serialisation:** Automatic conversion of Python data structures to JSON.
* **Documentation:** Automatic interactive API documentation (Swagger UI and ReDoc).
* **Dependency Injection:** Built-in support for managing dependencies.
* **Security:** Easy integration with security schemes like OAuth2.

### Core Concepts

* **Path Operations:** Define the HTTP methods (GET, POST, PUT, DELETE, etc.) and paths (URLS) for your API endpoints.
* **Path Parameters:** Variables in the URL path (e.g., `/items/{item_id}`).
* **Query Parameters:** Parameters passed in the URL after a question mark (e.g., `/items/?skip=0&limit=10`).
* **Request Body:** Data sent by the client in the body of the request (often in JSON format). Defined using Pydantic models.
* **Responses:** Data returned by the API to the client. Can also be defined using Pydantic models.
* **Pydantic:** A data validation and settings management library using Python type hints. Used by FastAPI for request and response data validation and serialization.
* **Dependencies:** Functions that can be run before your path operation functions, used for authentication, authorization, data validation, etc.
* **Middleware:** Functions that process every request before it reaches any specific path operation and every response before leaving.

### Basic Structure

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(item: Item):
    return item

# ... other path operations and code ...

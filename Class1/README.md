# Backend Development Concepts

This README provides an overview of backend development concepts, with a focus on RESTful APIs, as outlined in my notes.

## Core Backend Concepts

* **Programming Languages:**
    * [List the programming languages mentioned in your notes, e.g., Python, JavaScript, Java]
* **Computer Languages:**
    * Designed to give instructions to computers.
    * Work with data and state to perform tasks.
    * Built with strict syntax and semantic rules.
    * These are the basis of high-level programming languages.

## REST API Fundamentals

* **REST API:** (Representational State Transfer Application Programming Interface)
    * A common architectural style for building web services.
    * Relies on stateless communication.
    * Typically uses HTTP methods for operations.
    * Often transfers data in JSON format.

* **Key Components:**
    * **Resources:** Represent entities or objects (e.g., users, products).
    * **HTTP Methods:** Define actions to be performed on resources:
        * `GET`: Retrieve data.
        * `POST`: Create new data.
        * `PUT`: Update existing data.
        * `DELETE`: Remove data.
    * **Statelessness:** Each request from the client to the server contains all the information needed to understand the request. The server does not store any client context between requests.
    * **JSON:** (JavaScript Object Notation) A lightweight data-interchange format.

* **Logic & Flow:**
    ```
    User Centric Data --> Modules (functions, methods, processes, manipulation) --> Save in Database --> Logic (if/else/switch) --> REST API (Variables, functions, endpoints)
    ```

## HTTP (Hypertext Transfer Protocol)

* **Foundation of Data Communication on the Web.**
* **Request-Response Model:**
    * **Client (e.g., Browser, Application):** Sends HTTP requests to the server.
    * **Server:** Receives and processes requests, then sends back HTTP responses.

* **HTTP Request Structure:**
    * **Method:** (e.g., GET, POST, PUT, DELETE) Indicates the desired action.
    * **Path/URI (Uniform Resource Identifier):** Identifies the resource on the server.
    * **Headers:** Provide additional information about the request (e.g., content type, authorization).
    * **Body (Optional):** Contains data to be sent to the server (e.g., for POST or PUT requests).

* **HTTP Response Structure:**
    * **Status Code:** Indicates the outcome of the request (e.g., 200 OK, 404 Not Found, 500 Internal Server Error).
    * **Headers:** Provide additional information about the response (e.g., content type).
    * **Body (Optional):** Contains the requested data or error message.

* **Common HTTP Status Codes:**
    * `200 OK` - The request was successful.
    * `201 Created` - The request has been fulfilled and resulted in a new resource being created.
    * `400 Bad Request` - The server could not understand the request due to invalid syntax.
    * `401 Unauthorized` - The client must authenticate itself to get the requested response.
    * `403 Forbidden` - The client does not have access rights to the content.
    * `404 Not Found` - The server can not find the requested resource.
    * `500 Internal Server Error` - The server encountered an unexpected condition that prevented it from fulfilling the request.

## API Methodologies

* **REST (Representational State Transfer):** (Covered above)
* **SOAP (Simple Object Access Protocol):**
    * An older, more complex protocol for web services.
    * Relies on XML for message format.
* **GraphQL:**
    * A query language for your API and a server-side runtime for executing those queries.
    * Allows clients to request specific data they need, avoiding over-fetching.

## API Endpoints

* **Definition:** Specific URLs (Uniform Resource Locators) that represent the resources exposed by the API.
* **Structure:** Typically follows a logical and hierarchical structure (e.g., `/users`, `/products/{id}`, `/orders`).

## API Documentation

* **Importance:** Crucial for developers to understand how to use the API.
* **Common Methods:**
    * **Manual Documentation:** Writing guides and specifications.
    * **Swagger/OpenAPI:** A widely adopted specification for describing REST APIs. Allows for automated generation of documentation and client libraries.

## API Authentication and Authorization

* **Authentication:** Verifying the identity of the client making the request.
    * **Common Methods:**
        * HTTP Basic Auth: Simple authentication scheme using username and password.
        * API Keys: Unique keys assigned to clients for identification.
        * OAuth 2.0: An open standard for authorization, commonly used for third-party access.
        * JWT (JSON Web Tokens): A compact, URL-safe means of representing claims to be transferred between two parties.
* **Authorization:** Determining what actions an authenticated client is allowed to perform.

## Data Persistence

* **Databases:** Used to store and retrieve application data.
    * **Types:**
        * Relational Databases (e.g., MySQL, PostgreSQL): Organize data into tables with defined relationships.
        * NoSQL Databases (e.g., MongoDB, Cassandra): Provide flexible schemas for various data models.

## Backend Architecture
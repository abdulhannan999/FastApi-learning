# 📘 Class 3 – FastAPI Project Setup & Core Concepts

In Class 2 we made our first API!

## 🚀 Project Initialization Steps

To start a new FastAPI project using uv, follow these steps:


**What these commands do:**
- `uv init --app`: Initializes a new project with a structure ready for a web app.
- `uv add fastapi --standard`: Adds FastAPI along with standard dependencies.
- `uv run fastapi dev`: Runs the FastAPI server in development mode.

## 📁 Folder and File Structure

You created a folder called **App** in the root directory.

Inside it, you added a `__init__.py` file.

### Why use `__init__.py`?

This is a special "dunder" (double underscore) file that turns a folder into a package. A package allows Python to treat a directory as a module container.

## 🧩 Modules vs Packages

| Concept | Description |
|--------|-------------|
| Module | A single .py file that contains Python code. |
| Package | A folder containing a collection of modules, marked with a `__init__.py` file. |

## 🌐 API Basics

**Base URL:** The root address of your API.  
Example: [https://gemini.google.com](https://gemini.google.com)

**Entry Point:** The root path `/` of your API, which often returns a homepage or welcome message.

## 🔐 What is HTTPS?

HTTPS (HyperText Transfer Protocol Secure) is a secure version of HTTP.

- It ensures data sent between client and server is encrypted.
- Used in all secure communication on the web (e.g., login forms, payment gateways).

Operates through a request/response model:
1. The client (browser or app) sends a request.
2. The server processes it and returns a response.

## 🖥️ Server Concepts

**Server:** A computer that runs software to handle requests from clients over a network.

**NGINX Server:** A popular web server used as:
- A load balancer (distributes traffic across multiple servers).
- A reverse proxy (forwards client requests to backend servers).

**Port 80:**  
Default port for HTTP traffic.  
NGINX listens on this port to receive requests.

**Config File:**  
Found at: `/etc/nginx/sites-available/your-config-file`  
It defines how NGINX handles and redirects requests.

### Request/Response Cycle

1. Client sends a request (e.g., open a webpage).
2. NGINX receives it and redirects it to your app.
3. App sends back a response (HTML, JSON, etc.).

## 🌍 Domain Name System (DNS)

- `.com` is a TLD (Top-Level Domain).
- Domain name (like `google.com`) maps to a server's IP address (like `127.0.0.1` for localhost).
- This translation is handled by DNS (Domain Name System).

## 🛣️ URLs, Paths, and URIs

| Term | Meaning |
|------|---------|
| URL | Uniform Resource Locator. Complete web address (includes scheme, domain, and path). |
| URI | Uniform Resource Identifier. General term that identifies a resource (URL is a type of URI). |
| Path | Route to access resources on a server (e.g., /books/ or /books/123). |

### Types of Path Parameters

**Static Path**  
Doesn’t change.  
Example: `https://localhost.com/books`  
Conventionally plural.

**Dynamic Path**  
Changes based on request.  
Example: `https://localhost.com/books/1`  
Conventionally singular.

## 🔄 Data Serialization

### What is it?

- **Serialization:** Converting Python objects (e.g., dict) into JSON (string format) to send in a response.
- **Deserialization:** Converting JSON (string) into Python objects for processing on the server.

### Why it matters:

- APIs communicate using JSON.
- FastAPI automatically handles serialization/deserialization under the hood using pydantic models.


# 🚀 FastAPI Learning Notes

---

## 🔧 Prerequisites

- Python
- Virtual Environment
- Requirements.txt
- .env file
- IDE (VS Code / PyCharm)
- Package Management (pip / uv / poetry)
- pyproject.toml
- VS Version Control
- `.gitignore`
- Hosting
- Monitoring

---

## 📍 Where to Start

We are always stuck at starting something.  
**Before Start Learning**  
We need a clear "why"  
Why? → _I become backend developer_

---

## 🏁 Ignition آغاز

### What we want to build

Vehicle API – [PakWheels.com](https://www.pakwheels.com)  
**Tech Stack:**  
- FastAPI

---

## ⚙️ How to Start Creating Project in FastAPI

1. Initialize the FastAPI project & take help from any Python package manager  
   Helps install & uninstall required tools/packages/libraries to build our project.

2. Manage the whole project from development to production level.

**Levels:**
- `pip`
- `poetry`
- `uv`

### Check whether `uv` is installed:
```bash
uv --version
```

### Command to initialize app:
```bash
uv init --app
```
This will create a boilerplate/template to start your FastAPI project.

---

## 📦 Project Structure

- Create app folder inside your root project folder.
- App = main package (directory)
- `__init__.py` = what makes app a package
- `main.py` = entry point of your FastAPI project

---

## 📂 Template Notes

- `.gitignore`:  
  Keeps files/folders that are big in size, contain secrets, or are unnecessary to publish off remote repositories like GitHub/GitLab.

- `pyproject.toml`:  
  - Heart of the project  
  - Contains meta data, dependencies, scripts, and development dependencies  
  - Crucial file — _never delete_

- `requirements.txt`:  
  - Simple text file  
  - Strict syntax format to manage data: JSON, XML, YAML, TOML

---

## 🛠 Dependencies Installation

After project initialization, we need to install the first dependency: **FastAPI**

This is the first required tool to start the project.

### UV and FastAPI Installation Levels:
1. `uv add fastapi` — Standard (i.e. 5)
2. `uv add fastapi --extra` — Standard + extras (i.e. 15)
3. `uv add fastapi --extra all` — All dependencies (i.e. 34)

---

## 🔗 Dependencies FastAPI Uses

- **Pydantic**:  
  - Python package to validate, serialize, de-serialize data  
  - Performs actions regarding data manipulation  
  - Built on other Python packages

- **Starlette**:  
  - Web async Python framework  
  - Base framework used by FastAPI

- **Uvicorn**:  
  - Web server to run FastAPI application  
  - Handles all network requests between client and FastAPI

---

## 🚦 FastAPI App Commands

```bash
uv run fastapi dev
```

Uvicorn server runs the app.

---

## 📄 API Documentation: `openapi.json`

**swaggerui** → auto-generated documentation in browser to interact with our API  
- Behaves like a client
- We can call it
- Useful for testing APIs

---

## 🧪 API Testing Tools

- `pytest`
- `postman`
- `insomnia`
- `thunder client`
- `swaggerui`

---



In programming world, tools are interlinked with each other.  
They may differ in how they perform tasks, but the functionality is often similar.


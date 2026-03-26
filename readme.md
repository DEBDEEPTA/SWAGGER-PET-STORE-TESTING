# SWAGGER PET STORE TESTING

* A Python-based API test automation project for the Swagger Petstore API.  
* This repository is organized around three main API areas:

- **Pet API**
- **Store API**
- **User API**

* The project uses a shared `ApiClient` built on `requests.Session()`
* It has dedicated API wrapper classes for each domain, pytest-based test suites, and HTML report generation through `pytest-html`.

---

## Project Structure

```plaintext
SWAGGER-PET-STORE-TESTING/
├── src/                                 # Main source package
│   ├── __init__.py
│   ├── pet_api.py                       # API wrapper for Pet endpoints
│   ├── store_api.py                     # API wrapper for Store endpoints
│   ├── user_api.py                      # API wrapper for User endpoints
│   └── models/                          # Dataclass-style request/response models
│       ├── __init__.py
│       ├── category.py                  # Category model used in pet payloads
│       ├── order.py                     # Order model for store/order endpoints
│       ├── pet.py                       # Pet model
│       ├── tags.py                      # Tag model used with pets
│       └── user.py                      # User model
│
├── tests/                               # Test suites grouped by API domain
│   ├── __init__.py
│   ├── pet/
│   │   ├── __init__.py
│   │   ├── conftest.py                  # Pet-specific fixtures/setup
│   │   └── test_pet_api.py              # Tests for pet endpoints
│   ├── store/
│   │   ├── __init__.py
│   │   ├── conftest.py                  # Store-specific fixtures/setup
│   │   └── test_store_api.py            # Tests for store endpoints
│   └── user/
│       ├── __init__.py
│       ├── conftest.py                  # User-specific fixtures/setup
│       └── test_user_api.py             # Tests for user endpoints
│
├── utils/
│   ├── __init__.py
│   └── api_client.py                    # Shared HTTP client abstraction using requests
│
├── conftest.py                          # Global pytest hooks and report path setup
├── pytest.ini                           # Pytest configuration and custom markers
├── requirements.txt                     # Project dependencies
└── .gitignore                           # Ignored files/folders
```

## Features
* Modular API wrapper design
* Shared HTTP client for reusable request handling
* Domain-wise separation of source code and tests
* Pytest marker support for selective execution
* HTML test report generation
* Request model organization through dedicated model file

## Installation
1. Clone the repository
```commandline
    git clone https://github.com/DEBDEEPTA/SWAGGER-PET-STORE-TESTING.git
    cd SWAGGER-PET-STORE-TESTING
```
2. Create a Virtual Environment
```commandline
    python -m venv .venv
```
3. Activate Virtual Environment
   * <u>Windows</u>
    ```commandline
        .venv\Scripts\activate
    ```
   * <u>Mac/Linux</u>
   ```commandline
      source .venv/bin/activate 
   ```
## Install dependencies
```commandline
    pip install -r requirements.txt
```
## Running Tests
1. Run All tests
    ```commandline
        pytest
    ```
2. Run Only pet tests
    ```commandline
        pytest -m pet
    ```
3. Run Only Store tests
    ```commandline
        pytest -m store
    ```
4. Run Only User tests
    ```commandline
        pytest -m user
    ```
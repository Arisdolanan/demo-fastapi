## Overview - demo-fastapi
This project demo-fastapi.

## Run
- check python
`python3`

- install package dependencies
`pip install -r requirements.txt`

- running app in cli
`uvicorn main:app --reload`

- running in docker
`docker-compose down`
`docker-compose up --build -d`

# Tools and Technologies
- **Python**: Main programming language for the project.
- **FastAPI**: A modern, high-performance web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: A powerful ORM library for working with SQL databases in a more Pythonic way.
- **Pydantic**: A library for data validation and settings management using Python type annotations.
- **MySQL**: A powerful, open-source object-relational database system known for its reliability and scalability.
- **Uvicorn**: An ASGI server used to run the FastAPI application, enabling asynchronous programming.
- **Docker**: A platform used to develop, ship, and run applications inside containers, providing an isolated environment to run applications.

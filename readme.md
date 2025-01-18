Commands to run fastapi app:
uvicorn main:app --reload --host 0.0.0.0
uvicorn main:app --reload --host 0.0.0.0
uvicorn main:app --host 0.0.0.0 --port 80


uvicorn app:app --reload


Make sure tables are created in the db before doing any db actions
Base.metadata.create_all(bind=engine) use it to make tables into the database


If you want to use Postgres as your db, use:
SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<hostname>:<port>/<database_name>"

make sure psycopg2-binary is installed

/project-name
│
├── main.py                  # Main FastAPI application entry point
├── app
│   ├── __init__.py          # Makes this folder a Python package
│   ├── models               # Data models (using SQLAlchemy)
│   │   ├── __init__.py
│   │   ├── item.py           # Item model
│   │   └── user.py           # User model
│   │
│   ├── schemas              # Pydantic schemas for data validation and serialization
│   │   ├── __init__.py
│   │   ├── item.py           # Item schema
│   │   └── user.py           # User schema
│   │
│   ├── crud                 # CRUD operations for models
│   │   ├── __init__.py
│   │   ├── item.py           # CRUD functions for items
│   │   └── user.py           # CRUD functions for users
│   │
│   ├── routes               # Application routes
│   │   ├── __init__.py
│   │   ├── item.py           # API endpoints for items
│   │   └── user.py           # API endpoints for users
│   │
│   └── database             # Database setup and configuration
│       ├── __init__.py
│       └── session.py        # Database session management
│
├── tests                     # Test cases
│   ├── __init__.py
│   ├── test_item.py          # Tests for item routes
│   └── test_user.py          # Tests for user routes
│
└── env                      # Virtual environment

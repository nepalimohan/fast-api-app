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
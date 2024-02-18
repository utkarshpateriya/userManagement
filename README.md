# userManagement
FastAPI User Management: A dynamic project with login/signup endpoints. Flexible, MySQL-compatible, and JWT-secured. Under active development. Clone, configure MySQL, and explore with Swagger. Future updates include user profiles and role-based access control.

Steps to reproduce-

1. install all the packages-
   1. pip install fastapi, uvicorn, sqlalchemy, pymysql etc
2. Try running the project using `python -m uvicorn main:app --reload` or `uvicorn main:app --reload`
3. If the project runs successfully, do `alembic init alembic`
   1. This will generate an alembic folder that will be used for migrations. In that, import Base that is persent in
   the file database.py. For e.g `from database import Base`
    `target_metadata = Base.metadata` and set target_metadata to the way it is shown above then run
4. `alembic revision --autogenerate -m "Initial migrations"` if it says something like Target database is not up to date then run `alembic upgrade head` then do again `alembic revision --autogenerate -m "Initial migrations"`
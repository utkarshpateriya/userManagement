# userManagement
FastAPI User Management: A dynamic project with login/signup endpoints. Flexible, MySQL-compatible, and JWT-secured. Under active development. Clone, configure MySQL, and explore with Swagger. Future updates include user profiles and role-based access control.

Steps to reproduce-

1. install all the packages-
   1. pip install fastapi, uvicorn, sqlalchemy, pymysql etc
2. Try running the project using `python -m uvicorn main:app --reload` or `uvicorn main:app --reload`
3. If the project runs successfully, do `alembic init alembic`
   1. This will generate an alembic folder that will be used for migrations. In that, import Base that is persent in
   the file database.py. For e.g `from database import Base`
   2. It is important to import all the models in the same env.py file for e.g-
      `from models.userModel import *` and `from models.itemModel import *`.
   3. `target_metadata = Base.metadata` and set target_metadata to the way it is shown above then run
4. `alembic revision --autogenerate -m "Initial migrations"` if it says something like Target database is not up to date then run `alembic upgrade head` then do again `alembic revision --autogenerate -m "Initial migrations"` and at last run `alembic upgrade head`

# FastAPI User Management Project

This FastAPI project provides a boilerplate code for basic user management, including login and signup functionalities. It uses a MySQL or PostgreSQL database to store user information.

## Installation

1. Set up the database URL in the `.env` file.

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

4. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Initialize Alembic for database migrations:

    ```bash
    alembic init alembic
    ```

6. Update the Alembic `env.py` file:

    - Import models:

        ```python
        from models.userModel import *
        from models.itemModel import *
        ```

    - Add metadata:

        ```python
        target_metadata = Base.metadata
        ```

   - Apply migrations:

      ```bash
      alembic revision --autogenerate -m "Initial migrations"
      ```

      ```bash
      alembic upgrade head
      ```



## Usage

### User API Endpoints

#### 1. Login

Endpoint: `/signup`

Request:
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

#### 2. Login

Endpoint: `/login`

Request:
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Response:
```json
{
  "user": {
    "username": "your_username",
    "email": "your_email@example.com",
    "other_user_data": "other_data"
  },
  "token": "your_jwt_token"
}
```

### Items API Endpoints
Explore and play with the code in `routers/itemsRoute.py`.

### Database Configuration
This project is configured to use either MySQL or PostgreSQL. Modify the database URL in the `.env` file according to your choice.

###   Contributors
Utkarsh Pateriya

Feel free to contribute and enhance the project!
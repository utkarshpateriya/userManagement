# User Management
FastAPI User Management: A dynamic project with login/signup endpoints. Flexible, MySQL-compatible, and JWT-secured. Under active development. Clone, configure MySQL, and explore with Swagger. Future updates include user profiles and role-based access control.

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
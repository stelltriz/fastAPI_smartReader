## 👥 User Management API
A RESTful API built with FastAPI and SQLAlchemy to manage employee records.
Supports listing users, searching by ID, creating, updating, and deleting users.


### 🧰 Technologies Used
- FastAPI
- Python
- SQLAlchemy
- CORS Middleware for cross-origin requests


### 🎯 Features / Endpoints
| Method | Endpoint            | Description                   | Request Body     | Response Model   |
| ------ | ------------------- | ----------------------------- | ---------------- | ---------------- |
| GET    | `/get_all_users`    | Retrieve all registered users | None             | List of users    |
| GET    | `/user/{edv}`       | Retrieve user by EDV (ID)     | None             | Single user      |
| POST   | `/user/`            | Create a new user             | UserCreate model | Created user     |
| PUT    | `/update_user/{id}` | Update user data by ID        | UserUpdate model | Updated user     |
| DELETE | `/delete_user/{id}` | Delete user by ID             | None             | Deletion message |



### 🔍 Usage
- Use /get_all_users to view all registered employees
- Search specific employee by /user/{edv}
- Create new employee records via POST /user/
- Update existing records via PUT /update_user/{id}
- Delete users with DELETE /delete_user/{id}

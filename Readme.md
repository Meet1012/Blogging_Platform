# Blogging Platform - Django Application 📝

[![Django](https://img.shields.io/badge/Django-4.0%2B-brightgreen)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
This is a **Django-based blogging platform** that supports user authentication, blog creation, and role-based access control (RBAC) for admins and moderators. It allows users to register, log in, create and manage their blogs, and also provides an admin dashboard for managing users and blog content.

---

## 🚀 Features

- **User Authentication** 🔐: Secure login/logout with JWT token support.
- **Role-Based Access Control** ⚖️: Admins and moderators have special privileges to manage content.
- **Blog Management** 📝: Users can create, edit, view, and delete their own blogs.
- **Admin Dashboard** 🖥️: Admins can manage users and blog content.
- **Token Expiry Handling** ⏳: JWT tokens have a set expiration time, requiring re-authentication.

---

## 🧑‍💻 Technologies Used

- **Django** 🦄: Web framework for Python.
- **JWT (JSON Web Token)** 🔑: For secure authentication.
- **HTML/CSS** 🎨: For front-end styling.
- **SQLite** 🗄️: Database for storing user and blog data (or can be configured to use other DBs).

---

## 🏁 Installation

### Prerequisites 📋

- Python 3.x
- Django
- SQLite (or any other DB of choice)

### Steps to Install 🔧

1. Clone the repository:
    ```bash
    git clone https://github.com/Meet1012/Blogging_Platform.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Blogging_Platform
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser (optional but necessary for admin features):
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

---

## 🔑 Authentication

- **Login** 🛂: Users can log in using their username and password.
- **JWT Token** 🎟️: Upon successful login, a JWT token is generated and stored in the browser's cookies for authentication. The token is valid for a set period and automatically expires.

---

 ## 👤 Basic Credentials
| **Username** | **Password** | **Role**      |
|--------------|--------------|---------------|
| admin        | admin        | admin         |
| mod          | mod          | moderator     |
| user         | user         | user          |


---
## ⚙️ Key Functions

### 1. **Login & Register**

- **Login**: The user can log in with their username and password. Upon successful login, an access token is generated.
  
  - **Endpoint**: `/login/`
  - **Method**: `POST`
  
- **Register**: Users can create a new account by providing a username and password.

  - **Endpoint**: `/register/`
  - **Method**: `POST`

### 2. **Blog Management**

- **Create Blog**: Authenticated users can create a blog with a title and content.
  
  - **Endpoint**: `/create_blog/`
  - **Method**: `POST`

- **View Blog**: All users can view blogs created by others.
  
  - **Endpoint**: `/view_content/<id>/`
  - **Method**: `GET`

- **Edit Blog**: Users can edit their own blogs.
  
  - **Endpoint**: `/edit_blog/<id>/`
  - **Method**: `POST`

- **Delete Blog**: Users can delete their own blogs.
  
  - **Endpoint**: `/delete_blog/<id>/`
  - **Method**: `GET`

### 3. **Admin Dashboard**

- **Admin Access**: Only admin users can access the admin dashboard where they can manage users and blogs.
  
  - **Endpoint**: `/admin_page/`
  - **Method**: `GET`

- **User Management**: Admins can change user roles.
  
  - **Endpoint**: `/change/<user_id>/`
  - **Method**: `POST`

---


## 🔧 Configuration Settings

### **JWT Configuration**

In the `apis/settings.py`, you can modify the settings related to JWT authentication:

- `SECRET_KEY`: The secret key used for encoding and decoding the JWT tokens.
- `ALGORITHM`: The algorithm used to sign the token. Commonly, `'HS256'` is used.
- `EXPIRY_MINUTES`: The expiration time for the JWT token in minutes. Default is set to a value of your choice.

```python
SECRET_KEY = 'your-secret-key'
ALGORITHM = 'HS256'
EXPIRY_MINUTES = 15 
```
---
## 👨‍💻 Developers

- **Your Name** - [Meet1012](https://github.com/Meet1012)  
  Project Lead, Developer

---

## 📚 References

- [Django Official Documentation](https://docs.djangoproject.com/en/stable/)  
  Official documentation for Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design.

- [JWT.io Documentation](https://jwt.io/)  
  Documentation for JSON Web Tokens (JWT), a compact, URL-safe means of representing claims to be transferred between two parties.

- [SQLite Official Documentation](https://www.sqlite.org/docs.html)  
  Official documentation for SQLite, a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.

- [Django Forms Documentation](https://docs.djangoproject.com/en/stable/topics/forms/)  
  Comprehensive guide to working with forms in Django, including how to create forms, handle form submission, and validate data.

- [Python datetime Module Documentation](https://docs.python.org/3/library/datetime.html)  
  Official Python documentation for the `datetime` module, which supplies classes for manipulating dates and times.



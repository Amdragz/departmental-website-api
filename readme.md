# Django Backend

## Overview
This is a Django-based backend that powers the Departmental Portal, providing authentication, user management, and essential resource handling. It features JWT-based authentication for secure access, a PostgreSQL database for efficient data storage, and RESTful APIs to facilitate seamless communication between the frontend and backend. The backend is designed to handle academic resources, notifications, document tracking, and research tools, ensuring a reliable and efficient system that supports students and departmental operations at any University enterprises.

## Features
- User authentication with JWT
- Custom user model with UUID as the primary key
- CRUD operations for user management
- PostgreSQL as the database backend
- API endpoints for retrieving user data
- API endpoints for retrieving user resourses

## Technologies Used
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication

## Setup and Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip ^24.3.1
- PostgreSQL
- Virtualenv (optional but recommended)

### Clone the Repository
```sh
git clone <https://github.com/Amdragz/departmental-website-api>
cd <project-directory>
```

### Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Configure Environment Variables
Create a `.env` file in the project root and add the following:
```env
DB_NAME=<your-database-name>
DB_USER=<your-database-username>
DB_PWD=<your-database-password>
DB_HOST=<your-database-host>
DB_PORT=<your-database-port>
SECRET_KEY=<your-django-secret-key>
DEBUG=True  # Set to False in production
```

### Apply Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser
```sh
python manage.py createsuperuser
```
Follow the prompts to create a superuser account.

### Run the Development Server
```sh
python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

### Authentication
- **POST** `/api/token/` - Obtain JWT token
- **POST** `/api/token/refresh/` - Refresh JWT token

### User Management
- **GET** `/api/users/` - Get all users (requires authentication)
- **GET** `/api/users/<user_id>/` - Retrieve a user by matric number
- **POST** `/api/users/signup/` - Register a new user

### User resources
- **GET** `/api/users/documents/`
- **GET** `/api/users/resources/`
- **GET** `/api/users/courses/`
- **GET** `/api/users/notifications/`

## Deployment
For production, use a WSGI server like Gunicorn and set `DEBUG=False` in `.env`.

Example deployment command:
```sh
gunicorn backend.wsgi:application --bind 0.0.0.0:8000
```

## Contributing
  Missing something or found a bug? [Report here](ogaji2006@example.com).

## License
© 2025 BellsTech. All rights reserved.
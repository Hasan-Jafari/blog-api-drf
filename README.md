# blog-api-drf
 I still don't have any explanations in mind.
A blog API with posts, categories, tags, comments, and JWT authentication (In development)

## Project Overview
This project is a **Blog API** that allows users to create new posts, view posts, manage categories and tags, and submit comments.

### Key Features
- **JWT & Redis Authentication**: Send and verify OTPs.
- Create and manage posts, categories, and tags.
- Uses **SQLite** for development and **PostgreSQL** for production.

---

## Technologies
- **Python & Django**
- **Django REST Framework (DRF)** for building the API
- **JWT Authentication & Redis** for authentication and token caching
- **PostgreSQL** for production
- **SQLite** for development

---

## Project Architecture & Structure
The project follows a **monolithic architecture** and includes the following apps and modules:

### accounts
- `models.py` → Custom **User** model using AbstractBaseUser with phone number fields
- `managers.py` → User model manager
- `admin.py` → Admin panel configuration

### api
- `views/` → API views for Post, Category, Tag, and Comment
- `endpoints/` → URL definitions using **routers**
- `urls.py` → URLs to (`api/endpoints/`)

### core
- `models/` → Main models (Post, Category, Tag, Comment)
- `serializers/` → Serializers to convert models to JSON
- `filters/` → Filters for posts by category, tag, author, and title
- `paginations/` → API pagination management
- `permissions/` → Permissions and access control (dev in future)
- `validators/` → Phone number and password validations

### utils
- `redis_utils.py` → Redis management for OTP

### config
- `settings/`
  - `base.py` → Base settings
  - `dev.py` → Development settings
  - `pro.py` → Production settings
- `urls.py` → Main API URL (`api/v1/`)

---

## API Endpoints
### Auth Endpoints
- `http://127.0.0.1:8000/api/v1/auth/send-otp/`
- `http://127.0.0.1:8000/api/v1/auth/verify-otp/`
- `http://127.0.0.1:8000/api/v1/auth/refresh-token/`
- `http://127.0.0.1:8000/api/v1/auth/logout/`

### Post Endpoints
- `http://127.0.0.1:8000/api/v1/post/`  --> GET
- `http://127.0.0.1:8000/api/v1/post/` --> POST
- `http://127.0.0.1:8000/api/v1/post/{id}/comments/` --> GET/POST

### Category & Tag Endpoints
- `http://127.0.0.1:8000/api/v1/category/`  --> GET/POST
- `http://127.0.0.1:8000/api/v1/tag/` --> GET/POST

---

## Setup
1. Clone the project:
```bash
git clone https://github.com/Hasan-Jafari/blog-api-drf
cd blog-api-drf

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run the project
python manage.py runserver

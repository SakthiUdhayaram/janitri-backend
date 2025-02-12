<<<<<<< HEAD
# janitri-backend
=======
# Janitri Backend Assignment (Django)

This project implements RESTful APIs for user registration, login, patient management, and heart rate monitoring.

## Features
- User Registration & Login (with email/password validation)
- Patient Management (CRUD)
- Heart Rate Recording & Retrieval
- Uses Django REST Framework (DRF)

## Setup Instructions
1. Clone the repo:
   ```
   git clone <repo-url>
   cd janitri_backend
   ```
2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Start the server:
   ```
   python manage.py runserver
   ```

## API Documentation
- **Register**: `POST /api/users/register/`
- **Login**: `POST /api/users/login/`
- **Patients**:
  - `GET /api/patients/`
  - `POST /api/patients/`
- **Heart Rate**:
  - `GET /api/heart_rates/`
  - `POST /api/heart_rates/`

## Assumptions
- No authentication mechanism is used beyond email/password match.
- No frontend is implemented, only backend APIs.
- Unit tests are optional.
>>>>>>> dff0cfe (Initial commit - Janitri Backend Assignment)

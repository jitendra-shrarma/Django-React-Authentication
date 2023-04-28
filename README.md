# Django-React-Authentication

Django-React-Authentication is a REST API project based on Django and React, providing authentication functionalities such as signup, signin, signout, and reset password. It also includes an API to list users based on the current user group. The project is designed to work with a PostgreSQL database.

## Getting Started

To run the Django-React-Authentication project on your system, please follow these steps:

### Prerequisites

- Python 3.x
- Node.js
- PostgreSQL

### Backend Setup

1. Create a virtual environment:

   ```shell
   python -m venv .venv
   ```

2. Activate the virtual environment:

   - On Windows:

     ```shell
     .venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```shell
     source .venv/bin/activate
     ```

3. Install project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Set up the PostgreSQL database and configure the connection settings in the Django project's settings file (`settings.py`).

5. Apply database migrations:

   ```shell
   python manage.py migrate
   ```

6. Start the Django development server:

   ```shell
   python manage.py runserver
   ```

   The backend API will be accessible at `http://localhost:8000`.

### Frontend Setup

1. Install frontend dependencies:

   ```shell
   cd frontend
   npm install
   ```

2. Start the frontend development server:

   ```shell
   npm start
   ```

   The React application will be accessible at `http://localhost:3000`.

## Project Structure

The Django-React-Authentication project follows the following structure:

- `server/`: Contains the Django backend code.
- `client/`: Contains the React frontend code.
- `requirements.txt`: Lists the Python dependencies for the backend.
- `README.md`: Provides information about the project.

## Technologies Used

The project utilizes the following technologies:

- Django: Backend web framework for handling API requests and database operations.
- React: Frontend JavaScript library for building user interfaces.
- PostgreSQL: Relational database for data storage.
- Django Rest Framework: Toolkit for building RESTful APIs in Django.

Feel free to explore and modify the project to suit your needs.


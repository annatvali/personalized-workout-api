# PERSONALIZED-WORKOUT-API

## Overview

A **RESTful API** to create and manage customized workout plans and track fitness goals. Features include user *authentication*, *predefined exercises*, *personalized workout plans*, *progress tracking*, and *API documentation*.

## Project etup

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/personalized-workout-api.git
   cd personalized-workout-api
   ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    pip install -r requirements-dev.txt  # For developmen dependencies
    ```

4. Install pre-commit hooks:

    ```sh
    pre-commit install
    ```
5. Run the Application

    ```sh
    uvicorn src.main:app --reload
    ```
6. Access the API documentation

    ```sh
    # Open your web browser and navigate to

    http://127.0.0.1:8000/docs

    ```
    or browse the following URL: [https://app.swaggerhub.com/apis/ANNTVALIASHVILI/fast-api/0.1.0](https://app.swaggerhub.com/apis/ANNTVALIASHVILI/fast-api/0.1.0)


7. Docker Setup

    1. Build and run the Docker container:

    ```sh
    docker-compose up --build
    ```

## Tech Stack

- Backend Framework: Python with Flask/Django/**FastAPI**.
- Database: PostgreSQL or **SQLite**.
- Authentication: **JWT for API security**.
- Version Control: **Git**, focusing on a clear and meaningful commit history.

## Functionality

- [x] **User Authentication**: Secure user authentication and authorization.
- [x] **Predefined Exercises**: A database of predefined exercises.
- [x] Personalized Workout Plans: Create and manage personalized workout plans.
- [x] Progress Tracking: Track fitness goals and progress over time.
- [x] API Documentation: Interactive API documentation with Swagger.

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
    python src/main.py
    ```
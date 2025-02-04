# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the application code into container
COPY . .

# expose port
EXPOSE 8000

# run the app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
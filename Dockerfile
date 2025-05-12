# Use official Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy Python files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command: run the GUI app
CMD ["python", "main_gui.py"]

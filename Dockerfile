# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .
# Create a virtual environment and activate it
RUN python -m venv venv
RUN . venv/bin/activate
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Copy the FastAPI server code and the PyTorch model into the container
COPY . /app

# Expose the port your FastAPI server will run on
EXPOSE 8000

# Command to run your FastAPI server using Uvicorn
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]

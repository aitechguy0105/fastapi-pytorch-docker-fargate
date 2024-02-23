
ARG PYTHON_VERSION=3.9.13
FROM python:${PYTHON_VERSION}-slim as base

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY linear_model.pth .
COPY torch-2.2.0+cpu-cp39-cp39-linux_x86_64.whl .
COPY server.py .
COPY LinearRegressionModel.py .
# Install any dependencies specified in requirements.txt
RUN pip install torch-2.2.0+cpu-cp39-cp39-linux_x86_64.whl
RUN pip install --no-cache-dir fastapi==0.109.2
RUN pip install --no-cache-dir uvicorn==0.27.1


# Expose the port that your FastAPI server will run on
EXPOSE 8000

# Command to run your FastAPI server when the container starts
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
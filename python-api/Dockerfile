FROM python:3.11-slim
# Better performance than Alpine for Python

WORKDIR /code

# Install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt && \
    python -m compileall -q /code  # Precompile bytecode

# Copy application code
COPY ./app /code/app

# Expose the port the app runs on
EXPOSE 8000

# Command to run with performance optimizations
CMD ["python", "-O", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "2", "--no-access-log", "--no-use-colors"]
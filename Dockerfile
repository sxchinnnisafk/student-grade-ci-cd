FROM python:3.12-slim

WORKDIR /app
COPY app.py ./app.py

# The program uses only the Python standard library.
CMD ["python", "app.py"]

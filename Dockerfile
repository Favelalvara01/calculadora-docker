# syntax=docker/dockerfile:1
# check=error=true

FROM python:3.12-slim

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]

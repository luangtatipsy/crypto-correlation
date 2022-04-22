FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 80
COPY ./app /app
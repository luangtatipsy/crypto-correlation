FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir pandas pycoingecko jinja2

EXPOSE 80
COPY ./app /app
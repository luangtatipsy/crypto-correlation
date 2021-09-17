FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir pandas pycoingecko jinja2

EXPOSE 80
COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
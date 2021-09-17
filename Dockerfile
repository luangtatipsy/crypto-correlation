FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /crypto-correlation

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir pandas pycoingecko jinja2

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
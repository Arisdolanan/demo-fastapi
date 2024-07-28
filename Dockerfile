FROM python:3.12.4-slim

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install cryptography
RUN pip install faker

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000"]

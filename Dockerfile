FROM python3.
COPY ./app
WORKDIR /app
python3 main.py


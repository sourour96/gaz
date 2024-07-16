FROM python:3.9-slim

RUN apt-get update \
    && apt-get install -y python3-dev build-essential \
    && pip install --upgrade pip

RUN pip install RPi.GPIO==0.7.1a4 firebase-admin==6.5.0

WORKDIR /usr/src/app

COPY . .

EXPOSE 80

CMD ["python", "./Gaz.py"]































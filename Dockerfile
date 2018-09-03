FROM python:latest

ENV PYTHONBUFFERED 1

WORKDIR /src

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

RUN chmod a+x run-production.sh

ENV IS_PRODUCTION 1

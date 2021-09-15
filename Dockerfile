# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /source_code/
COPY requirements.txt /source_code/
COPY ./manage.py /source_code/
RUN pip install -r requirements.txt
COPY . /source_code/

EXPOSE 8001
CMD python manage.py makemigrations
CMD python manage.py migrate
CMD python manage.py runserver
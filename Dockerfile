FROM python:3.10.10

ARG SECRET_KEY=${SECRET_KEY}

ENV PYTHONUNBUFFERED 1
ENV HOME_PROJECT=/server

ENV DJANGO_WSGI_MODULE=app.wsgi
ENV BIND=0.0.0.0:8000
ENV NUM_WORKERS=4


WORKDIR /server

COPY ./app .
COPY ./requirements.txt .

EXPOSE 8000

RUN apt-get update && \
    pip install -r requirements.txt

RUN chmod +x ./gunicorn_entrypoint.sh
RUN python manage.py collectstatic --noinput --clear
CMD python manage.py makemigrations && python manage.py migrate && ./gunicorn_entrypoint.sh
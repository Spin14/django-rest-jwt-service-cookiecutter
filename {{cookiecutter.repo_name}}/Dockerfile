FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN pip3.6 install pipenv

COPY . code
WORKDIR /code
RUN pipenv install --system --dev

EXPOSE 8000

CMD cd {{cookiecutter.app_name}} && python manage.py migrate && gunicorn --bind 0.0.0.0:8000 --access-logfile - {{cookiecutter.app_name}}.wsgi:application

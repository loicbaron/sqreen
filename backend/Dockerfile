# WARNING: run with a dedicated user instead of priviledge one

FROM python:3.8
WORKDIR /code

# Sqreen/PyMiniRacer build breaks with image python:3.8-alpine
# https://github.com/sqreen/PyMiniRacer#binary-builds-availability
# RUN apk add python2 libgcc libstdc++

COPY sqreen.ini sqreen.ini
COPY .env .env

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./project ./project
COPY ./test ./test
COPY *.py ./

# RUN FOR DEV
# WARNING: This is a development server. Do not use it in a production deployment.
# ENTRYPOINT ["python", "run.py"]

# RUN FOR PROD
ENTRYPOINT ["gunicorn", "wsgi:app", "-w", "4", "-b", "0.0.0.0:8000"]
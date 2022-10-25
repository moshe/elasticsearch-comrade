FROM python:3.11.0-slim@sha256:f8cc89f5e47347703ec0c2b755464d7db2fa16f255ab860c4b24ba6ef2402020
WORKDIR /app
COPY setup.py MANIFEST.in Pipfile* ./
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python-dev g++ make build-essential libssl-dev libffi-dev python3-dev cargo &&\
    mkdir /app/comrade && \
    pip install pipenv && \
    pipenv install -e . --skip-lock && \
    apt-get purge -y --auto-remove gcc python-dev g++ make libffi-dev libssl-dev && \
    find /usr/local/lib/python3.7/ -type d -name __pycache__ | xargs rm -rf && \
    find /root/.local/ -type d -name __pycache__ | xargs rm -rf && \
    rm -rf ~/.cache /var/cache && \
    rm -rf /var/lib/apt/lists/*
COPY comrade/ /app/comrade/
EXPOSE 8000
CMD pipenv run comrade

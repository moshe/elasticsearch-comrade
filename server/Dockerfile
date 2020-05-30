FROM python:3.8.3-slim@sha256:87e7a5744fa7df0b441abebf63c0d27c86fd1ceb109e849ea9ccd82cf27abb65
WORKDIR /app
COPY setup.py MANIFEST.in server/Pipfile* ./
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python-dev g++ make libffi-dev libssl-dev &&\
    mkdir /app/comrade && \
    pip install pipenv && \
    pipenv install -e . --skip-lock && \
    apt-get purge -y --auto-remove gcc python-dev g++ make libffi-dev libssl-dev && \
    find /usr/local/lib/python3.7/ -type d -name __pycache__ | xargs rm -rf && \
    find /root/.local/ -type d -name __pycache__ | xargs rm -rf && \
    rm -rf ~/.cache /var/cache && \
    rm -rf /var/lib/apt/lists/*
COPY server/ /app/comrade/
EXPOSE 8000
CMD pipenv run comrade

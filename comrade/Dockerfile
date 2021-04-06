FROM python:3.9.4-slim@sha256:1e046bca10e9187236f8c52830da166111a465842d6450fcd52863eebd216db7
WORKDIR /app
COPY setup.py MANIFEST.in Pipfile* ./
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
COPY comrade/ /app/comrade/
EXPOSE 8000
CMD pipenv run comrade

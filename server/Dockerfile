FROM python:3.8.2-alpine@sha256:b57a7416bfe585015ed06db89cb25d3b9ec08d97ddee0e51f9d39d2ff7bfac58
WORKDIR /app
COPY setup.py MANIFEST.in server/Pipfile* ./
RUN apk add --no-cache gcc libc-dev make libffi-dev libressl-dev && \
    mkdir /app/comrade && \
    pip install pipenv && \
    pipenv install -e . --skip-lock && \
    apk del gcc make libc-dev libffi-dev libressl-dev && \
    rm -rf ~/.cache /var/cache && \
    find /usr/local/lib/python3.7/ -type d -name __pycache__ | xargs rm -rf && \
    find /root/.local/ -type d -name __pycache__ | xargs rm -rf
COPY server/ /app/comrade/
EXPOSE 8000
CMD pipenv run comrade

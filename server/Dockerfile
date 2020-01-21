FROM python:3.8.1-alpine@sha256:f21927aab8cd2535ee708e0945e70579143857f7df2e661d19f6d05bc5941063
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

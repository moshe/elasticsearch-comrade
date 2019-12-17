FROM python:3.8.0-alpine@sha256:3996a4b86240b6d41b57055cd7f626cbb15e2baef149b4fd841e04fec7308290
WORKDIR /app
COPY server/Pipfile* ./
RUN apk add --no-cache gcc libc-dev make && \
    pip install pipenv && \
    pipenv install && \
    apk del gcc make libc-dev && \
    rm -rf ~/.cache /var/cache && \
    find /usr/local/lib/python3.7/ -type d -name __pycache__ | xargs rm -rf && \
    find /root/.local/ -type d -name __pycache__ | xargs rm -rf
COPY server/ /app/comrade/
COPY setup.py MANIFEST.in /app/
EXPOSE 8000
RUN pipenv install -e . --skip-lock
CMD pipenv run comrade

FROM python:3.7.4-alpine@sha256:488bfa82d8ac22f1ed9f1d4297613a920bf14913adb98a652af7dbbbf1c3cab9
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

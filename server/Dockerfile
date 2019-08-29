FROM python:3.7.4-alpine@sha256:488bfa82d8ac22f1ed9f1d4297613a920bf14913adb98a652af7dbbbf1c3cab9
WORKDIR /app
COPY server/Pipfile* ./
RUN apk add --no-cache gcc libc-dev make && \
    pip install pipenv && \
    pipenv install && \
    apk del gcc make libc-dev && \
    rm -rf ~/.cache /var/cache
COPY server/ .
EXPOSE 8000
CMD pipenv run python index.py

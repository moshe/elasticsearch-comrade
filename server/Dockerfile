FROM python:3.7-alpine
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

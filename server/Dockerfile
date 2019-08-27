FROM python:3.7-alpine@sha256:9363cb46e52894a22ba87ebec0845d30f4c27efd6b907705ba9a27192b45e797
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

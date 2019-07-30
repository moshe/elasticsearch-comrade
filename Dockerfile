FROM node:12-alpine AS client

WORKDIR /usr/src/app
COPY client/package*.json ./
RUN npm ci --only=production && npm install @vue/cli
ADD client/ ./
RUN npm run build

FROM python:3.7-alpine
WORKDIR /app
COPY server/Pipfile* ./
RUN apk add --no-cache gcc libc-dev make && \
    pip install pipenv && \
    pipenv install && \
    apk del gcc make libc-dev && \
    rm -rf ~/.cache /var/cache
COPY --from=client /usr/src/app/dist/ /app/static/
COPY server/ .
EXPOSE 8000
CMD pipenv run python index.py

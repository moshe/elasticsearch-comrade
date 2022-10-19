FROM node:19-alpine AS client

WORKDIR /usr/src/app
COPY client/package*.json ./
RUN npm ci
ADD client/ ./

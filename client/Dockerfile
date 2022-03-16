FROM node:17-alpine AS client

WORKDIR /usr/src/app
COPY client/package*.json ./
RUN npm ci
ADD client/ ./

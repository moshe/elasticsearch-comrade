FROM node:13-alpine AS client

WORKDIR /usr/src/app
COPY client/package*.json ./
RUN npm ci
ADD client/ ./

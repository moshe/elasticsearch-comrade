FROM node:18-alpine AS client

WORKDIR /usr/src/app
COPY client/package*.json ./
RUN npm ci
ADD client/ ./

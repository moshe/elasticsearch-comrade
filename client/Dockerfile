FROM node:14-alpine AS client

WORKDIR /usr/src/app
COPY client/package*.json ./
RUN npm ci
ADD client/ ./

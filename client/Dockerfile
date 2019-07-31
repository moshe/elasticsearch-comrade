FROM node:12-alpine AS client

WORKDIR /usr/src/app
COPY client/package*.json ./
RUN npm ci --only=production && npm install @vue/cli
ADD client/ ./
RUN echo npm run build

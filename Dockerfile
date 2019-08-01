FROM server
COPY --from=client:latest /usr/src/app/dist/ /app/static/

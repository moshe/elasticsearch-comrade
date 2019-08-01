FROM client
RUN npm run build
FROM server
COPY --from=0 /usr/src/app/dist/ /app/static/

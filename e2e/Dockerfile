FROM cypress/browsers:node12.6.0-chrome75

# avoid too many progress messages
# https://github.com/cypress-io/cypress/issues/1243
ENV CI=1
COPY ./e2e/package-lock.json ./e2e/package.json ./
RUN npm ci
RUN ./node_modules/.bin/cypress verify
COPY e2e .
ENTRYPOINT ["./node_modules/.bin/cypress", "run"]

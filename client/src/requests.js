import state from "./store";

export class RequestError extends Error {
  constructor(args = {}, ...params) {
    super(...params);
    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, RequestError);
    }

    this.name = "RequestError";
    this.args = args;
  }
}

function headers(additional) {
  return { "X-Elastic-Cluster": state.state.connectedCluster, ...additional };
}

async function request(showError, ...args) {
  let response;
  let content;
  try {
    response = await fetch(...args);
    content = await response.json();
  } catch (e) {
    if (showError) {
      state.commit("setErrorBarContent", { type: "HTTP error", body: e });
    }
    throw new RequestError({ type: "HTTP error", body: e });
  }
  if (content && content.error) {
    if (showError) {
      state.commit("setErrorBarContent", {
        type: content.type || "Server Error",
        body: content.error
      });
    }
    throw new RequestError({
      type: content.type || "Server Error",
      body: content.error
    });
  }
  return content;
}

export async function GET(url, showError = true) {
  return request(showError, url, { headers: headers() });
}

export async function POST(url, body, showError = true) {
  return request(showError, url, {
    method: "POST",
    headers: headers({
      Accept: "application/json",
      "Content-Type": "application/json"
    }),
    body: JSON.stringify(body)
  });
}

import state from "./store";

function headers(additional) {
  return { "X-Elastic-Cluster": state.state.connectedCluster, ...additional };
}

async function request(...args) {
  let response;
  try {
    response = await fetch(...args);
    const content = await response.json();
    if (content.error) {
      state.commit("setErrorBarContent", {
        type: content.type || "Server Error",
        body: content.error
      });
    }
    return content;
  } catch (e) {
    state.commit("setErrorBarContent", { type: "HTTP error", body: e });
  }
}

export async function GET(url) {
  return request(url, { headers: headers() });
}

export async function POST(url, body) {
  return request(url, {
    method: "POST",
    headers: headers({
      Accept: "application/json",
      "Content-Type": "application/json"
    }),
    body: JSON.stringify(body)
  });
}

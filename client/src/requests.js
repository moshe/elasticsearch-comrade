import state from "./store";

function headers(additional) {
  return { "X-Elastic-Cluster": state.state.connectedCluster, ...additional };
}
export async function GET(url) {
  return (await fetch(url, {
    headers: headers()
  })).json();
}

export async function POST(url, body) {
  return (await fetch(url, {
    method: "POST",
    headers: headers({
      Accept: "application/json",
      "Content-Type": "application/json"
    }),
    body: JSON.stringify(body)
  })).json();
}

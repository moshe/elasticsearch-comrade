export async function GET(url) {
  return (await fetch(url)).json();
}

export async function POST(url, body) {
  return (await fetch(url, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json"
    },
    body: JSON.stringify(body)
  })).json();
}

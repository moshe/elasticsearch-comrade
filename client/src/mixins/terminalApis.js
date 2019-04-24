export default {
  methods: {
    async sendQuery(method, url, body) {
      const res = await fetch("/api/v1/terminal/query", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          method,
          url,
          body
        })
      });
      return res.json();
    }
  }
};

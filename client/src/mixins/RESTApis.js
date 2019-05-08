import { POST } from "../requests";

export default {
  methods: {
    async sendQuery(method, url, body) {
      return POST("/api/v1/rest/query", { method, url, body });
    }
  }
};

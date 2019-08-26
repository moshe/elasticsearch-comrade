import { POST } from "../requests";

export default {
  methods: {
    async sendQuery(method, path, body, showError = false) {
      return POST("/api/v1/rest/query", { method, path, body }, showError);
    }
  }
};

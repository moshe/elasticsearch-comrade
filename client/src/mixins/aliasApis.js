import { GET, POST } from "../requests";

export default {
  methods: {
    async listAliases() {
      return GET("/api/v1/alias/list");
    },
    async updateAliases(actions) {
      return POST("/api/v1/alias/batch", { actions });
    }
  }
};

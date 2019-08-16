import { GET, POST } from "../requests";

export default {
  methods: {
    async listAliases() {
      return GET("/api/v1/alias/list");
    },
    async updateAliases(actions) {
      this.$store.commit("startLoading");
      const response = await POST("/api/v1/alias/batch", { actions });
      await this.$store.dispatch("shardsGrid");
      this.$store.commit("stopLoading");
      return response;
    }
  }
};

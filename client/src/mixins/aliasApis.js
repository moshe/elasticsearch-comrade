import { POST } from "../requests";

export default {
  methods: {
    async updateAliases(actions) {
      this.$store.commit("startLoading");
      const response = await POST("/api/v1/alias/batch", { actions });
      await this.$store.dispatch("shardsGrid");
      this.$store.commit("stopLoading");
      return response;
    }
  }
};

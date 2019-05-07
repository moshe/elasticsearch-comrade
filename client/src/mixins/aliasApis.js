import { POST } from "../requests";

export default {
  methods: {
    async createAlias({
      aliasName,
      selectedIndices,
      filter,
      indexRouting,
      searchRouting
    }) {
      this.$store.commit("startLoading");
      const response = POST("/api/v1/alias/create", {
        alias: aliasName,
        indices: selectedIndices,
        filter,
        indexRouting,
        searchRouting
      });
      await this.$store.dispatch("shardsGrid");
      this.$store.commit("stopLoading");
      return response;
    }
  }
};

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
      return POST("/api/v1/alias/create", {
        alias: aliasName,
        indices: selectedIndices,
        filter,
        indexRouting,
        searchRouting
      });
    }
  }
};

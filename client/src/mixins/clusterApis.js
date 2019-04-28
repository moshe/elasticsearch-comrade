import { POST } from "../requests";

export default {
  methods: {
    async setAllocation(option) {
      return POST(`/api/v1/cluster/allocation/${option}`, {});
    }
  }
};

import { GET } from "../requests";

export default {
  methods: {
    async getNodeInfo(nodeId) {
      return await GET(`/api/v1/node/${nodeId}/info`);
    },
    async getNodeStats(nodeId) {
      return await GET(`/api/v1/node/${nodeId}/stats`);
    }
  }
};

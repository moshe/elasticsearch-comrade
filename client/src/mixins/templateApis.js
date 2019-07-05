import { GET, POST } from "../requests";

export default {
  methods: {
    async listTemplates() {
      return GET("/api/v1/template/list");
    },
    async cancleTask(taskId) {
      return POST("/api/v1/task/cancle", { taskId });
    }
  }
};

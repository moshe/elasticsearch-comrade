import { GET, POST } from "../requests";

export default {
  methods: {
    async listTasks() {
      return GET("/api/v1/task/list");
    },
    async cancelTask(taskId) {
      return POST("/api/v1/task/cancel", { taskId });
    }
  }
};

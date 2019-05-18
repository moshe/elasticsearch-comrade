import { GET, POST } from "../requests";

export default {
  methods: {
    async listTasks() {
      return GET("/api/v1/task/list");
    },
    async cancleTask(taskId) {
      return POST("/api/v1/task/cancle", { taskId });
    }
  }
};

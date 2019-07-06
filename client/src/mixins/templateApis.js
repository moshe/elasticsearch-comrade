import { GET, POST } from "../requests";

export default {
  methods: {
    async listTemplates() {
      return GET("/api/v1/template/list");
    },
    async deleteTemplate(templateName) {
      return GET(`/api/v1/template/${templateName}/delete`);
    },
    async updateTemplate(templateName, body) {
      return POST(`/api/v1/template/${templateName}/update`, body);
    },
    async createTemplate(templateName, body) {
      return POST(`/api/v1/template/${templateName}/create`, body);
    }
  }
};

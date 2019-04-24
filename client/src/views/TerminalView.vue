<template>
  <v-container>
    <v-layout>
      <v-flex style="flex: 2">
        <v-autocomplete
          v-model="method"
          :items="['GET', 'POST', 'DELETE']"
          label="Method"
          persistent-hint
        />
      </v-flex>
      <v-flex style="flex: 10" class="ml-3">
        <v-text-field clearable label="URL" v-model="url" />
      </v-flex>
      <v-flex style="flex: 1">
        <v-btn color="info" @click="onClick">Send</v-btn>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex style="flex:1;" class="mr-3">
        <query-editor ref="editor" />
      </v-flex>
      <v-flex style="flex:1">
        <v-textarea
          name="input-7-1"
          color="#1e1e1e"
          rows="20"
          label="Response"
          readonly
          v-model="response"
          hint="Hint text"
          outline
        ></v-textarea>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import QueryEditor from "../components/Terminal/QueryEditor";
import terminalApis from "../mixins/terminalApis";

export default {
  name: "QueryView",
  components: { QueryEditor },
  mixins: [terminalApis],
  data() {
    return {
      response: "{}",
      method: "GET",
      url: "/"
    };
  },
  methods: {
    async onClick() {
      console.log(this.$refs.editor.getQuery());
      const resp = await this.sendQuery(
        this.method,
        this.url,
        this.$refs.editor.getQuery()
      );
      this.response = JSON.stringify(resp, null, 2);
    }
  }
};
</script>

<style></style>

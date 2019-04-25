<template>
  <v-container>
    <v-layout>
      <v-flex style="flex: 2">
        <v-autocomplete
          v-model="method"
          :items="['GET', 'POST', 'DELETE', 'HEAD']"
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
      <v-slide-x-transition>
        <v-flex class="mr-3" style="flex: 10" v-show="panes.includes('editor')">
          <query-editor ref="editor" />
        </v-flex>
      </v-slide-x-transition>
      <v-flex shrink>
        <terminal-buttons style="margin-top: 20px" :panes.sync="panes" />
      </v-flex>
      <v-slide-x-reverse-transition>
        <v-flex v-show="panes.includes('preview')" style="flex: 10">
          <query-editor ref="preview" read-only />
        </v-flex>
      </v-slide-x-reverse-transition>
    </v-layout>
  </v-container>
</template>

<script>
import QueryEditor from "../components/Terminal/QueryEditor";
import terminalApis from "../mixins/terminalApis";
import TerminalButtons from "../components/Terminal/TerminalButtons";

export default {
  name: "QueryView",
  components: { TerminalButtons, QueryEditor },
  mixins: [terminalApis],
  data() {
    return {
      response: null,
      method: "GET",
      url: "/",
      panes: ["preview", "editor"]
    };
  },
  methods: {
    async onClick() {
      const resp = await this.sendQuery(
        this.method,
        this.url,
        this.$refs.editor.getQuery()
      );
      this.$refs.preview.setContent(resp);
    }
  }
};
</script>

<style></style>

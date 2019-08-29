<template>
  <v-hover>
    <template v-slot:default="{ hover }">
      <div>
        <v-header sub>SQL Editor (Beta)</v-header>
        <div class="pane" id="editor">SELECT * from "index" LIMIT 100</div>
        <v-row justify="end">
          <v-col style="flex-grow: 0">
            <v-btn color="success" @click="executeQuery" v-text="'Run'" />
          </v-col>
        </v-row>
        <div>
          <v-header sub>Results</v-header>
          <v-data-table :headers="headers" :items="items" class="elevation-1" />
        </div>
        <v-fade-transition>
          <v-overlay
            v-if="!$store.state.clusterVersion.startsWith('7')"
            absolute
            opacity="0.8"
          >
            <div
              style="background-color: rgba(0,0,0,0.3); border-radius: 10px; font-size:18px"
              class="pa-9"
            >
              SQL is a version 7 only feature
            </div>
          </v-overlay>
        </v-fade-transition>
      </div>
    </template>
  </v-hover>
</template>

<script>
import RESTApis from "../mixins/RESTApis";
import VHeader from "../components/Base/Header.vue";

var ace = require("brace");
require("brace/mode/sql");
require("brace/theme/monokai");
export default {
  mixins: [RESTApis],
  components: { VHeader },
  mounted() {
    this.editor = ace.edit("editor");
    this.editor.getSession().setMode("ace/mode/sql");
    this.editor.setTheme("ace/theme/monokai");
  },
  data() {
    return {
      editor: null,
      headers: [],
      items: []
    };
  },
  methods: {
    async executeQuery() {
      const query = this.editor.getValue();
      const resp = await this.sendQuery("POST", "/_sql", { query }, true);
      this.headers = resp.columns.map(x => ({ text: x.name, value: x.name }));
      this.items = resp.rows.map(row =>
        Object.fromEntries(
          row.map((col, i) => [
            resp.columns[i].name,
            col == null ? "null" : col
          ])
        )
      );
    }
  }
};
</script>

<style scoped>
.pane {
  height: 50vh;
}
</style>

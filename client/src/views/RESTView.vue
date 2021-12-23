<template>
  <div>
    <v-layout align-baseline>
      <v-flex style="flex: 2">
        <v-autocomplete
          v-model="method"
          :items="['GET', 'POST', 'DELETE', 'HEAD', 'PUT']"
          label="Method"
        />
      </v-flex>
      <v-flex style="flex: 10" class="ml-4">
        <endpoint-auto-completer
          @change="selectRoute"
          :method="method"
          :path="path"
        />
      </v-flex>
      <v-flex style="flex: 1" class="ml-4">
        <v-btn color="success" @click="onClick">Send</v-btn>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex
        class="mr-4"
        style="margin-top:48px; flex:1"
        v-show="panes.includes('editor')"
      >
        <query-editor
          style="height: 700px;"
          ref="editor"
          @execute="onClick"
          :init="init.body"
        />
      </v-flex>
      <v-flex shrink>
        <r-e-s-t-buttons style="margin-top: 70px" :panes.sync="panes" />
      </v-flex>
      <v-flex style="flex: 1" v-show="panes.includes('preview')">
        <v-tabs background-color="bg-color">
          <v-tab>Response</v-tab>
          <v-tab>History</v-tab>
          <v-tab>Starred</v-tab>
          <v-tab-item eager>
            <query-editor style="height: 700px;" ref="preview" read-only v-if="json_result"/>
            <rest-table v-bind:result-data="resultData" v-if="cat_result"/>
          </v-tab-item>
          <v-tab-item eager>
            <query-history
              @query="setQueryFromHistory"
              ref="history"
              storeName="history"
              @star="x => $refs.starred.addEntry(x)"
            />
          </v-tab-item>
          <v-tab-item eager>
            <query-history
              @query="setQueryFromHistory"
              ref="starred"
              storeName="starred"
            />
          </v-tab-item>
        </v-tabs>
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import RESTApis from "../mixins/RESTApis";
import QueryEditor from "../components/Base/QueryEditor.vue";
import RESTButtons from "../components/REST/RESTButtons.vue";
import EndpointAutoCompleter from "../components/REST/EndpointAutoCompleter.vue";
import QueryHistory from "../components/REST/QueryHistory.vue";
import RestTable from '../components/REST/RestTable.vue';


export default {
  components: { EndpointAutoCompleter, RESTButtons, QueryEditor, QueryHistory, RestTable },
  mixins: [RESTApis],
  props: {
    init: {
      type: Object,
      default: () => ({ body: {} })
    }
  },
  data() {
    return {
      resultData: null,
      json_result: true,
      cat_result: false,
      response: null,
      method: this.init.method || "GET",
      path: this.init.path || "/",
      panes: ["preview", "editor"]
    };
  },
  methods: {
    setQueryFromHistory({ path, query, method }) {
      this.method = method;
      this.selectRoute({ path, template: query });
    },
    selectRoute({ path, template }) {
      this.path = path;
      if (template) {
        this.$refs.editor.setContent(template);
      }
    },
    async onClick() {
      // FIXME: Ugly hack in order to make endpoint completer to work when adding custom urls
      this.path = document.querySelector("#endpoint-selector")._value;
      this.$refs.history.addEntry({
        method: this.method,
        path: this.path,
        query: this.$refs.editor.getQuery(),
        date: Date.now()
      });
      let resp = null;
      try {
        resp = await this.sendQuery(
          this.method,
          this.path,
          this.$refs.editor.getQuery()
        );
      } catch (error) {
        resp = error;
      }
      if (resp.hasOwnProperty("table")) {
          this.json_result = false
          this.cat_result = true
          this.resultData = resp.table
          return
      };
      this.json_result = true
      this.$refs.preview.setContent(resp);
    }
  },
  watch: {
    panes() {
      setTimeout(() => {
        this.$refs.editor.refresh();
        this.$refs.preview.refresh();
      }, 310);
    }
  }
};
</script>

<style></style>

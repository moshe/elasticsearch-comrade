<template>
  <div>
    <v-layout>
      <v-flex style="flex: 2">
        <v-autocomplete
          v-model="method"
          :items="['GET', 'POST', 'DELETE', 'HEAD']"
          label="Method"
          autofocus
        />
      </v-flex>
      <v-flex style="flex: 10" class="ml-3">
        <endpoint-auto-completer
          @change="selectRoute"
          :method="method"
          :path="path"
        />
      </v-flex>
      <v-flex style="flex: 1">
        <v-btn color="info" @click="onClick">Send</v-btn>
      </v-flex>
    </v-layout>
    <v-layout>
      <transition name="slide-fade-reverse">
        <v-flex
          class="mr-3"
          style="flex: 10; margin-top:48px"
          v-show="panes.includes('editor')"
        >
          <query-editor
            style="height: 800px;"
            ref="editor"
            @execute="onClick"
          />
        </v-flex>
      </transition>
      <v-flex shrink>
        <r-e-s-t-buttons style="margin-top: 20px" :panes.sync="panes" />
      </v-flex>
      <transition name="slide-fade">
        <v-flex v-show="panes.includes('preview')" style="flex: 10">
          <v-tabs color="#303030">
            <v-tab>Response</v-tab>
            <v-tab>History</v-tab>
            <v-tab>Starred</v-tab>
            <v-tab-item>
              <query-editor style="height: 800px;" ref="preview" read-only />
            </v-tab-item>
            <v-tab-item>
              <query-history
                @query="setQueryFromHistory"
                ref="history"
                storeName="history"
                @star="x => $refs.starred.addEntry(x)"
              />
            </v-tab-item>
            <v-tab-item>
              <query-history
                @query="setQueryFromHistory"
                ref="starred"
                storeName="starred"
              />
            </v-tab-item>
          </v-tabs>
        </v-flex>
      </transition>
    </v-layout>
  </div>
</template>

<script>
import RESTApis from "../mixins/RESTApis";
import QueryEditor from "../components/Base/QueryEditor.vue";
import RESTButtons from "../components/REST/RESTButtons.vue";
import EndpointAutoCompleter from "../components/REST/EndpointAutoCompleter.vue";
import QueryHistory from "../components/REST/QueryHistory.vue";

export default {
  name: "QueryView",
  components: { EndpointAutoCompleter, RESTButtons, QueryEditor, QueryHistory },
  mixins: [RESTApis],
  data() {
    return {
      response: null,
      method: "GET",
      path: "/",
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
      this.$refs.editor.setContent(template || {});
    },
    async onClick() {
      this.$refs.history.addEntry({
        method: this.method,
        path: this.path,
        query: this.$refs.editor.getQuery(),
        date: Date.now()
      });
      const resp = await this.sendQuery(
        this.method,
        this.path,
        this.$refs.editor.getQuery()
      );
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

<style>
.slide-fade-enter-active,
.slide-fade-reverse-enter-active {
  transition: all 0.3s ease;
}
.slide-fade-leave-active,
.slide-fade-reverse-leave-active {
  transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
}
.slide-fade-enter,
.slide-fade-leave-to {
  transform: translateX(600px);
  opacity: 0;
}

.slide-fade-reverse-enter,
.slide-fade-reverse-leave-to {
  transform: translateX(-600px);
  opacity: 0;
}
</style>

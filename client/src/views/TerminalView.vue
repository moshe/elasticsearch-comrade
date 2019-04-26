<template>
  <v-container>
    <v-layout>
      <v-flex style="flex: 2">
        <v-autocomplete
          v-model="method"
          :items="['GET', 'POST', 'DELETE', 'HEAD']"
          label="Method"
        />
      </v-flex>
      <v-flex style="flex: 10" class="ml-3">
        <v-combobox
          :items="endpoints"
          clearable
          autofocus
          label="URL"
          v-model="url"
          item-text="path"
        >
          <template v-slot:item="{ index, item }">
            <v-list-tile-content>
              <v-chip :color="`gray lighten-3`" dark label small>
                {{ item.method }} {{ item.path }}
              </v-chip>
            </v-list-tile-content>
            <v-list-tile-action>
              <v-chip :color="`gray lighten-3`" dark label small>
                {{ item.name }}
              </v-chip>
            </v-list-tile-action>
          </template>
        </v-combobox>
      </v-flex>
      <v-flex style="flex: 1">
        <v-btn color="info" @click="onClick">Send</v-btn>
      </v-flex>
    </v-layout>
    <v-layout>
      <transition name="slide-fade-reverse">
        <v-flex class="mr-3" style="flex: 10" v-show="panes.includes('editor')">
          <query-editor ref="editor" />
        </v-flex>
      </transition>
      <v-flex shrink>
        <terminal-buttons style="margin-top: 20px" :panes.sync="panes" />
      </v-flex>
      <transition name="slide-fade">
        <v-flex v-show="panes.includes('preview')" style="flex: 10">
          <query-editor ref="preview" read-only />
        </v-flex>
      </transition>
    </v-layout>
  </v-container>
</template>

<script>
import QueryEditor from "../components/Terminal/QueryEditor";
import terminalApis from "../mixins/terminalApis";
import TerminalButtons from "../components/Terminal/TerminalButtons";
import endpoints from "../assets/elasticsearch_endpoints";
import { mapState } from "vuex";

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
  computed: {
    ...mapState(["indices"]),
    endpoints() {
      return endpoints.flatMap(this.expandIndices);
    }
  },
  methods: {
    expandIndices(route) {
      const indices = Object.keys(this.indices);
      if (route.path.includes("{index}")) {
        return indices.map(x => {
          return { ...route, path: route.path.replace("{index}", x) };
        });
      }
      return route;
    },
    async onClick() {
      const resp = await this.sendQuery(
        this.method,
        this.url,
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

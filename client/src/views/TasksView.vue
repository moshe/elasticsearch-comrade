<template>
  <v-layout column>
    <v-flex>
      <v-layout row wrap>
        <v-flex>
          <v-combobox
            :items="actions"
            autofocus
            ref="filter"
            clearable
            label="Filter (Regex Supported)"
            @change="filterAction"
          />
        </v-flex>
      </v-layout>
    </v-flex>
    <v-flex class="mb-2">
      <v-chip
        v-for="filter in filters"
        :key="filter"
        color="green"
        close
        small
        class="mr-2"
        @click:close="removeFilter(filter, 'filters')"
      >
        {{ filter }}
      </v-chip>
      <v-chip
        v-for="filter in notFilters"
        :key="filter"
        color="red"
        close
        small
        class="mr-2"
        @click:close="removeFilter(filter, 'notFilters')"
      >
        {{ filter }}
      </v-chip>
    </v-flex>
    <v-flex>
      <v-data-table
        :headers="headers"
        :items="filteredTasks"
        class="elevation-1 small-table"
        item-key="taskId"
        show-expand
        :footer-props="{ 'items-per-page-options': [30, 100, 200] }"
      >
        <template v-slot:item.cancellable="{ item }">
          <v-btn icon :disabled="!item.cancellable" small @click="cancleTask">
            <v-icon>clear</v-icon>
          </v-btn>
        </template>
        <template v-slot:expanded-item="{ item }">
          <code>{{ JSON.stringify(item, 0, 2) }}</code>
        </template>
      </v-data-table>
    </v-flex>
  </v-layout>
</template>

<script>
import { mapState } from "vuex";
import actions from "../assets/elasticsearch_actions.json";
import taskApis from "../mixins/taskApis";
export default {
  mixins: [taskApis],
  data() {
    return {
      value: "",
      actions: actions.flatMap(x => [x, "!" + x]),
      filters: [],
      tasks: [],
      notFilters: [],
      timeout: null,
      headers: [
        { text: "Expand", value: "expend" },
        { text: "taskId", value: "taskId" },
        { text: "Action", value: "action" },
        { text: "Node", value: "nodeName" },
        { text: "Cancle", value: "cancellable" }
      ]
    };
  },
  async created() {
    this.refreshTasks(true);
  },
  destroyed() {
    clearTimeout(this.timeout);
  },
  computed: {
    ...mapState(["settingsRefreshEvery", "settingsRefreshEnabled"]),
    filteredTasks() {
      return this.tasks.filter(({ action }) => {
        const negativeConditionsMatched = this.notFilters.some(filter =>
          RegExp(filter).test(action)
        );
        if (negativeConditionsMatched) {
          return false;
        }
        const possitiveConditionsMatched = this.filters.some(filter =>
          RegExp(filter).test(action)
        );
        if (this.filters.length !== 0 && !possitiveConditionsMatched) {
          return false;
        }
        return true;
      });
    }
  },
  methods: {
    async refreshTasks(force) {
      if (this.settingsRefreshEnabled || force) {
        this.tasks = await this.listTasks();
      }
      this.timeout = setTimeout(this.refreshTasks, this.settingsRefreshEvery);
    },
    filterAction(selected) {
      if (!selected) {
        return;
      }
      this.$refs.filter.blur();
      if (selected.startsWith("!")) {
        const filter = selected.substr(1);
        this.removeFilter(filter, "filters");
        this.notFilters.push(selected.substr(1));
        return;
      }
      this.removeFilter(selected, "notFilters");
      this.filters.push(selected);
    },
    removeFilter(filter, type) {
      this[type] = this[type].filter(x => x !== filter);
    }
  }
};
</script>

<style scoped>
.expand {
  overflow: hidden;
  transition-duration: 0.4s;
  transition-property: transform;
}

.expand:hover {
  transform: rotate(90deg);
  -webkit-transform: rotate(90deg);
}

.expanded {
  transform: rotate(90deg);
}
</style>

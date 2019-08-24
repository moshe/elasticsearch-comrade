<template>
  <v-combobox
    :items="endpoints"
    clearable
    label="URL"
    item-text="path"
    ref="filter"
    autofocus
    v-model="select"
    id="endpoint-selector"
  >
    <template v-slot:item="{ index, item }">
      <v-list-item-content>
        <div>{{ item.method }} {{ item.path }}</div>
      </v-list-item-content>
      <v-list-item-action>
        <v-chip label small color="success">{{ item.name }}</v-chip>
      </v-list-item-action>
    </template>
  </v-combobox>
</template>

<script>
import { mapState } from "vuex";
import endpoints from "../../assets/elasticsearch_endpoints.json";

export default {
  props: {
    method: {
      type: String,
      required: true
    },
    path: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      select: this.path
    };
  },
  computed: {
    ...mapState(["indices"]),
    endpoints() {
      return endpoints
        .flatMap(this.expandIndices)
        .filter(x => x.method === this.method);
    }
  },
  watch: {
    select(selected) {
      if (typeof selected === "string") {
        this.$emit("change", { path: selected });
      } else {
        this.$emit("change", selected);
      }
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
    }
  }
};
</script>

<style scoped></style>

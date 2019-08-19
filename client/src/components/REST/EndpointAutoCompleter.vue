<template>
  <v-combobox
    :items="endpoints"
    :value="path"
    clearable
    label="URL"
    item-text="path"
    ref="filter"
    @update:search-input="onChange"
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
  computed: {
    ...mapState(["indices"]),
    endpoints() {
      return endpoints
        .flatMap(this.expandIndices)
        .filter(x => x.method === this.method);
    }
  },
  methods: {
    onChange(selected) {
      if (typeof selected === "string") {
        this.$emit("change", { path: selected });
      } else {
        this.$emit("change", selected);
      }
    },
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

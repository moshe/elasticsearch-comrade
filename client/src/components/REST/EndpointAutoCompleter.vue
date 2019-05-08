<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-combobox
    :items="endpoints"
    clearable
    autofocus
    label="URL"
    item-text="path"
    @change="onChange"
  >
    <template v-slot:item="{ index, item }">
      <v-list-tile-content>
        <v-chip dark label small> {{ item.method }} {{ item.path }} </v-chip>
      </v-list-tile-content>
      <v-list-tile-action>
        <v-chip dark label small>{{ item.name }}</v-chip>
      </v-list-tile-action>
    </template>
  </v-combobox>
</template>

<script>
import { mapState } from "vuex";
import endpoints from "../../assets/elasticsearch_endpoints.json";

export default {
  name: "EndpointAutoCompleter",
  props: {
    method: {
      type: String
    },
    url: {
      type: String
    }
  },
  computed: {
    ...mapState(["indices"]),
    endpoints() {
      return endpoints.flatMap(this.expandIndices);
    }
  },
  methods: {
    onChange(selected) {
      if (typeof selected === "string") {
        this.$emit("change", {
          path: selected,
          method: this.method
        });
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

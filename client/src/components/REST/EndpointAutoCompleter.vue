<template>
  <v-combobox
    :items="endpoints"
    :value="path"
    clearable
    label="URL"
    item-text="path"
    ref="filter"
    @change="onChange"
  >
    <template v-slot:item="{ index, item }">
      <v-list-tile-content>
        <v-chip dark label small> {{ item.method }} {{ item.path }} </v-chip>
      </v-list-tile-content>
      <v-list-tile-action>
        <v-chip dark label small color="success">{{ item.name }}</v-chip>
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
        this.$emit("change", {
          path: selected
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

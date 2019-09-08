<template>
  <v-data-table
    :headers="headers"
    :items="items"
    class="elevation-1 small-table"
    :footer-props="{ 'items-per-page-options': [30, 100, 200] }"
    sort-by="date"
    :sort-desc="true"
  >
    <template v-slot:item.date="{ item }">
      {{ fromNow(item.date) }}
    </template>
    <template v-slot:item.query="props">
      {{ truncate(JSON.stringify(props.item.query), 50) }}
    </template>
    <template v-slot:item.actions="props">
      <v-icon x-small @click="removeQuery(props.item)">clear</v-icon>
      <v-icon x-small class="ml-1" @click="setQuery(props.item)">edit</v-icon>
      <v-icon
        x-small
        color="yellow"
        class="ml-1"
        @click="$emit('star', props.item)"
        v-if="storeName !== 'starred'"
      >
        {{ icon(props.item) }}
      </v-icon>
    </template>
  </v-data-table>
</template>

<script>
const MAX_SIZE = 1000;
import formatDistance from "date-fns/formatDistanceToNow";

export default {
  props: {
    storeName: {
      type: String,
      required: true
    }
  },
  mounted() {
    if (localStorage[this.storeName]) {
      this.items = JSON.parse(localStorage[this.storeName]);
    }
  },
  data() {
    return {
      headers: [
        { text: "Method", value: "method" },
        { text: "Path", value: "path" },
        { text: "Date", value: "date" },
        { text: "Query", value: "query" },
        { text: "Actions", value: "actions", sortable: false }
      ],
      items: []
    };
  },
  methods: {
    setQuery(item) {
      this.$emit("query", item);
    },
    truncate(input, size) {
      return input.length > size
        ? `${input.substring(0, size - 4)} ...`
        : input;
    },
    fromNow(t) {
      return formatDistance(t, { addSuffix: true });
    },
    addEntry({ method, path, query, date }) {
      this.items.push({ method, query, path, date });
      if (this.items.length > MAX_SIZE) {
        this.items.splice(-(this.items.length - MAX_SIZE));
      }
      localStorage[this.storeName] = JSON.stringify(this.items);
    },
    removeQuery(item) {
      this.items = this.items.filter(
        x =>
          !(
            item.method === x.method &&
            item.path === x.path &&
            JSON.stringify(item.query) === JSON.stringify(x.query) &&
            item.date === x.date
          )
      );
      localStorage[this.storeName] = JSON.stringify(this.items);
    },
    icon(item) {
      const matches = JSON.parse(localStorage["starred"] || "[]").filter(
        x =>
          item.method === x.method &&
          item.path === x.path &&
          JSON.stringify(item.query) === JSON.stringify(x.query) &&
          item.date === x.date
      );
      return matches.length === 0 ? "star_border" : "start";
    }
  }
};
</script>

<style></style>

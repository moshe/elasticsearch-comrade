<template>
  <v-data-table
    :headers="headers"
    :items="items"
    class="elevation-1 mt-3 query-history"
    :rows-per-page-items="[30, 100, 200]"
    :pagination.sync="pagination"
  >
    <template v-slot:items="props">
      <td>{{ props.item.method }}</td>
      <td>{{ props.item.path }}</td>
      <td>{{ fromNow(props.item.date) }}</td>
      <td>{{ props.item.query }}</td>
      <td>
        <v-icon small @click="removeQuery(props.item)">
          clear
        </v-icon>
        <v-icon small class="ml-2" @click="setQuery(props.item)">edit</v-icon>
        <v-icon
          small
          color="yellow"
          class="ml-2"
          @click="$emit('star', props.item)"
          v-if="storeName !== 'starred'"
        >
          {{ icon(props.item) }}
        </v-icon>
      </td>
    </template>
  </v-data-table>
</template>

<script>
const MAX_SIZE = 1000;
import formatDistance from "date-fns/distance_in_words_to_now";

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
      pagination: { descending: true, sortBy: "date" },
      headers: [
        { text: "Method", value: "method" },
        { text: "Path", value: "path" },
        { text: "Date", value: "date" },
        { text: "Query", value: "query" },
        { text: "Actions", value: "path" }
      ],
      items: []
    };
  },
  methods: {
    setQuery(item) {
      this.$emit("query", item);
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

<style>
.query-history table.v-table tbody td {
  padding: 0 !important;
  padding-left: 5px !important;
}
.query-history table.v-table thead th {
  padding: 0 !important;
  padding-left: 5px !important;
}
.query-history table.v-table tbody td {
  height: 24px;
  line-height: 24px;
  text-align: left;
}

.query-history table.v-table thead th {
  height: 50px;
  line-height: 50px;
  font-size: 14px;
  text-align: center;
}
</style>

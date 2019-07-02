<template>
  <v-data-table
    :headers="headers"
    :items="history"
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
        <v-icon small class="mr-2" @click="removeQuery(props.item)">
          clear
        </v-icon>
        <v-icon small @click="setQuery(props.item)">edit</v-icon>
      </td>
    </template>
  </v-data-table>
</template>

<script>
const HISTORY_MAX_SIZE = 1000;
import formatDistance from "date-fns/distance_in_words_to_now";

export default {
  mounted() {
    if (localStorage.queryHistory) {
      this.history = JSON.parse(localStorage.queryHistory);
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
      history: []
    };
  },
  methods: {
    setQuery(item) {
      this.$emit("query", item);
    },
    fromNow(t) {
      return formatDistance(t, { addSuffix: true });
    },
    addEntry(method, path, query) {
      const date = Date.now();
      this.history.push({ method, query, path, date });
      if (this.history.length > HISTORY_MAX_SIZE) {
        this.history.splice(-(this.history.length - HISTORY_MAX_SIZE));
      }
      localStorage.queryHistory = JSON.stringify(this.history);
    },
    removeQuery(item) {
      this.history = this.history.filter(
        x =>
          !(
            item.method === x.method &&
            item.path === x.path &&
            item.query === x.query &&
            item.date === x.date
          )
      );
      localStorage.queryHistory = JSON.stringify(this.history);
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

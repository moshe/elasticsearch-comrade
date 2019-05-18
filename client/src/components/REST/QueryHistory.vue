<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="history"
      class="elevation-1 mt-3"
      :rows-per-page-items="[30, 100, 200]"
    >
      <template v-slot:items="props">
        <td>
          <v-icon small class="mr-2" @click="removeQuery(props.item)">
            clear
          </v-icon>
          <v-icon small @click="setQuery(props.item)">
            edit
          </v-icon>
        </td>
        <td>{{ props.item.method }}</td>
        <td>{{ props.item.path }}</td>
        <td>{{ props.item.date }}</td>
        <td>{{ props.item.query }}</td>
      </template>
    </v-data-table>
  </div>
</template>

<script>
const HISTORY_MAX_SIZE = 1000;
export default {
  mounted() {
    if (localStorage.queryHistory) {
      this.history = JSON.parse(localStorage.queryHistory);
    }
  },
  data() {
    return {
      headers: [
        { text: "Actions", value: "path" },
        { text: "Method", value: "method" },
        { text: "Path", value: "path" },
        { text: "Date", value: "date" },
        { text: "Query", value: "query" }
      ],
      history: []
    };
  },
  methods: {
    setQuery(item) {
      this.$emit("query", item);
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

<style scoped>
table.v-table tbody td {
  height: unset;
  line-height: 36px;
}
</style>

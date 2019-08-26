<template>
  <div>
    <v-header sub>Index Graveyard</v-header>
    <v-data-table
      :headers="headers"
      :items-per-page="100"
      :items="yard"
      class="elevation-1 small-table"
      :footer-props="{ 'items-per-page-options': [30, 100, 200] }"
      sort-by="delete_date_in_millis"
      :sort-desc="true"
    >
      <template v-slot:item.delete_date_in_millis="{ item }">
        {{ fromNow(item.delete_date_in_millis) }}
      </template>
    </v-data-table>
  </div>
</template>

<script>
import indexApis from "../mixins/indexApis";
import formatDistance from "date-fns/formatDistanceToNow";
import VHeader from "../components/Base/Header.vue";
export default {
  mixins: [indexApis],
  components: { VHeader },
  async created() {
    this.$store.commit("startLoading");
    this.yard = await this.getGraveyard();
    this.$store.commit("stopLoading");
  },
  data() {
    return {
      headers: [
        { text: "Index Name", value: "index.index_name" },
        { text: "Index UUID", value: "index.index_uuid" },
        { text: "Time", value: "delete_date_in_millis" }
      ],
      yard: []
    };
  },
  methods: {
    fromNow(t) {
      return formatDistance(t, { addSuffix: true });
    }
  }
};
</script>

<style lang="scss" scoped></style>

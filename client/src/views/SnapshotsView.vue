<template>
  <v-layout>
    <v-flex xs7 class="pr-4">
      <v-header sub>Snapshots</v-header>
      <snapshot-list-table :repos="repos" />
    </v-flex>
    <v-flex xs5 class="pl-4">
      <v-header sub>Create a snapshot</v-header>
      <create-snapshot :repos="repos" />
    </v-flex>
  </v-layout>
</template>

<script>
import snapshotApis from "../mixins/snapshotApis";
import SnapshotListTable from "../components/Snapshots/SnapshotListTable.vue";
import CreateSnapshot from "../components/Snapshots/CreateSnapshot.vue";
import VHeader from "../components/Base/Header.vue";

export default {
  mixins: [snapshotApis],
  components: { SnapshotListTable, CreateSnapshot, VHeader },
  async created() {
    this.repos = await this.listRepos();
  },
  data() {
    return { repos: [] };
  }
};
</script>

<style></style>

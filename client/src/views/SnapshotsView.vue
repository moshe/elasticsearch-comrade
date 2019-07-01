<template>
  <v-layout>
    <v-flex xs8 class="pr-3">
      <div style="font-size: 25px" class="mb-2">Snapshots</div>
      <snapshot-list-table :repos="repos" />
    </v-flex>
    <v-flex xs5 class="pl-3">
      <div style="font-size: 25px" class="mb-2">Create a snapshot</div>
      <create-snapshot :repos="repos" />
    </v-flex>
  </v-layout>
</template>

<script>
import snapshotApis from "../mixins/snapshotApis";
import SnapshotListTable from "../components/Snapshots/SnapshotListTable.vue";
import CreateSnapshot from "../components/Snapshots/CreateSnapshot.vue";

export default {
  mixins: [snapshotApis],
  components: { SnapshotListTable, CreateSnapshot },
  async created() {
    this.repos = await this.listRepos();
  },
  data() {
    return { repos: [] };
  }
};
</script>

<style></style>

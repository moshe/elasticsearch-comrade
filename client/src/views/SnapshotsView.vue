<template>
  <v-layout>
    <v-flex xs6 class="pr-3">
      <div style="font-size: 25px" class="mb-2">Snapshots</div>
      <v-combobox
        :items="repos"
        label="Select repository"
        item-text="id"
        @change="repo => loadRepo(repo.id)"
        class="mb-2"
      >
        <template v-slot:item="{ index, item }">
          <v-list-tile-content>
            <v-chip dark label small>{{ item.id }} {{ item.location }} </v-chip>
          </v-list-tile-content>
          <v-list-tile-action>
            <v-chip dark label small>{{ item.type }}</v-chip>
          </v-list-tile-action>
        </template>
      </v-combobox>
      <snapshot-list-table :snapshots="snapshots" :repo="selectedRepo" />
    </v-flex>
    <v-flex xs6 class="pl-3">
      <div style="font-size: 25px" class="mb-2">Restore</div>
    </v-flex>
  </v-layout>
</template>

<script>
import snapshotApis from "../mixins/snapshotApis";
import SnapshotListTable from "../components/Snapshots/SnapshotListTable.vue";
export default {
  mixins: [snapshotApis],
  components: { SnapshotListTable },
  async created() {
    this.repos = await this.listRepos();
  },
  methods: {
    async loadRepo(repo) {
      this.snapshots = await this.listSnapshots(repo);
      this.selectedRepo = repo;
    }
  },
  data() {
    return {
      repos: [],
      snapshots: [],
      selectedRepo: ""
    };
  }
};
</script>

<style>
.checkbox-text {
  cursor: help;
}
</style>

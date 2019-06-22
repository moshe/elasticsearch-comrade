<template>
  <v-layout id="snapshots-view">
    <v-flex xs6 class="pr-3">
      <div style="font-size: 25px" class="mb-2">Snapshots</div>
      <v-combobox
        :items="repos"
        clearable
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
      <snapshot-list-table :snapshots="snapshots" @restore="selectSnapshot" />
    </v-flex>
    <v-flex xs6 class="pl-3">
      <div style="font-size: 25px" class="mb-2">Restore</div>
      <restore-form :snapshot="selectedSnapshot" />
    </v-flex>
  </v-layout>
</template>

<script>
import snapshotApis from "../mixins/snapshotApis";
import RestoreForm from "../components/Snapshots/RestoreForm.vue";
import SnapshotListTable from "../components/Snapshots/SnapshotListTable.vue";
export default {
  mixins: [snapshotApis],
  components: { RestoreForm, SnapshotListTable },
  async created() {
    this.repos = await this.listRepos();
  },
  methods: {
    async loadRepo(repo) {
      this.snapshots = await this.listSnapshots(repo);
    },
    selectSnapshot(snapshot) {
      this.selectedSnapshot = snapshot;
    }
  },
  data() {
    return {
      repos: [],
      snapshots: [],
      selectedSnapshot: { indices: [] }
    };
  }
};
</script>

<style>
.checkbox-text {
  cursor: help;
}
#snapshots-view .v-btn--icon.v-btn--small {
  margin: 0;
}

#snapshots-view .v-input--selection-controls {
  margin-top: 0;
  padding-top: 0;
}

#snapshots-view
  .v-input--selection-controls:not(.v-input--hide-details)
  .v-input__slot {
  margin-bottom: 0;
}

#snapshots-view .v-messages {
  min-height: 0px;
}
</style>

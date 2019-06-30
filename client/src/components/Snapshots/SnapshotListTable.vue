<template>
  <div>
    <repo-selector :repos="repos" @select="loadRepo" />
    <v-dialog v-model="showDialog" width="60%">
      <restore-form :repo="repo" :snapshot="snapshot" />
    </v-dialog>
    <v-data-table
      :headers="headers"
      :items="snapshots"
      class="elevation-1 snapshots-list-table"
      item-key="id"
      :rows-per-page-items="[30, 100, 200]"
    >
      <template v-slot:items="props">
        <tr>
          <td>{{ props.item.snapshot }}</td>
          <td>{{ props.item.state }}</td>
          <td>{{ props.item.start_time.split(":")[0] }}</td>
          <td>{{ parseInt(props.item.duration_in_millis / 1000) }}</td>
          <td>
            <v-btn flat icon small @click="showRestoreDialog(props.item)">
              <v-icon small>settings_backup_restore</v-icon>
            </v-btn>
          </td>
        </tr>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import RestoreForm from "./RestoreForm.vue";
import RepoSelector from "./RepoSelector.vue";
import snapshotApis from "../../mixins/snapshotApis";

export default {
  props: {
    repos: {
      type: Array,
      required: true
    }
  },
  mixins: [snapshotApis],
  components: { RestoreForm, RepoSelector },
  methods: {
    showRestoreDialog(snapshot) {
      this.snapshot = snapshot;
      this.showDialog = true;
    },
    async loadRepo(repo) {
      if (!repo) {
        return;
      }
      this.snapshots = await this.listSnapshots(repo);
      this.repo = repo;
    }
  },
  data() {
    return {
      showDialog: false,
      snapshots: [],
      repo: "",
      snapshot: { indices: [] },
      headers: [
        { text: "Id", value: "snapshot" },
        { text: "State", value: "state" },
        { text: "Time", value: "start_time" },
        { text: "Took", value: "duration_in_millis" },
        { text: "Restore", value: "duration_in_millis", sortable: false }
      ]
    };
  }
};
</script>

<style>
.snapshots-list-table table.v-table tbody td {
  padding: 0 !important;
  padding-left: 5px !important;
}
.snapshots-list-table table.v-table thead th {
  padding: 0 !important;
  padding-left: 5px !important;
}
.snapshots-list-table table.v-table tbody td {
  height: 24px;
  line-height: 24px;
  text-align: left;
}

.snapshots-list-table table.v-table thead th {
  height: 50px;
  line-height: 50px;
  font-size: 14px;
  text-align: center;
}

.snapshots-list-table .v-btn--icon.v-btn--small {
  margin: 0;
}
</style>

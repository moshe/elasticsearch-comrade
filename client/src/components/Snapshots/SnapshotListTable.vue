<template>
  <div>
    <repo-selector :repos="repos" @select="loadRepo" />
    <v-dialog v-model="showDialog" width="60%">
      <restore-form :repo="repo" :snapshot="snapshot" />
    </v-dialog>
    <v-data-table
      :headers="headers"
      :items="snapshots"
      class="elevation-1 small-table"
      item-key="id"
      :footer-props="{ 'items-per-page-options': [30, 100, 200] }"
      sort-by="start_time"
      :sort-desc="true"
    >
      <template v-slot:items="props">
        <tr>
          <td>{{ props.item.snapshot }}</td>
          <td>{{ fromNow(props.item.start_time) }}</td>
          <td>{{ props.item.state }}</td>
          <td>{{ parseInt(props.item.duration_in_millis / 1000) }}s</td>
          <td>
            <v-btn text icon small @click="showRestoreDialog(props.item)">
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
import formatDistance from "date-fns/formatDistanceToNow";

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
    fromNow(t) {
      return formatDistance(t, { addSuffix: true });
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
        { text: "Time", value: "start_time" },
        { text: "State", value: "state" },
        { text: "Took", value: "duration_in_millis" },
        { text: "Restore", value: "duration_in_millis", sortable: false }
      ]
    };
  }
};
</script>

<style></style>

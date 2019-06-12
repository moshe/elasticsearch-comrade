<template>
  <v-layout>
    <v-flex xs6>
      <div style="font-size: 25px" class="mb-2">
        Snapshots
      </div>
      <v-combobox
        :items="repos"
        clearable
        label="Repository"
        item-text="id"
        @change="repo => loadRepo(repo.id)"
      >
        <template v-slot:item="{ index, item }">
          <v-list-tile-content>
            <v-chip dark label small>
              {{ item.id }} {{ item.location }}
            </v-chip>
          </v-list-tile-content>
          <v-list-tile-action>
            <v-chip dark label small>{{ item.type }}</v-chip>
          </v-list-tile-action>
        </template>
      </v-combobox>
      <v-data-table
        :headers="headers"
        :items="snapshots"
        class="elevation-1"
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
              <v-btn flat icon small>
                <v-icon small>restore</v-icon>
              </v-btn>
              <v-btn flat icon small>
                <v-icon small>clear</v-icon>
              </v-btn>
            </td>
          </tr>
        </template>
      </v-data-table>
    </v-flex>
    <v-flex style="margin-left: 10px">
      <div style="font-size: 25px" class="mb-2">
        Restore
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
import snapshotApis from "../mixins/snapshotApis";
import { mapState } from "vuex";
export default {
  mixins: [snapshotApis],
  computed: {
    ...mapState(["settingsRefreshEvery", "settingsRefreshEnabled"])
  },
  async created() {
    await this.updateData();
    setTimeout(this.updateData, this.settingsRefreshEvery);
  },
  methods: {
    async loadRepo(repo) {
      this.snapshots = await this.listSnapshots(repo);
    },
    async updateData() {
      if (this.settingsRefreshEnabled) {
        this.repos = await this.listRepos();
      }
      setTimeout(this.refreshTasks, this.settingsRefreshEvery);
    }
  },
  data() {
    return {
      headers: [
        { text: "Id", value: "snapshot" },
        { text: "State", value: "state" },
        { text: "Time", value: "start_time" },
        { text: "Took", value: "duration_in_millis" },
        { text: "Actions", value: "duration_in_millis" }
      ],
      repos: [],
      snapshots: []
    };
  }
};
</script>

<style>
table.v-table tbody td {
  padding: 0 !important;
  padding-left: 5px !important;
}
table.v-table thead th {
  padding: 0 !important;
  padding-left: 5px !important;
}
table.v-table tbody td {
  height: 24px;
  line-height: 24px;
  text-align: left;
}

table.v-table thead th {
  height: 50px;
  line-height: 50px;
  font-size: 14px;
  text-align: center;
}

.v-btn--icon.v-btn--small {
  margin: 0;
}
</style>

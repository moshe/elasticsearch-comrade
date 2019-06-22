<template>
  <v-layout id="snapshots-view">
    <v-flex xs6 class="pr-3">
      <div style="font-size: 25px" class="mb-2">
        Snapshots
      </div>
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
            <v-chip dark label small>
              {{ item.id }} {{ item.location }}
            </v-chip>
          </v-list-tile-content>
          <v-list-tile-action>
            <v-chip dark label small>{{ item.type }}</v-chip>
          </v-list-tile-action>
        </template>
      </v-combobox>
      <snapshot-list-table :snapshots="snapshots" @restore="selectSnapshot" />
    </v-flex>
    <v-flex xs6 class="pl-3">
      <div style="font-size: 25px" class="mb-2">
        Restore
      </div>
      <div style="font-size: 18px" class="mb-2">Restore Options</div>
      <v-layout>
        <v-flex class="pr-3" style="flex:1">
          <v-text-field solo label="Rename Pattern" />
        </v-flex>
        <v-flex class="pr-3" style="flex:1">
          <v-text-field solo label="Rename Replacement" />
        </v-flex>
      </v-layout>

      <v-checkbox>
        <template v-slot:label>
          <v-tooltip bottom max-width="400px">
            <template v-slot:activator="{ on }">
              <div v-on="on">Ignore unavailable indices</div>
            </template>
            <span>{{ docs.ignoreUnavailable }} </span>
          </v-tooltip>
        </template>
      </v-checkbox>

      <v-checkbox>
        <template v-slot:label>
          <v-tooltip bottom max-width="400px">
            <template v-slot:activator="{ on }">
              <div v-on="on">Include global state</div>
            </template>
            <span>{{ docs.includeGlobalState }} </span>
          </v-tooltip>
        </template>
      </v-checkbox>

      <v-checkbox>
        <template v-slot:label>
          <v-tooltip bottom max-width="400px">
            <template v-slot:activator="{ on }">
              <div v-on="on">Include aliases</div>
            </template>
            <span>{{ docs.includeAliases }} </span>
          </v-tooltip>
        </template>
      </v-checkbox>

      <v-checkbox>
        <template v-slot:label>
          <v-tooltip bottom max-width="400px">
            <template v-slot:activator="{ on }">
              <div v-on="on">Partial</div>
            </template>
            <span>{{ docs.partial }} </span>
          </v-tooltip>
        </template>
      </v-checkbox>
      <div style="font-size: 18px" class="mt-3">Choose indices</div>
      <index-selector
        :indices="selectedSnapshot.indices"
        @select="selectIndices"
      />

      <v-btn color="success">Restore</v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
import snapshotApis from "../mixins/snapshotApis";
import IndexSelector from "../components/Snapshots/IndexSelector.vue";
import SnapshotListTable from "../components/Snapshots/SnapshotListTable.vue";
export default {
  mixins: [snapshotApis],
  components: { IndexSelector, SnapshotListTable },
  async created() {
    this.repos = await this.listRepos();
  },
  methods: {
    async loadRepo(repo) {
      this.snapshots = await this.listSnapshots(repo);
    },
    selectSnapshot(snapshot) {
      this.selectedSnapshot = snapshot;
    },
    selectIndices(indices) {
      this.selectedIndices = indices;
    }
  },
  data() {
    return {
      docs: {
        // https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-snapshots.html#_partial_restore
        partial:
          "By default, the entire restore operation will fail if one or more indices participating in the operation don’t have snapshots of all shards available. It can occur if some shards failed to snapshot for example. It is still possible to restore such indices by setting partial to true. Please note, that only successfully snapshotted shards will be restored in this case and all missing shards will be recreated empty.",
        // https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-snapshots.html#_restore
        includeAliases:
          "Set include_aliases to false to prevent aliases from being restored together with associated indices",
        ignoreUnavailable:
          "The snapshot request also supports the ignore_unavailable option. Setting it to true will cause indices that do not exist to be ignored during snapshot creation. By default, when ignore_unavailable option is not set and an index is missing the snapshot request will fail. By setting include_global_state to false it’s possible to prevent the cluster global state to be stored as part of the snapshot. By default, the entire snapshot will fail if one or more indices participating in the snapshot don’t have all primary shards available. This behaviour can be changed by setting partial to true.",
        includeGlobalState:
          "By setting include_global_state to false it’s possible to prevent the cluster global state to be stored as part of the snapshot. By default, the entire snapshot will fail if one or more indices participating in the snapshot don’t have all primary shards available. This behaviour can be changed by setting partial to true."
      },
      repos: [],
      snapshots: [],
      selectedIndices: [],
      selectedSnapshot: { indices: [] }
    };
  }
};
</script>

<style>
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

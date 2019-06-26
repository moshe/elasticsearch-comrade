<template>
  <div class="restore-form">
    <v-layout>
      <v-flex class="pr-3" style="flex:1">
        <v-text-field
          :disabled="!snapshot.snapshot"
          v-model="renamePattern"
          label="Rename Pattern"
          placeholder="index_(.+)"
        />
      </v-flex>
      <v-flex class="pr-3" style="flex:1">
        <v-text-field
          :disabled="!snapshot.snapshot"
          v-model="renameReplacement"
          label="Rename Replacement"
          placeholder="restored_index_$1"
        />
      </v-flex>
    </v-layout>
    <div style="font-size: 18px" class="mb-2 mt-3">Restore Options</div>
    <v-checkbox
      v-for="option in booleanOptions"
      :key="option.title"
      v-model="option.value"
      :disabled="!snapshot.snapshot"
    >
      <template v-slot:label>
        <v-tooltip bottom max-width="400px">
          <template v-slot:activator="{ on }">
            <div v-on="on" class="checkbox-text">{{ option.title }}</div>
          </template>
          <span>{{ option.docs }} </span>
        </v-tooltip>
      </template>
    </v-checkbox>
    <div style="font-size: 18px" class="mt-3">Choose indices</div>
    <index-selector
      :indices="snapshot.indices"
      :selected.sync="selectedIndices"
    />
    <div style="font-size: 18px" class="mt-3">Override index Settings</div>
    <query-editor ref="editor" :init="{ 'index.number_of_replicas': 0 }" />
    <v-btn
      color="success"
      @click="onRestore"
      :disabled="!snapshot.snapshot || selectedIndices.length === 0"
    >
      Restore
    </v-btn>
  </div>
</template>

<script>
import IndexSelector from "./IndexSelector.vue";
import snapshotApis from "../../mixins/snapshotApis";
import QueryEditor from "../Base/QueryEditor.vue";
export default {
  props: ["snapshot", "repo"],
  components: { IndexSelector, QueryEditor },
  mixins: [snapshotApis],
  data() {
    return {
      // https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-snapshots.html
      renamePattern: undefined,
      renameReplacement: undefined,
      booleanOptions: {
        partial: {
          title: "Partial",
          value: false,
          docs:
            "By default, the entire restore operation will fail if one or more indices participating in the operation don’t have snapshots of all shards available. It can occur if some shards failed to snapshot for example. It is still possible to restore such indices by setting partial to true. Please note, that only successfully snapshotted shards will be restored in this case and all missing shards will be recreated empty."
        },
        include_global_state: {
          title: "Include global state",
          value: true,
          docs:
            "By setting include_global_state to false it’s possible to prevent the cluster global state to be stored as part of the snapshot. By default, the entire snapshot will fail if one or more indices participating in the snapshot don’t have all primary shards available. This behaviour can be changed by setting partial to true."
        },
        include_aliases: {
          title: "Include aliases",
          value: true,
          docs:
            "Set include_aliases to false to prevent aliases from being restored together with associated indices"
        },
        ignore_unavailable: {
          title: "Ignore unavailable",
          value: false,
          docs:
            "The snapshot request also supports the ignore_unavailable option. Setting it to true will cause indices that do not exist to be ignored during snapshot creation. By default, when ignore_unavailable option is not set and an index is missing the snapshot request will fail. By setting include_global_state to false it’s possible to prevent the cluster global state to be stored as part of the snapshot. By default, the entire snapshot will fail if one or more indices participating in the snapshot don’t have all primary shards available. This behaviour can be changed by setting partial to true."
        }
      },
      selectedIndices: []
    };
  },
  methods: {
    makeBody() {
      const { parse, stringify } = JSON;
      return parse(
        stringify({
          indices: this.selectedIndices,
          partial: this.booleanOptions.partial.value,
          include_global_state: this.booleanOptions.include_global_state.value,
          include_aliases: this.booleanOptions.include_aliases.value,
          ignore_unavailable: this.booleanOptions.ignore_unavailable.value,
          rename_pattern: this.renamePattern,
          rename_replacement: this.rename_replacement,
          index_settings: this.$refs.editor.getQuery()
        })
      );
    },
    async onRestore() {
      await this.restore(this.repo, this.snapshot.snapshot, this.makeBody());
    }
  }
};
</script>

<style>
.restore-form .v-input--selection-controls {
  margin-top: 0;
  padding-top: 0;
}

.restore-form
  .v-input--selection-controls:not(.v-input--hide-details)
  .v-input__slot {
  margin-bottom: 0;
}

.restore-form .v-messages {
  min-height: 0px;
}
</style>

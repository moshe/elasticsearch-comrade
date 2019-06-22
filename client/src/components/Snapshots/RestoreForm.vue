<template>
  <div>
    <v-layout>
      <v-flex class="pr-3" style="flex:1"
        ><v-text-field solo label="Rename Pattern" />
      </v-flex>
      <v-flex class="pr-3" style="flex:1">
        <v-text-field solo label="Rename Replacement" />
      </v-flex>
    </v-layout>
    <div style="font-size: 18px" class="mb-2">Restore Options</div>
    <v-checkbox v-for="option in booleanOptions" :key="option.title">
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
    <v-btn color="success">Restore</v-btn>
  </div>
</template>

<script>
import IndexSelector from "./IndexSelector.vue";

export default {
  props: ["snapshot"],
  components: { IndexSelector },
  data() {
    return {
      // https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-snapshots.html
      booleanOptions: {
        partial: {
          title: "Partial",
          value: null,
          docs:
            "By default, the entire restore operation will fail if one or more indices participating in the operation don’t have snapshots of all shards available. It can occur if some shards failed to snapshot for example. It is still possible to restore such indices by setting partial to true. Please note, that only successfully snapshotted shards will be restored in this case and all missing shards will be recreated empty."
        },
        include_global_state: {
          title: "Include global state",
          value: null,
          docs:
            "By setting include_global_state to false it’s possible to prevent the cluster global state to be stored as part of the snapshot. By default, the entire snapshot will fail if one or more indices participating in the snapshot don’t have all primary shards available. This behaviour can be changed by setting partial to true."
        },
        include_aliases: {
          title: "Include aliases",
          value: null,
          docs:
            "Set include_aliases to false to prevent aliases from being restored together with associated indices"
        },
        ignore_unavailable: {
          title: "Ignore unavailable",
          value: null,
          docs:
            "The snapshot request also supports the ignore_unavailable option. Setting it to true will cause indices that do not exist to be ignored during snapshot creation. By default, when ignore_unavailable option is not set and an index is missing the snapshot request will fail. By setting include_global_state to false it’s possible to prevent the cluster global state to be stored as part of the snapshot. By default, the entire snapshot will fail if one or more indices participating in the snapshot don’t have all primary shards available. This behaviour can be changed by setting partial to true."
        }
      },
      selectedIndices: []
    };
  }
};
</script>

<style lang="scss" scoped></style>

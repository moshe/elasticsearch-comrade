<template>
  <div>
    <repo-selector :repos="repos" @select="x => (repo = x)" />
    <v-text-field label="Snapshot name" />
    <index-selector :indices="Object.keys(indices)" v-model="selectedIndices" />
    <doc-checkbox
      v-for="option in booleanOptions"
      :key="option.title"
      v-model="option.value"
      :doc="option.doc"
      :label="option.title"
    />
    <v-btn
      block
      class="mt-4"
      color="success"
      :disabled="selectedIndices.length === 0"
    >
      Create Snapshot
    </v-btn>
  </div>
</template>

<script>
import IndexSelector from "./IndexSelector.vue";
import { mapState } from "vuex";
import DocCheckbox from "./DocCheckbox.vue";
import RepoSelector from "./RepoSelector.vue";

export default {
  components: { IndexSelector, DocCheckbox, RepoSelector },
  props: {
    repos: {
      type: Array,
      required: true
    }
  },
  computed: {
    ...mapState(["indices"])
  },
  data() {
    return {
      selectedIndices: [],
      repo: null,
      booleanOptions: {
        partial: {
          title: "Partial",
          value: false,
          doc:
            "By default, the entire snapshot will fail if one or more indices participating in the snapshot don’t have all primary shards available. This behaviour can be changed by setting partial to true."
        },
        include_global_state: {
          title: "Include global state",
          value: true,
          doc:
            "By setting include_global_state to false it’s possible to prevent the cluster global state to be stored as part of the snapshot."
        },
        ignore_unavailable: {
          title: "Ignore unavailable",
          value: false,
          doc:
            "By default, when ignore_unavailable option is not set and an index is missing the snapshot request will fail."
        }
      }
    };
  }
};
</script>

<style scoped></style>

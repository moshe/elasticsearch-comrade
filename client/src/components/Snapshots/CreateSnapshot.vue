<template>
  <div>
    <repo-selector :repos="repos" @select="x => (repo = x)" />
    <v-text-field label="Snapshot name" />
    <index-selector
      :indices="Object.keys(indices)"
      :selected.sync="selectedIndices"
    />
    <!-- TODO: Add docs -->
    <doc-checkbox doc="docs!" label="Ignore unavailable indices" />
    <doc-checkbox doc="docs!" label="Include global state" />
    <doc-checkbox doc="docs!" label="Partial" />
    <v-btn block class="mt-4" color="success">Create Snapshot</v-btn>
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
      repo: null
    };
  }
};
</script>

<style scoped></style>

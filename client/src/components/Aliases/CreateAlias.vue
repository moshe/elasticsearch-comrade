<template>
  <div>
    <v-layout column>
      <v-flex>
        <div style="font-size: 25px" class="mb-2">
          Create New Alias
        </div>
      </v-flex>
      <v-layout>
        <v-flex class="pr-3" style="flex:1">
          <v-text-field solo label="Alias Name *" v-model="aliasName" />
        </v-flex>
        <v-flex style="flex:1">
          <v-autocomplete
            multiple
            solo
            v-model="selectedIndices"
            :items="Object.keys(indices)"
            label="Select Indices *"
          />
        </v-flex>
      </v-layout>
    </v-layout>

    <v-layout column>
      <v-flex>
        <div style="font-size: 18px" class="mb-2">
          Routing options
        </div>
      </v-flex>
      <v-layout>
        <v-flex class="pr-3" style="flex:1">
          <v-text-field solo label="Index Routing" v-model="indexRouting" />
        </v-flex>
        <v-flex style="flex:1">
          <v-text-field solo label="Search Routing" v-model="searchRouting" />
        </v-flex>
      </v-layout>
    </v-layout>
    <v-layout column>
      <v-flex>
        <div style="font-size: 18px">
          Filter
        </div>
      </v-flex>
      <v-layout>
        <v-flex class="pr-3" style="flex:1">
          <query-editor ref="editor" style="height: 400px;" />
        </v-flex>
      </v-layout>
    </v-layout>
    <v-btn
      color="primary"
      @click="submit"
      :disabled="!(selectedIndices.length && aliasName)"
      >Add</v-btn
    >
  </div>
</template>

<script>
import { mapState } from "vuex";
import aliasApis from "../../mixins/aliasApis";
import QueryEditor from "../REST/QueryEditor.vue";
export default {
  components: { QueryEditor },
  computed: {
    ...mapState(["indices"])
  },
  mixins: [aliasApis],
  methods: {
    async submit() {
      this.filter = this.$refs.editor.getQuery();
      for (const index of this.selectedIndices) {
        this.$emit("action", {
          index,
          action: "add",
          alias: this.aliasName,
          indexRouting: this.indexRouting,
          searchRouting: this.searchRouting
        });
      }
    }
  },
  data() {
    return {
      aliasName: "",
      selectedIndices: [],
      indexRouting: "",
      searchRouting: "",
      filter: {}
    };
  }
};
</script>

<style scoped></style>

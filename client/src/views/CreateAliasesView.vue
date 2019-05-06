<template>
  <v-form>
    <v-layout
      column
      style="background-color: #202020; padding: 20px; border-radius: 3px; margin-bottom:10px"
    >
      <v-flex>
        <div style="font-size: 25px">
          Basic options
        </div>
      </v-flex>
      <v-layout>
        <v-flex class="pr-3" style="flex:1">
          <v-text-field
            :error="!aliasName"
            label="Alias Name"
            v-model="aliasName"
          />
        </v-flex>
        <v-flex style="flex:1">
          <v-autocomplete
            :error="!selectedIndices.length"
            multiple
            v-model="selectedIndices"
            :items="Object.keys(indices)"
            label="Select Indices"
          />
        </v-flex>
      </v-layout>
    </v-layout>

    <v-layout
      style="background-color: #202020; padding: 20px; border-radius: 3px;margin-bottom:10px"
      column
    >
      <v-flex>
        <div style="font-size: 25px">
          Routing options
        </div>
      </v-flex>
      <v-layout>
        <v-flex class="pr-3" style="flex:1">
          <v-text-field label="Index Routing" v-model="indexRouting" />
        </v-flex>
        <v-flex style="flex:1">
          <v-text-field label="Search Routing" v-model="searchRouting" />
        </v-flex>
      </v-layout>
    </v-layout>
    <v-layout column>
      <v-flex>
        <div style="font-size: 25px">
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
      >Create</v-btn
    >
  </v-form>
</template>

<script>
import { mapState } from "vuex";
import aliasApis from "../mixins/aliasApis";

import QueryEditor from "../components/Terminal/QueryEditor.vue";
export default {
  mixins: [aliasApis],
  methods: {
    async submit() {
      if (!this.aliasName || this.selectedIndices.length === 0) {
        return;
      }
      this.filter = this.$refs.editor.getQuery();
      await this.createAlias(this);
    }
  },
  data() {
    return {
      aliasName: "",
      selectedIndices: [],
      indexRouting: "",
      searchRouting: "",
      filter: {},
      rules: {
        required: value => !!value || "Required."
      }
    };
  },
  components: { QueryEditor },
  computed: {
    ...mapState(["indices"])
  }
};
</script>

<style scoped></style>

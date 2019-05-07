<template>
  <v-layout row wrap>
    <v-flex style="margin-right: 20px" xs8>
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
        >Create</v-btn
      >
    </v-flex>
    <v-flex>
      <v-flex>
        <div style="font-size: 25px" class="mb-2">
          Manage Aliases
        </div>
      </v-flex>
      <div>
        <v-text-field
          solo
          label="Filter Aliases / Indices"
          v-model="value"
        ></v-text-field>
        <div v-for="index in Object.keys(indices)" :key="index">
          <div v-if="indices[index].aliases">
            <div style="font-size:15px">
              {{ index }}
            </div>
            <v-chip
              v-for="alias in indices[index].aliases"
              :key="alias"
              close
              color="orange"
              label
              outline
              small
            >
              {{ alias }}
            </v-chip>
            <v-btn flat icon color="orange">
              <v-icon>add</v-icon>
            </v-btn>
            <v-divider class="mb-2 mt-2"></v-divider>
          </div>
        </div>
        <v-btn color="success">Save</v-btn>
      </div>
    </v-flex>
  </v-layout>
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

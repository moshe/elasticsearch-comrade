<template>
  <div>
    <v-layout column>
      <v-flex><v-header sub>Create New Alias</v-header></v-flex>
      <v-layout>
        <v-flex class="pr-4" style="flex:1">
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
        <div style="font-size: 18px" class="mb-2">Routing options</div>
      </v-flex>
      <v-layout>
        <v-flex class="pr-4" style="flex:1">
          <v-text-field solo label="Index Routing" v-model="indexRouting" />
        </v-flex>
        <v-flex style="flex:1">
          <v-text-field solo label="Search Routing" v-model="searchRouting" />
        </v-flex>
      </v-layout>
    </v-layout>
    <v-layout column>
      <v-flex><div style="font-size: 18px">Filter</div></v-flex>
      <v-layout>
        <v-flex class="pr-4" style="flex:1">
          <query-editor ref="editor" style="height: 400px;" />
        </v-flex>
      </v-layout>
    </v-layout>
    <v-btn
      color="success"
      @click="submit"
      :disabled="!(selectedIndices.length && aliasName)"
    >
      Add
    </v-btn>
  </div>
</template>

<script>
import { mapState } from "vuex";
import QueryEditor from "../Base/QueryEditor.vue";
import VHeader from "../Base/Header.vue";

export default {
  components: { QueryEditor, VHeader },
  computed: { ...mapState(["indices"]) },
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

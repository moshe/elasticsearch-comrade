<template>
  <div>
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
          <v-text-field label="Alias Name"></v-text-field>
        </v-flex>
        <v-flex style="flex:1">
          <v-autocomplete
            multiple
            v-model="method"
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
          <v-text-field label="Index Routeing"></v-text-field>
        </v-flex>
        <v-flex style="flex:1">
          <v-text-field label="Search Routing"></v-text-field>
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
          <query-editor ref="editor" style="height: 400px;" />
        </v-flex>
      </v-layout>
    </v-layout>
    <v-btn color="primary">Save</v-btn>
  </div>
</template>

<script>
import { mapState } from "vuex";
import QueryEditor from "../components/Terminal/QueryEditor.vue";
export default {
  components: { QueryEditor },
  computed: {
    ...mapState(["indices"])
  }
};
</script>

<style scoped></style>

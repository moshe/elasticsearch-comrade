<template>
  <v-container>
    <v-layout>
      <v-flex style="flex: 2">
        <v-autocomplete
          v-model="method"
          :items="['GET', 'POST', 'DELETE']"
          label="Method"
          persistent-hint
        />
      </v-flex>
      <v-flex style="flex: 10" class="ml-3">
        <v-text-field clearable label="URL" v-model="url" />
      </v-flex>
      <v-flex style="flex: 1">
        <v-btn color="info" @click="sendQuery">Send</v-btn>
      </v-flex>
    </v-layout>
    <v-layout>
      <v-flex style="flex:1;" class="mr-3">
        <query-editor ref="editor" />
      </v-flex>
      <v-flex style="flex:1">
        <v-textarea
          name="input-7-1"
          color="#1e1e1e"
          rows="20"
          label="Response"
          readonly
          value="The Woodman set to work at once, and so sharp was his axe that the tree was soon chopped nearly through."
          hint="Hint text"
          outline
        ></v-textarea>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import QueryEditor from "../components/Terminal/QueryEditor";
export default {
  name: "QueryView",
  components: { QueryEditor },
  data() {
    return {
      method: "GET",
      url: "/"
    };
  },
  methods: {
    sendQuery() {
      console.log(this.$refs.editor.getQuery());
    }
  },
};
</script>

<style></style>

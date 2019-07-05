<template>
  <v-layout>
    <v-flex xs6>
      <v-header sub>lolcake</v-header>
      <v-data-table
        :headers="headers"
        :items="templates"
        class="elevation-1 small-table"
        item-key="id"
        :rows-per-page-items="[30, 100, 200]"
      >
        <template v-slot:items="props">
          <tr>
            <td>{{ props.item.name }}</td>
            <td>{{ props.item.index_patterns.join(",") }}</td>
            <td>
              <v-btn flat icon small>
                <v-icon small>edit</v-icon>
              </v-btn>
              <v-btn flat icon small>
                <v-icon small>delete_outline</v-icon>
              </v-btn>
            </td>
          </tr>
        </template>
      </v-data-table>
    </v-flex>
    <v-flex xs6>
      {{ templates }}
    </v-flex>
  </v-layout>
</template>

<script>
import templateApis from "../mixins/templateApis";
import VHeader from "../components/Base/Header.vue";

export default {
  mixins: [templateApis],
  components: { VHeader },
  async created() {
    this.templates = await this.listTemplates();
  },
  data() {
    return {
      templates: [],
      headers: [
        { text: "Name", value: "name" },
        { text: "Index Pattern", value: "index_patterns" },
        { text: "Actions", value: "index_patterns" }
      ]
    };
  }
};
</script>

<style lang="scss" scoped></style>

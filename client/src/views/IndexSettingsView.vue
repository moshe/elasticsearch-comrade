<template>
  <v-tabs color="#303030">
    <v-tab v-for="module in modules" :key="module.name">
      {{ module.name }}
    </v-tab>
    <v-tab-item v-for="module in modules" :key="module.name">
      <index-settings-form :module="module" />
    </v-tab-item>
  </v-tabs>
</template>

<script>
import indexApis from "../mixins/indexApis";
import IndexSettingsForm from "../components/IndexSettings/IndexSettingsForm.vue";

export default {
  mixins: [indexApis],
  components: { IndexSettingsForm },
  props: {
    indexName: {
      type: String,
      required: true
    }
  },
  async created() {
    this.modules = await this.getIndexDynamicModules(this.indexName);
  },
  data() {
    return { modules: [] };
  }
};
</script>

<style scoped></style>

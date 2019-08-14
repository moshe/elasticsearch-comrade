<template>
  <v-tabs color="#303030">
    <v-tab
      v-for="module in modules"
      :key="module.name"
      :data-tab="module.name.replace(' ', '-').toLowerCase()"
    >
      {{ module.name }}
    </v-tab>
    <v-tab-item v-for="module in modules" :key="module.name">
      <index-settings-form :module="module" @save="save" />
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
  },
  methods: {
    async save(settings) {
      await this.setIndexSettings(this.indexName, settings);
      this.modules = await this.getIndexDynamicModules(this.indexName);
    }
  }
};
</script>

<style scoped></style>

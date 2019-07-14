<template>
  <v-layout column>
    <v-flex v-for="module in modules" :key="module.name">
      <v-header sub>{{ module.name }}</v-header>
      <div>{{ module.description }}</div>
      <v-layout wrap>
        <v-flex
          xs6
          sm4
          md3
          v-for="setting in module.settings.filter(x => x.value !== undefined)"
          :key="setting.name"
          class="pa-2"
        >
          <v-text-field
            :label="setting.name"
            :value="setting.value"
            @change="v => handleChange(setting, v)"
          >
            <template v-slot:prepend-inner>
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-icon v-on="on" size="18">help_outline</v-icon>
                </template>
                <div
                  v-for="line in setting.description.split('\n')"
                  :key="line"
                >
                  {{ line }}
                </div>
              </v-tooltip>
            </template>
          </v-text-field>
        </v-flex>
      </v-layout>
      <div v-for="(value, key) in changes2" :key="key">
        {{ key }} changed from {{ value.from }} to {{ value.value }}
      </div>
      <v-btn color="success">Save</v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
import indexApis from "../mixins/indexApis";
import VHeader from "../components/Base/Header.vue";
import Vue from "vue";

export default {
  components: { VHeader },
  mixins: [indexApis],
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
    return {
      modules: [],
      changes2: {}
    };
  },
  methods: {
    handleChange(field, value) {
      if (value === field.value) {
        Vue.delete(this.changes2, field.name);
      } else {
        Vue.set(this.changes2, field.name, { value, from: field.value });
      }
    }
  }
};
</script>

<style lang="scss" scoped></style>

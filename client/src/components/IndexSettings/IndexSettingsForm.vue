<template>
  <div class="pa-4">
    <v-header sub>{{ module.name }}</v-header>
    <div style="line-height: 1; white-space: pre;">
      <span v-for="line in module.description.split('\n')" :key="line">
        {{ line }}
      </span>
    </div>
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
          :data-input="setting.name"
        >
          <template v-if="setting.description" v-slot:prepend-inner>
            <v-tooltip bottom>
              <template v-slot:activator="{ on }">
                <v-icon v-on="on" size="18">help_outline</v-icon>
              </template>
              <div v-for="line in setting.description.split('\n')" :key="line">
                {{ line }}
              </div>
            </v-tooltip>
          </template>
        </v-text-field>
      </v-flex>
    </v-layout>
    <div v-for="(value, key) in changes" :key="key">
      <v-btn text small color="white" @click="handleChange({ name: key })">
        <v-icon>clear</v-icon>
      </v-btn>
      {{ key }} changed from {{ value.from }} to {{ value.value }}
    </div>
    <v-btn
      class="mt-5"
      data-btn="save"
      color="success"
      :disabled="!pending"
      @click="save"
      v-text="'Save'"
    />
  </div>
</template>

<script>
import indexApis from "../../mixins/indexApis";
import VHeader from "../Base/Header.vue";
import Vue from "vue";

export default {
  components: { VHeader },
  mixins: [indexApis],
  props: {
    module: {
      type: Object
    }
  },
  data() {
    return { changes: {} };
  },
  computed: {
    pending() {
      return Object.keys(this.changes).length > 0;
    }
  },
  methods: {
    async save() {
      this.$emit(
        "save",
        Object.entries(this.changes).map(([k, v]) => [k, v.value])
      );
    },
    handleChange(field, value) {
      if (value === field.value || value === undefined) {
        Vue.delete(this.changes, field.name);
      } else {
        Vue.set(this.changes, field.name, { value, from: field.value });
      }
    }
  },
  watch: {
    module() {
      this.changes = {};
    }
  }
};
</script>

<style scoped></style>

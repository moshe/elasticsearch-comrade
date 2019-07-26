<template>
  <v-checkbox class="doc-checkbox" v-model="internalValue">
    <template v-slot:label>
      {{ label }}
      <v-tooltip bottom max-width="400px">
        <template v-slot:activator="{ on }">
          <v-icon size="14" class="ml-1" v-on="on" color="secondary lighten-2">
            help_outline
          </v-icon>
        </template>
        <span>{{ doc }}</span>
      </v-tooltip>
    </template>
  </v-checkbox>
</template>

<script>
export default {
  data() {
    return {
      internalValue: null
    };
  },
  created() {
    this.internalValue = this.value;
  },
  props: {
    doc: {
      type: String,
      required: true
    },
    label: {
      type: String,
      required: true
    },
    value: {
      type: Boolean
    }
  },
  watch: {
    internalValue(newValue) {
      this.$emit("input", newValue);
    }
  }
};
</script>

<style scoped></style>

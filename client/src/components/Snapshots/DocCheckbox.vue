<template>
  <v-checkbox class="doc-checkbox" v-model="internalValue">
    <template v-slot:label>
      <v-tooltip bottom max-width="400px">
        <template v-slot:activator="{ on }">
          <div v-on="on" class="checkbox-text">{{ label }}</div>
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

<style>
.doc-checkbox .checkbox-text {
  cursor: help;
}
.doc-checkbox .restore-form .v-input--selection-controls {
  margin-top: 0;
  padding-top: 0;
}

.doc-checkbox
  .restore-form
  .v-input--selection-controls:not(.v-input--hide-details)
  .v-input__slot {
  margin-bottom: 0;
}

.doc-checkbox .restore-form .v-messages {
  min-height: 0px;
}

.v-input--selection-controls {
  margin-top: 0;
  padding-top: 0;
}

.v-input--selection-controls:not(.v-input--hide-details) .v-input__slot {
  margin-bottom: 0;
}

.doc-checkbox .v-messages {
  min-height: 0px;
}
</style>

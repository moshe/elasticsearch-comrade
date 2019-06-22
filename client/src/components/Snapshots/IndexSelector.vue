<template>
  <v-select v-model="selected" :items="indices" label="Select indices" multiple>
    <template v-slot:prepend-item>
      <v-list-tile ripple @click="toggle">
        <v-list-tile-action>
          <v-icon>{{ icon }}</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
          <v-list-tile-title>Select All</v-list-tile-title>
        </v-list-tile-content>
      </v-list-tile>
    </template>
  </v-select>
</template>

<script>
export default {
  props: {
    indices: {
      type: Array,
      required: true
    }
  },
  computed: {
    allSelected() {
      return this.selected.length === this.indices.length;
    },
    likesSomeFruit() {
      return this.selected.length > 0 && !this.allSelected;
    },
    icon() {
      if (this.allSelected) return "check_box";
      if (this.likesSomeFruit) return "indeterminate_check_box";
      return "check_box_outline_blank";
    }
  },
  methods: {
    toggle() {
      this.$nextTick(() => {
        if (this.allSelected) {
          this.selected = [];
        } else {
          this.selected = this.indices.slice();
        }
      });
    }
  },
  data() {
    return {
      selected: []
    };
  },
  watch: {
    selected(selected) {
      this.$emit("select", selected);
    }
  }
};
</script>

<style scoped></style>

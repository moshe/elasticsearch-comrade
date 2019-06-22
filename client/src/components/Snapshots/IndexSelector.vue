<template>
  <div>
    <v-select v-model="inner" :items="indices" label="Select indices" multiple>
      <template v-slot:prepend-item>
        <v-list-tile ripple @click="toggle">
          <v-list-tile-action>
            <v-icon>{{ icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>
              {{ allSelected ? "Unselect all" : "Select All" }}
            </v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </template>
      <template v-slot:selection="{ item, index }">
        <v-chip v-if="selected.length === indices.length && index === 0">
          <span>ALL</span>
        </v-chip>
        <span
          v-if="selected.length === indices.length && index === 0"
          class="caption"
        >
          ({{ selected.length }} indices)
        </span>
        <v-chip v-else-if="selected.length !== indices.length">
          <span>{{ item }}</span>
        </v-chip>
      </template>
    </v-select>
  </div>
</template>

<script>
export default {
  props: {
    indices: {
      type: Array,
      required: true
    },
    selected: {
      type: Array,
      required: true
    }
  },
  computed: {
    inner: {
      get() {
        return this.selected;
      },
      set(x) {
        this.$emit("update:selected", x);
      }
    },
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
          this.inner = [];
        } else {
          this.inner = this.indices.slice();
        }
      });
    }
  }
};
</script>
<style scoped></style>

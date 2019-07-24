<template>
  <div>
    <v-select v-model="inner" :items="indices" label="Select indices*" multiple>
      <template v-slot:prepend-item>
        <v-list-item ripple @click="toggle">
          <v-list-item-action>
            <v-icon>{{ icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>
              {{ allSelected ? "Unselect all" : "Select All" }}
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </template>
      <template v-slot:selection="{ item, index }">
        <v-chip v-if="value.length === indices.length && index === 0">
          <span>ALL</span>
        </v-chip>
        <span
          v-if="value.length === indices.length && index === 0"
          class="caption"
        >
          ({{ value.length }} indices)
        </span>
        <v-chip v-else-if="value.length !== indices.length">
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
    value: {
      type: Array,
      required: true
    }
  },
  computed: {
    inner: {
      get() {
        return this.value;
      },
      set(x) {
        this.$emit("input", x);
      }
    },
    allSelected() {
      return this.value.length === this.indices.length;
    },
    likesSomeFruit() {
      return this.value.length > 0 && !this.allSelected;
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

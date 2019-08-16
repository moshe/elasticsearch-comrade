<template>
  <v-chip
    close
    :disabled="removed"
    :color="color"
    label
    outlined
    small
    @click:close="handleRemove"
  >
    <span :class="removed ? 'removed' : added ? 'added' : null">
      {{ alias }}
    </span>
  </v-chip>
</template>

<script>
export default {
  props: {
    alias: {
      type: String
    },
    added: {
      type: Boolean,
      default: false
    },
    removed: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    colorVariant() {
      return this.$vuetify.theme.dark ? "lighten" : "darken";
    },
    color() {
      if (this.added) {
        return `primary ${this.colorVariant}-1`;
      }
      if (this.removed) {
        return "gray";
      }
      return `orange ${this.colorVariant}-2`;
    }
  },
  methods: {
    handleRemove() {
      this.$emit("remove");
    }
  }
};
</script>

<style scoped>
.removed {
  text-decoration: line-through;
}

.added {
  text-decoration: forestgreen;
}
</style>

<template>
  <v-chip
    :close="!removed"
    :color="color"
    label
    outline
    small
    @input="handleRemove"
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
    color() {
      if (this.added) {
        return "yellow";
      }
      if (this.removed) {
        return "gray";
      }
      return "teal";
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

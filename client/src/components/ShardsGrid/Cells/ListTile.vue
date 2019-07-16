<template>
  <v-list-tile @click="action" :disabled="disabled" style="margin-left:24px">
    <v-list-tile-title>{{ title }}</v-list-tile-title>
  </v-list-tile>
</template>

<script>
export default {
  name: "ListTile",
  props: {
    action: {
      type: Function,
      required: true
    },
    title: {
      type: String,
      required: true
    },
    disabled: {
      type: Boolean,
      default: false
    }
  }
};
</script>

<style scoped></style>

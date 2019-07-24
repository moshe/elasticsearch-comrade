<template>
  <v-list-item @click="action" :disabled="disabled" style="margin-left:24px">
    <v-list-item-title>{{ title }}</v-list-item-title>
  </v-list-item>
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

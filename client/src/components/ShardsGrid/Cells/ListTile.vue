<template>
  <v-list-item @click="action" :disabled="disabled" style="padding-left:40px">
    <v-list-item-title :data-tile="dataTitle">{{ title }}</v-list-item-title>
  </v-list-item>
</template>

<script>
export default {
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
  },
  computed: {
    dataTitle() {
      return this.title.replace(" ", "-").toLowerCase();
    }
  }
};
</script>

<style scoped></style>

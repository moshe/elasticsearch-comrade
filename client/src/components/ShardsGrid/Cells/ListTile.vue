<template>
  <v-list-tile @click="action" :disabled="disabled">
    <v-list-tile-action style="min-width: unset" class="pr-2">
      <v-icon style="font-size: 16px" :disabled="disabled" :color="color">
        {{ icon }}
      </v-icon>
    </v-list-tile-action>
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
    icon: {
      type: String,
      required: true
    },
    title: {
      type: String,
      required: true
    },
    disabled: {
      type: Boolean,
      default: false
    },
    color: {
      type: String
    }
  }
};
</script>

<style scoped></style>

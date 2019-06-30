<template>
  <v-combobox
    :items="repos"
    label="Select repository"
    item-text="id"
    @change="repo => $emit('select', repo.id)"
    class="mb-2"
  >
    <template v-slot:item="{ index, item }">
      <v-list-tile-content>
        <v-chip dark label small>{{ item.id }} {{ item.location }} </v-chip>
      </v-list-tile-content>
      <v-list-tile-action>
        <v-chip dark label small>{{ item.type }}</v-chip>
      </v-list-tile-action>
    </template>
  </v-combobox>
</template>

<script>
export default {
  props: {
    repos: {
      type: Array,
      required: true
    }
  }
};
</script>

<style lang="scss" scoped></style>

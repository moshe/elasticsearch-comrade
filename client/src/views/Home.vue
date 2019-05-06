<template>
  <v-container fluid>
    <v-layout column>
      <v-flex>
        <shards-grid />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import ShardsGrid from "../components/ShardsGrid.vue";
export default {
  components: { ShardsGrid },
  data: () => ({})
};
</script>

<style></style>

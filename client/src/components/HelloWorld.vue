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
import ShardsGrid from "./ShardsGrid";
export default {
  components: { ShardsGrid },
  data: () => ({})
};
</script>

<style></style>

<template>
  <v-container>
    <v-layout column>
      <v-flex xs12>
        <v-img :src="require('../assets/logo.svg')" contain height="200" />
      </v-flex>
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

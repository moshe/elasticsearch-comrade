<template>
  <v-container>
    <v-layout column>
      <v-flex xs12>
        <v-img
          :src="require('../assets/logo.svg')"
          contain
          height="200"
        />
      </v-flex>
      <v-flex>
        <mgr-shards-table/>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import MgrShardsTable from "./MgrShardsTable";
export default {
  components: {MgrShardsTable},
  data: () => ({})
};
</script>

<style></style>

<template>
  <v-layout align-center justify-center row>
    <v-flex style="flex: 1" class="ma-2">
      <info-box :text="`Indices: ${cluster.numOfIndices}`" />
    </v-flex>
    <v-flex style="flex: 1" class="ma-2">
      <info-box :text="`Primary Shards: ${cluster.numOfPrimaryShards}`" />
    </v-flex>
    <v-flex style="flex: 1" class="ma-2">
      <info-box :text="`Replica Shards: ${cluster.numOfReplicaShards}`" />
    </v-flex>
    <v-flex style="flex: 1" class="ma-2">
      <info-box :text="`Docs: ${cluster.numberOfDocs.toLocaleString()}`" />
    </v-flex>
    <v-flex style="flex: 1" class="ma-2">
      <info-box :text="`Nodes: ${cluster.numberOfNodes}`" />
    </v-flex>
  </v-layout>
</template>

<script>
import InfoBox from "./InfoBox.vue";
import { mapState } from "vuex";

export default {
  components: { InfoBox },
  computed: { ...mapState(["cluster"]) }
};
</script>

<style scoped></style>

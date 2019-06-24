<template>
  <v-layout align-center justify-center row>
    <v-flex>
      <info-box class="mr-4" :text="`Indices: ${cluster.numOfIndices}`" />
    </v-flex>
    <v-flex>
      <info-box
        class="mr-4"
        :text="`Primary Shards: ${cluster.numOfPrimaryShards}`"
      />
    </v-flex>
    <v-flex>
      <info-box
        class="mr-4"
        :text="`Replica Shards: ${cluster.numOfReplicaShards}`"
      />
    </v-flex>
    <v-flex>
      <info-box
        class="mr-4"
        :text="`Docs: ${cluster.numberOfDocs.toLocaleString()}`"
      />
    </v-flex>
    <v-flex>
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

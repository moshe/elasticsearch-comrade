<template>
  <v-layout align-start justify-space-between column>
    <v-flex grow>
      <div v-if="cluster.relocatingShards && cluster.relocatingShards !== 0">
        <v-progress-circular indeterminate color="white" size="8" width="1" />
        {{ cluster.relocatingShards }} relocating shards
      </div>
    </v-flex>
    <v-flex grow>
      <div
        v-if="cluster.initializingShards && cluster.initializingShards !== 0"
      >
        <v-progress-circular indeterminate color="white" size="8" width="1" />
        {{ cluster.initializingShards }} initializing shards
      </div>
    </v-flex>
    <v-flex shrink>
      <allocation-button />
    </v-flex>
  </v-layout>
</template>

<script>
import { mapState } from "vuex";
import AllocationButton from "../AllocationButton";

export default {
  name: "ClusterCell",
  components: { AllocationButton },
  computed: {
    ...mapState(["cluster"])
  }
};
</script>

<style scoped></style>

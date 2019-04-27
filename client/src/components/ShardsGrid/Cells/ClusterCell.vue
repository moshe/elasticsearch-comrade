<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div style="text-align: left">
    <div v-if="cluster.relocatingShards && cluster.relocatingShards !== 0">
      <v-progress-circular
        indeterminate
        color="white"
        size="8"
        width="1"
      ></v-progress-circular>
      {{ cluster.relocatingShards }} relocating shards
    </div>
    <div v-if="cluster.initializingShards && cluster.initializingShards !== 0">
      <v-progress-circular
        indeterminate
        color="white"
        size="8"
        width="1"
      ></v-progress-circular>
      {{ cluster.initializingShards }} initializing shards
    </div>
    <allocation-button />
  </div>
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

<style scoped>
</style>

<template>
  <div>
    <allocation-button />
    <div v-if="cluster.relocatingShards && cluster.relocatingShards !== 0">
      <v-progress-circular indeterminate color="white" size="8" width="1" />
      {{ cluster.relocatingShards }} relocating shards
    </div>
    <div v-if="cluster.unassignedShards && cluster.unassignedShards !== 0">
      <v-icon size="14">error_outline</v-icon>
      {{ cluster.unassignedShards }} unassigned shards
    </div>
    <div v-if="cluster.initializingShards && cluster.initializingShards !== 0">
      <v-progress-circular indeterminate color="white" size="8" width="1" />
      {{ cluster.initializingShards }} initializing shards
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import AllocationButton from "../AllocationButton.vue";

export default {
  components: { AllocationButton },
  computed: { ...mapState(["cluster"]) }
};
</script>

<style scoped></style>

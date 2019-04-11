<template>
  <div class="node-info ma-1">
    <div class="node-name">
      {{ name }}
    </div>
    <v-layout style="font-size: 8px">
      <v-flex>
        <node-stat-bar :metric="metrics.heapPercent" name="HEAP" />
      </v-flex>
      <v-flex class="pl-1">
        <node-stat-bar :metric="metrics.diskPercent" name="DISK" />
      </v-flex>
      <v-flex class="pl-1">
        <node-stat-bar :metric="metrics.CPUPercent" name="CPU" />
      </v-flex>
      <v-flex class="pl-1">
        <node-stat-bar :metric="metrics.load1Percent" name="LOAD" />
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import NodeStatBar from "./NodeStatBar";
export default {
  name: "MgrNodeInfo",
  components: { NodeStatBar },
  props: {
    name: {
      required: true,
      type: String
    },
    metrics: {
      required: true,
      type: Object
    }
  }
};
</script>

<style scoped>
.node-info {
  max-width: 200px;
}

.node-name {
  font-size: 16px;
}
</style>

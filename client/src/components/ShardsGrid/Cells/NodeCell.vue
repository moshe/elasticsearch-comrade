<template>
  <div class="node-info ma-1">
    <div class="node-name ml-1">
      {{ nodeName }}
    </div>
<!--    <v-icon v-if="isSuitableForRelocation" class="relocate-here">-->
<!--      archive-->
<!--    </v-icon>-->
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
import NodeStatBar from "../NodeStatBar";
import store from "../../../store";

export default {
  name: "NodeCell",
  components: { NodeStatBar },
  props: {
    nodeName: {
      required: true,
      type: String
    },
    metrics: {
      required: true,
      type: Object
    }
  },
  computed: {
    isSuitableForRelocation() {
      if (store.state.shardsMarkedForRelocation.length === 0) {
        return false;
      }
      for (const mark of store.state.shardsMarkedForRelocation) {
        if (mark.nodeName === this.nodeName) {
          return false;
        }
      }
      return true;
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
  display: inline-block;
}

.relocate-here {
  font-size: 16px;
  cursor: pointer;
}
</style>

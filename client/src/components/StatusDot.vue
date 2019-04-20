<template>
  <div class="dot mr-3" v-bind:style="{ backgroundColor: color }"></div>
</template>

<script>
import { mapState } from "vuex";
import { clusterStatus } from "../enums";

export default {
  name: "StatusDot",
  computed: {
    ...mapState(["cluster"]),
    color() {
      if (this.cluster.clusterStatus === clusterStatus.green) {
        return "green";
      }
      if (this.cluster.clusterStatus === clusterStatus.yellow) {
        return "yellow";
      }
      if (this.cluster.clusterStatus === clusterStatus.red) {
        return "red";
      }
      if (this.cluster.clusterStatus === clusterStatus.loading) {
        return "gray";
      }
      throw new Error(`Unknown cluster status ${this.cluster.clusterStatus}`);
    }
  }
};
</script>

<style scoped>
.dot {
  height: 18px;
  width: 18px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
}
</style>

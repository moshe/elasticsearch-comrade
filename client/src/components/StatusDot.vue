<template>
  <div class="dot" v-bind:style="{ backgroundColor: color }"></div>
</template>

<script>
import { clusterStatus } from "../enums";

export default {
  props: {
    status: {
      type: String,
      default: "loading"
    }
  },
  computed: {
    color() {
      if (this.status === clusterStatus.green) {
        return "green";
      }
      if (this.status === clusterStatus.yellow) {
        return "yellow";
      }
      if (this.status === clusterStatus.red) {
        return "red";
      }
      if (this.status === clusterStatus.loading) {
        return "gray";
      }
      throw new Error(`Unknown cluster status ${this.status}`);
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

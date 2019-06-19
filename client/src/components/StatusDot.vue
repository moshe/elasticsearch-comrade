<template>
  <span>
    <v-progress-circular v-if="isLoading" :indeterminate="true" />
    <div v-else class="dot" v-bind:style="{ backgroundColor: color }"></div>
  </span>
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
    isLoading() {
      return this.status === clusterStatus.loading;
    },
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

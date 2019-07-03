<template>
  <span>
    <v-progress-circular :size="20" v-if="isLoading" :indeterminate="true" />
    <v-icon v-else-if="isError" :size="size" color="red">error</v-icon>
    <div
      v-else
      class="dot"
      v-bind:style="{
        backgroundColor: color,
        height: `${size}px`,
        width: `${size}px`
      }"
    />
  </span>
</template>

<script>
import { clusterStatus } from "../enums";
import colors from "vuetify/es5/util/colors";

export default {
  props: {
    status: {
      type: String,
      default: "loading"
    },
    size: {
      type: Number,
      default: 18
    }
  },
  computed: {
    isLoading() {
      return this.status === clusterStatus.loading;
    },
    isError() {
      return this.status === clusterStatus.error;
    },
    color() {
      if (
        [clusterStatus.red, clusterStatus.yellow, clusterStatus.green].indexOf(
          this.status
        ) !== -1
      ) {
        return colors[this.status].accent4;
      }
      throw new Error(`Unknown cluster status ${this.status}`);
    }
  }
};
</script>

<style scoped>
.dot {
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
}
</style>

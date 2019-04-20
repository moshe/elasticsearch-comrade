<template>
  <div class="dot mr-3" v-bind:style="{ backgroundColor: color }"></div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "StatusDot",
  computed: {
    ...mapState(["cluster"]),
    color() {
      if (this.cluster.clusterStatus === "Green") {
        return "green";
      }
      if (this.cluster.clusterStatus === "Yellow") {
        return "yellow";
      }
      return "red";
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

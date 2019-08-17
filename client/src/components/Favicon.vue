<template>
  <div />
</template>

<script>
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState(["cluster"]),
    status() {
      return this.cluster.clusterStatus;
    }
  },
  watch: {
    status(newValue, oldValue) {
      document
        .querySelectorAll("link[rel*='icon']")
        .forEach(x => (x.href = x.href.replace(oldValue, newValue)));
    }
  }
};
</script>

<style lang="scss" scoped></style>

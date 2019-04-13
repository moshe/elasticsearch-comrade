<template>
  <v-layout column fill-height class="index-cell">
    <v-flex grow>
      <div class="index-name">{{ index }}</div>
    </v-flex>
    <v-flex shrink>
      <div class="index-info">shards 5 * 1 | docs: 123,133 | size: 112.32mb | nodes: 12</div>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: "IndexCell",
  props: {
    index: {
      required: true,
      type: String
    }
  }
};
</script>

<style scoped>
.index-cell {
  text-align: left;
  height: 80px;
}
.index-name {
  font-size: 14px;
}
.index-info {
  max-width: 13vw;
  white-space: pre-wrap;
  font-size: 11px;
}
</style>

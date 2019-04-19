<template>
  <v-layout column fill-height class="index-cell">
    <v-flex grow>
      <div class="index-name">{{ index }}</div>
    </v-flex>
    <v-flex shrink>
      <!--      eslint-disable-next-line -->
      <div class="index-info">shards {{primaries}} * {{replicas}} | docs: {{docsCount.toLocaleString()}} | size: {{storeSize}}</div>
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
    },
    storeSize: {
      required: true,
      type: String
    },
    primaries: {
      required: true,
      type: Number
    },
    replicas: {
      required: true,
      type: Number
    },
    docsCount: {
      required: true,
      type: Number,
      default: 0
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

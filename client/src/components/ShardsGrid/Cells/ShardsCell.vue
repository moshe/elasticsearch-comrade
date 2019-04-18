<template>
  <div v-if="index" style="max-width: 13vw">
    <span v-if="index.primaries">
      <shard-square
        :id="x.shard"
        :state="x.state"
        :progress="x.progress"
        :index="indexName"
        :node-name="nodeName"
        :key="x"
        v-for="x in index.primaries"
        :primary="true"
      />
    </span>
    <span v-if="index.replicas">
      <shard-square
        :id="x.shard"
        :state="x.state"
        :progress="x.progress"
        :index="indexName"
        :node-name="nodeName"
        :key="x"
        v-for="x in index.replicas"
        :primary="false"
      />
    </span>
  </div>
</template>

<script>
import ShardSquare from "../ShardSquare";
export default {
  name: "ShardsCell",
  props: {
    index: {
      required: true
    },
    nodeName: {
      type: String,
      required: true
    },
    indexName: {
      type: String,
      required: true
    }
  },
  components: { ShardSquare }
};
</script>

<style scoped></style>

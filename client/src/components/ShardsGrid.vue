<template>
  <div class="shards-grid" :style="cssProps">
    <cluster-info-boxes class="mt-4 mb-4" />
    <v-layout class="mb-2">
      <v-flex>
        <v-layout>
          <v-flex xs4>
            <v-text-field
              clearable
              label="Filter indices"
              v-model="indexSearch"
              hide-details
            />
          </v-flex>
          <v-flex>
            <v-checkbox
              color="blue-grey lighten-4"
              label="Show Hidden"
              v-model="showHidden"
              hide-details
            />
            <v-checkbox
              color="blue-grey lighten-4"
              label="Show Green Indices"
              v-model="showGreen"
              hide-details
            />
          </v-flex>
        </v-layout>
      </v-flex>
      <v-flex shrink>
        <v-btn
          text
          icon
          @click="page--"
          :disabled="page * perPage - perPage < 0"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
        {{ page * perPage + 1 }} -
        {{ Math.min(page * perPage + perPage, indices.length) }} /
        {{ indices.length }}
        <v-btn
          text
          icon
          @click="page++"
          :disabled="(page + 1) * perPage >= indices.length"
        >
          <v-icon>mdi-chevron-right</v-icon>
        </v-btn>
      </v-flex>
    </v-layout>
    <div class="elevation-6 shards-table">
      <v-layout>
        <v-flex class="pa-1 cell" style="flex:1.1">
          <cluster-cell />
        </v-flex>
        <v-flex class="pa-1 cell" v-for="index of currentIndices" :key="index">
          <index-cell :indexName="index" />
        </v-flex>
        <v-flex
          class="pa-1 cell"
          v-for="index of Math.abs(
            Math.min(currentIndices.length - perPage, 0)
          )"
          :key="index"
        />
      </v-layout>
      <v-layout v-for="node in nodes" :key="node.name">
        <v-flex class="cell pa-1" style="flex:1.1">
          <node-cell
            :node-name="node.name"
            :node-ip="node.ip"
            :metrics="node.metrics"
          />
        </v-flex>
        <v-flex v-for="index of currentIndices" :key="index" class="pa-1 cell">
          <shards-cell
            :node-name="node.name"
            :index="node.indices[index]"
            :index-name="index"
          />
        </v-flex>
        <v-flex
          v-for="index in Math.abs(
            Math.min(currentIndices.length - perPage, 0)
          )"
          :key="index"
          class="pa-1 cell"
        />
      </v-layout>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import NodeCell from "./ShardsGrid/Cells/NodeCell.vue";
import ShardsCell from "./ShardsGrid/Cells/ShardsCell.vue";
import IndexCell from "./ShardsGrid/Cells/IndexCell.vue";
import ClusterInfoBoxes from "./ClusterInfoBoxes.vue";
import ClusterCell from "./ShardsGrid/Cells/ClusterCell.vue";

export default {
  components: {
    ClusterCell,
    ClusterInfoBoxes,
    IndexCell,
    ShardsCell,
    NodeCell
  },
  computed: {
    ...mapState(["nodes", "cluster"]),
    ...mapState({ indicesInfo: "indices" }),
    currentIndices() {
      return this.indices.slice(
        this.page * this.perPage,
        this.page * this.perPage + this.perPage
      );
    },
    indices() {
      return Object.keys(this.indicesInfo)
        .filter(
          index =>
            RegExp(this.indexSearch || "").test(index) ||
            this.indicesInfo[index].aliases.filter(alias =>
              RegExp(this.indexSearch || "").test(alias)
            ).length > 0
        )
        .filter(index => (this.showHidden ? true : !index.startsWith(".")))
        .filter(index =>
          this.showGreen ? true : this.indicesInfo[index].unassignedShards
        );
    },
    cssProps() {
      return {
        "--border-color": this.$vuetify.theme.dark
          ? "rgba(255, 255, 255, 0.14)"
          : "rgba(0, 0, 0, 0.14)"
      };
    }
  },
  data() {
    return {
      page: 0,
      indexSearch: "",
      perPage: 6,
      showHidden: true,
      showGreen: true
    };
  },
  watch: {
    indexSearch() {
      this.page = 0;
    }
  }
};
</script>

<style>
.cell {
  border-left: 1px solid var(--border-color);
  border-bottom: 1px solid var(--border-color);
  flex: 1;
}

.shards-table {
  border-top: 1px solid var(--border-color);
  border-right: 1px solid var(--border-color);
}
</style>

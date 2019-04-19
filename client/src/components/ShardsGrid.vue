<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <cluster-info-boxes />
    <v-layout align-end justify-end row>
      <v-flex shrink>
        <v-btn
          flat
          icon
          @click="page--"
          :disabled="page * perPage - perPage < 0"
        >
          <v-icon>{{ $vuetify.icons.prev }}</v-icon>
        </v-btn>
        {{ page * perPage }} - {{ page * perPage + perPage }}
        <v-btn
          flat
          icon
          @click="page++"
          :disabled="page * perPage + perPage >= indices.length + perPage"
        >
          <v-icon>{{ $vuetify.icons.next }}</v-icon>
        </v-btn>
      </v-flex>
    </v-layout>
    <v-data-table :items="nodes" class="elevation-1" hide-actions>
      <template slot="headers">
        <th class="pa-2">
          <cluster-cell />
        </th>
        <th class="pa-2" v-for="index of indices" :key="index">
          <index-cell
            :index="index"
            :primaries="indicesInfo[index]['primaries']"
            :replicas="indicesInfo[index]['replicas']"
            :docs-count="indicesInfo[index]['docsCount']"
            :store-size="indicesInfo[index]['storeSize']"
          />
        </th>
        <th
          class="pl-1 pr-1"
          v-for="index of Math.abs(Math.min(indices.length - perPage, 0))"
          :key="index"
        ></th>
      </template>
      <template v-slot:items="props">
        <td class="pl-0 pr-0" style="max-width: 200px; min-width: 180px">
          <node-cell
            :node-name="props.item.name"
            :metrics="props.item.metrics"
          />
        </td>
        <td v-for="index of indices" :key="index" class="pa-1 shards-cell">
          <shards-cell
            :node-name="props.item.name"
            :index="props.item.indices[index]"
            :index-name="index"
          />
        </td>
        <td
          v-for="index in Math.abs(Math.min(indices.length - perPage, 0))"
          :key="index"
          class="pa-1 shards-cell"
        ></td>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import NodeCell from "./ShardsGrid/Cells/NodeCell";
import ShardsCell from "./ShardsGrid/Cells/ShardsCell";
import IndexCell from "./ShardsGrid/Cells/IndexCell";
import { mapActions, mapState } from "vuex";
import ClusterInfoBoxes from "./ClusterInfoBoxes";
import ClusterCell from "./ShardsGrid/Cells/ClusterCell";

export default {
  name: "MgrShardsTable",
  components: {
    ClusterCell,
    ClusterInfoBoxes,
    IndexCell,
    ShardsCell,
    NodeCell
  },
  computed: {
    ...mapState(["nodes", "settingsRefreshEvery", "cluster"]),
    ...mapState({ indicesInfo: "indices" }),
    uniqueIndices() {
      return [
        ...new Set([].concat(...this.nodes.map(x => Object.keys(x.indices))))
      ];
    },
    indices() {
      return this.uniqueIndices.slice(
        this.page * this.perPage,
        this.page * this.perPage + this.perPage
      );
    }
  },
  async created() {
    await this.updateData();
  },
  methods: {
    ...mapActions(["shardsGrid"]),
    async updateData() {
      await this.shardsGrid();
      setTimeout(this.updateData, this.settingsRefreshEvery);
    }
  },
  data() {
    return {
      page: 0,
      perPage: 5
    };
  }
};
</script>

<style>
.shards-cell {
  border-left: 1px solid rgba(255, 255, 255, 0.12);
  min-width: 200px;
}
th,
td {
  vertical-align: top;
}
</style>

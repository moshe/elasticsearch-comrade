<template>
  <div>
    <cluster-info-boxes class="mt-3 mb-3" />
    <v-layout align-end justify-end row>
      <v-flex>
        <v-layout>
          <v-flex xs4>
            <v-text-field
              clearable
              label="Filter indices"
              v-model="indexSearch"
              class="pr-4"
            />
          </v-flex>
          <v-flex>
            <v-checkbox label="Include Hidden" v-model="includeHidden" />
          </v-flex>
        </v-layout>
      </v-flex>
      <v-flex shrink>
        <v-btn
          flat
          icon
          @click="page--"
          :disabled="page * perPage - perPage < 0"
        >
          <v-icon>{{ $vuetify.icons.prev }}</v-icon>
        </v-btn>
        {{ page * perPage + 1 }} -
        {{ Math.min(page * perPage + perPage, indices.length) }} /
        {{ indices.length }}
        <v-btn
          flat
          icon
          @click="page++"
          :disabled="(page + 1) * perPage >= indices.length"
        >
          <v-icon>{{ $vuetify.icons.next }}</v-icon>
        </v-btn>
      </v-flex>
    </v-layout>
    <v-data-table :items="nodes" class="elevation-3" hide-actions>
      <template slot="headers">
        <th class="pa-2">
          <cluster-cell />
        </th>
        <th class="pa-2" v-for="index of currentIndices" :key="index">
          <index-cell :indexName="index" />
        </th>
        <th
          class="pl-1 pr-1"
          v-for="index of Math.abs(
            Math.min(currentIndices.length - perPage, 0)
          )"
          :key="index"
        ></th>
      </template>
      <template v-slot:items="props">
        <td class="pl-0 pr-0" style="max-width: 200px; min-width: 180px">
          <node-cell
            :node-name="props.item.name"
            :node-ip="props.item.ip"
            :metrics="props.item.metrics"
          />
        </td>
        <td
          v-for="index of currentIndices"
          :key="index"
          class="pa-1 shards-cell"
        >
          <shards-cell
            :node-name="props.item.name"
            :index="props.item.indices[index]"
            :index-name="index"
          />
        </td>
        <td
          v-for="index in Math.abs(
            Math.min(currentIndices.length - perPage, 0)
          )"
          :key="index"
          class="pa-1 shards-cell"
        />
      </template>
    </v-data-table>
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
  name: "MgrShardsTable",
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
            (this.indicesInfo[index].aliases || []).filter(alias =>
              RegExp(this.indexSearch || "").test(alias)
            ).length > 0
        )
        .filter(index => (this.includeHidden ? true : !index.startsWith(".")));
    }
  },
  data() {
    return {
      page: 0,
      indexSearch: "",
      perPage: 5,
      includeHidden: true
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
.shards-cell {
  border-left: 1px solid rgba(255, 255, 255, 0.12);
  min-width: 200px;
}
th,
td {
  vertical-align: top;
}

div.v-text-field__details {
  display: none;
}
</style>

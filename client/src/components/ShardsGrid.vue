<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <v-layout align-end justify-end row>
      <v-flex shrink>
        <v-btn flat icon @click="page--" :disabled="(page * perPage - perPage) < 0">
          <v-icon>{{$vuetify.icons.prev}}</v-icon>
        </v-btn>
        {{page * perPage}} - {{page * perPage + perPage}}
        <v-btn flat icon @click="page++" :disabled="(page * perPage + perPage) > (indices.length + perPage)">
          <v-icon>{{$vuetify.icons.next}}</v-icon>
        </v-btn>
      </v-flex>
    </v-layout>
    <v-data-table :items="nodes" class="elevation-1">
      <template slot="headers">
        <th class="pl-1 pr-1"><div style="text-align: left">Node</div></th>
        <th class="pl-1 pr-1" v-for="index of indices" :key="index">
          <index-cell :index="index" />
        </th>
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
      </template>
    </v-data-table>
  </div>
</template>

<script>
import NodeCell from "./ShardsGrid/Cells/NodeCell";
import store from "../store";
import ShardsCell from "./ShardsGrid/Cells/ShardsCell";
import IndexCell from "./ShardsGrid/Cells/IndexCell";

export default {
  name: "MgrShardsTable",
  components: { IndexCell, ShardsCell, NodeCell },
  computed: {
    uniqueIndices() {
      return [
        ...new Set([].concat(...this.nodes.map(x => Object.keys(x.indices))))
      ];
    },
    indices() {
      return this.uniqueIndices.slice(this.page * this.perPage, this.page * this.perPage + this.perPage);
    },
    lol() {
      return store.state.shardsMarkedForRelocation;
    }
  },
  async created() {
    const a = await fetch("/api/v1/shards_grid");
    const b = await a.json();
    this.nodes = b;
  },
  data() {
    return {
      page: 0,
      perPage: 5,
      indicesInfo: {
        "logstash-1234": {
          shards: 10,
          replicas: 2,
          docs: 12,
          sizeBytes: 10012
        }
      },
      nodes: []
      // nodes: [
      //   {
      //     name: "Frozen Yogurt",
      //     indices: {
      //       index1: {
      //         replicas: [1, 2, 3, 4, 5],
      //         primaries: [6, 7, 8]
      //       },
      //       index2: {
      //         replicas: [1, 2, 3, 4, 5, 6, 7, 8],
      //         primaries: [9]
      //       }
      //     },
      //     metrics: {
      //       heapPercent: 15,
      //       diskPercent: 45,
      //       CPUPercent: 65,
      //       load1Percent: 4
      //     }
      //   },
      //   {
      //     name: "Ice cream sandwich",
      //     indices: {
      //       index3: {
      //         replicas: [9, 2, 3],
      //         primaries: [1, 4, 5, 6, 7, 8]
      //       }
      //     },
      //     metrics: {
      //       heapPercent: 85,
      //       diskPercent: 35,
      //       CPUPercent: 14,
      //       load1Percent: 80
      //     }
      //   },
      //   {
      //     name: "Eclair",
      //     indices: {
      //       index3: {
      //         replicas: [1, 4, 5, 6, 7, 8],
      //         primaries: [2, 3]
      //       },
      //       index5: {
      //         replicas: [],
      //         primaries: [1, 2, 3, 4, 5, 6, 7, 8]
      //       }
      //     },
      //     metrics: {
      //       heapPercent: 35,
      //       diskPercent: 15,
      //       CPUPercent: 97,
      //       load1Percent: 81
      //     }
      //   },
      //   {
      //     name: "Cupcake",
      //     indices: {
      //       index1: {
      //         replicas: [6, 7, 8],
      //         primaries: [1, 2, 3, 4, 5]
      //       },
      //       index4: {
      //         replicas: [9],
      //         primaries: [1, 2, 3, 4, 5, 6, 7, 8]
      //       }
      //     },
      //     metrics: {
      //       heapPercent: 11,
      //       diskPercent: 15,
      //       CPUPercent: 4,
      //       load1Percent: 7
      //     }
      //   }
      //   // {
      //   //   nodeName: "Gingerbread"
      //   // },
      //   // {
      //   //   nodeName: "Jelly bean"
      //   // },
      //   // {
      //   //   nodeName: "Lollipop"
      //   // },
      //   // {
      //   //   nodeName: "Honeycomb"
      //   // },
      //   // {
      //   //   nodeName: "Donut"
      //   // },
      //   // {
      //   //   nodeName: "KitKat"
      //   // }
      // ]
    };
  }
};
</script>

<style>
.shards-cell {
  border-left: 1px solid rgba(255, 255, 255, 0.12);
}
th,
td {
  vertical-align: top;
}
</style>

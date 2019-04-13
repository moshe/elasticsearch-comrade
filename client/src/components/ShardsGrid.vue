<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <div>
    <v-data-table :items="nodes" class="elevation-1">
      <template slot="headers">
        <th class="pl-1 pr-1"><div style="text-align: left">Node</div></th>
        <th class="pl-1 pr-1" v-for="index of indices" :key="index">
          <div style="text-align: left">{{ index }}</div>
        </th>
      </template>
      <template v-slot:items="props">
        <td class="pl-0 pr-0">
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
import ShardSquare from "./ShardsGrid/ShardSquare";
import store from "../store";
import ShardsCell from "./ShardsGrid/Cells/ShardsCell";

export default {
  name: "MgrShardsTable",
  components: { ShardsCell, ShardSquare, NodeCell },
  computed: {
    indices() {
      return [
        ...new Set([].concat(...this.nodes.map(x => Object.keys(x.indices))))
      ];
    },
    lol() {
      return store.state.shardsMarkedForRelocation;
    }
  },
  data() {
    return {
      nodes: [
        {
          name: "Frozen Yogurt",
          indices: {
            index1: {
              replicas: [1, 2, 3, 4, 5],
              primaries: [6, 7, 8]
            },
            index2: {
              replicas: [1, 2, 3, 4, 5, 6, 7, 8],
              primaries: [9]
            }
          },
          metrics: {
            heapPercent: 15,
            diskPercent: 45,
            CPUPercent: 65,
            load1Percent: 4
          }
        },
        {
          name: "Ice cream sandwich",
          indices: {
            index3: {
              replicas: [9, 2, 3],
              primaries: [1, 4, 5, 6, 7, 8]
            }
          },
          metrics: {
            heapPercent: 85,
            diskPercent: 35,
            CPUPercent: 14,
            load1Percent: 80
          }
        },
        {
          name: "Eclair",
          indices: {
            index3: {
              replicas: [1, 4, 5, 6, 7, 8],
              primaries: [2, 3]
            },
            index5: {
              replicas: [],
              primaries: [1, 2, 3, 4, 5, 6, 7, 8]
            }
          },
          metrics: {
            heapPercent: 35,
            diskPercent: 15,
            CPUPercent: 97,
            load1Percent: 81
          }
        },
        {
          name: "Cupcake",
          indices: {
            index1: {
              replicas: [6, 7, 8],
              primaries: [1, 2, 3, 4, 5]
            },
            index4: {
              replicas: [9],
              primaries: [1, 2, 3, 4, 5, 6, 7, 8]
            }
          },
          metrics: {
            heapPercent: 11,
            diskPercent: 15,
            CPUPercent: 4,
            load1Percent: 7
          }
        }
        // {
        //   nodeName: "Gingerbread"
        // },
        // {
        //   nodeName: "Jelly bean"
        // },
        // {
        //   nodeName: "Lollipop"
        // },
        // {
        //   nodeName: "Honeycomb"
        // },
        // {
        //   nodeName: "Donut"
        // },
        // {
        //   nodeName: "KitKat"
        // }
      ]
    };
  }
};
</script>

<style scoped>
.shards-cell {
  border-left: 1px solid rgba(255, 255, 255, 0.12);
  vertical-align: top;
}
</style>

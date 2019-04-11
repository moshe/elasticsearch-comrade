<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-data-table :items="nodes" class="elevation-1" :headers="['a', '1', '2']">
    <template slot="headers">
      <th class="pl-1 pr-1"><div style="text-align: left">Node</div></th>
      <th class="pl-1 pr-1" v-for="index of indices" :key="index">
        <div style="text-align: left">{{ index }}</div>
      </th>
    </template>
    <template v-slot:items="props">
      <td class="pl-1 pr-1">
        <mgr-node-info :name="props.item.name" :metrics="props.item.metrics" />
      </td>
      <td
        v-for="index of indices"
        :key="index"
        style="border-left: 1px solid rgba(255,255,255,0.12)"
        class="pl-1 pr-1"
      >
        <div v-if="props.item.indices[index]" style="max-width: 13vw">
          <span v-if="props.item.indices[index].primaries">
            <shard-square
              :id="x"
              :key="x"
              v-for="x in props.item.indices[index].primaries"
              :primary="true"
            />
          </span>
          <span v-if="props.item.indices[index].replicas">
            <shard-square
              :id="x"
              :key="x"
              v-for="x in props.item.indices[index].replicas"
              :primary="false"
            />
          </span>
        </div>
      </td>
    </template>
  </v-data-table>
</template>

<script>
import MgrNodeInfo from "./MgrShardsTableComponents/MgrNodeInfo";
import ShardSquare from "./MgrShardsTableComponents/ShardSquare";

export default {
  name: "MgrShardsTable",
  components: { ShardSquare, MgrNodeInfo },
  computed: {
    indices() {
      return [
        ...new Set([].concat(...this.nodes.map(x => Object.keys(x.indices))))
      ];
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
        //   name: "Gingerbread"
        // },
        // {
        //   name: "Jelly bean"
        // },
        // {
        //   name: "Lollipop"
        // },
        // {
        //   name: "Honeycomb"
        // },
        // {
        //   name: "Donut"
        // },
        // {
        //   name: "KitKat"
        // }
      ]
    };
  }
};
</script>

<style scoped></style>

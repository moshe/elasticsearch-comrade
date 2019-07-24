<template>
  <v-layout column>
    <v-flex>
      <v-layout wrap>
        <v-flex xs4 v-for="(items, name) in cards" :key="name">
          <v-card class="ma-2" color="light-blue ">
            <v-card-title class="subtitle-1 font-weight-bold">
              {{ name }}
            </v-card-title>
            <v-divider />
            <v-list dense>
              <v-list-item v-for="{ key, value } in items" :key="key">
                <v-list-item-content>{{ key }}:</v-list-item-content>
                <v-list-item-content class="align-end">
                  {{ value }}
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-flex>
      </v-layout>
    </v-flex>
    <v-flex>
      <v-layout wrap>
        <v-flex
          xs6
          v-for="x in [
            Array.from({ length: 30 }, () =>
              Math.ceil(Math.random() * (120 - 80) + 80)
            ),
            Array.from({ length: 30 }, () =>
              Math.ceil(Math.random() * (120 - 80) + 80)
            ),
            Array.from({ length: 30 }, () =>
              Math.ceil(Math.random() * (120 - 80) + 80)
            ),
            Array.from({ length: 30 }, () =>
              Math.ceil(Math.random() * (120 - 80) + 80)
            )
          ]"
          :key="x"
          class="pa-2"
        >
          <v-card class="mx-auto text-xs-center" color="green">
            <v-card-text>
              <v-sheet color="rgba(0, 0, 0, .12)">
                <v-sparkline
                  key="15"
                  smooth
                  color="rgba(255, 255, 255, .7)"
                  :value="x"
                  auto-draw
                  height="100"
                  padding="14"
                  stroke-linecap="round"
                >
                  <template v-slot:label="item">
                    {{ item.index % 2 === 0 ? item.value : "" }}
                  </template>
                </v-sparkline>
              </v-sheet>
            </v-card-text>
            <v-card-text>
              <div class="display-1 font-weight-thin">Sales Last 24h</div>
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  data() {
    return {
      heartbeats: Array.from({ length: 30 }, () =>
        Math.ceil(Math.random() * (120 - 80) + 80)
      ),
      cards: {
        Details: [
          { key: "ip", value: "10.31.45.13" },
          { key: "Roles", value: "Data,Master" },
          { key: "Home Path", value: "/mnt/data" },
          { key: "Data Path", value: "/mnt/" },
          { key: "Conf Path", value: "/mnt/conf" },
          { key: "Logs Path", value: "/mnt/logs" }
        ],
        "Thread Pools": [
          { key: "index", value: "0/10" },
          { key: "search", value: "5/10" },
          { key: "bulk", value: "2/18" },
          { key: "get", value: "1/14" },
          { key: "snapshot", value: "5/12" },
          { key: "management", value: "12/12" }
        ],
        JVM: [
          { key: "pid", value: "24258" },
          { key: "version", value: "1.8.0_91" },
          { key: "vm_name", value: "Java HotSpot(TM) 64-Bit Server VM" },
          { key: "vm_vendor", value: "Oracle Corporation" },
          { key: "uptime", value: "1 day ago" },
          { key: "heap_max", value: "10gb" }
        ]
      }
    };
  }
};
</script>

<style lang="scss" scoped></style>

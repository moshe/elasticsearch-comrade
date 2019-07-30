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
              <v-list-item v-for="(value, key) in items" :key="key">
                <v-list-item-content>{{ key }}:</v-list-item-content>
                <v-list-item-content>{{ value }}</v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card>
        </v-flex>
      </v-layout>
    </v-flex>
    <v-flex>
      <v-layout wrap>
        <v-flex xs12>
          <v-header>Thread Pools</v-header>
        </v-flex>
        <v-flex xs4 class="pa-1">
          <v-layout wrap>
            <v-flex
              xs3
              v-for="(v, k) in threadPools"
              :key="k"
              class="pa-3"
              :class="{ 'elevation-6': k === 'analyze' }"
            >
              <div style="font-size: 10px">{{ k }}</div>
              <v-sparkline
                key="15"
                smooth
                color="rgba(255, 255, 255, .7)"
                :value="v['active']"
                auto-draw
                height="90px"
                stroke-linecap="round"
              >
                <template v-slot:label="item">
                  {{ item.index % 2 === 0 ? item.value : "" }}
                </template>
              </v-sparkline>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex xs8 class="pa-1">
          <v-card class="mx-auto text-xs-center" color="green">
            <v-card-text>
              <v-sheet color="rgba(0, 0, 0, .12)">
                <v-sparkline
                  key="15"
                  smooth
                  color="rgba(255, 255, 255, .7)"
                  :value="[1, 2, 3, 4]"
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
    <!-- <div v-for="stat in threadPools.search.active" :key="stat">
      {{ stat }}
    </div> -->
  </v-layout>
</template>

<script>
import nodeApis from "../mixins/nodeApis";
import VHeader from "../components/Base/Header.vue";
export default {
  props: {
    nodeId: {
      type: String,
      required: true
    }
  },
  mixins: [nodeApis],
  components: { VHeader },
  async created() {
    this.cards = await this.getNodeInfo(this.nodeId);
    setInterval(this.collect, 1000);
    // this.collect();
  },
  methods: {
    async collect() {
      const stats = await this.getNodeStats(this.nodeId);
      for (const [k, v] of Object.entries(stats.threadPool)) {
        if (!this.threadPools[k]) {
          // this.threadPools[k] = { active: [v["active"]] };
        } else {
          this.threadPools[k]["active"].push(v["active"]);
        }
      }
    }
  },
  data() {
    return {
      heartbeats: Array.from({ length: 30 }, () =>
        Math.ceil(Math.random() * (120 - 80) + 80)
      ),
      cards: {},
      stats: { threadPools: [123] },
      threadPools: {
        analyze: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        data_frame_indexing: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        fetch_shard_started: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        fetch_shard_store: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        flush: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        force_merge: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        generic: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        get: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        listener: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        management: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        ml_datafeed: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        ml_job_comms: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        ml_utility: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        refresh: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        rollup_indexing: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        search: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        search_throttled: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        "security-token-key": {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        snapshot: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        warmer: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        watcher: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        },
        write: {
          threads: [],
          queue: [],
          active: [],
          rejected: [],
          largest: [],
          completed: []
        }
      }
    };
  }
};
</script>

<style lang="scss" scoped></style>

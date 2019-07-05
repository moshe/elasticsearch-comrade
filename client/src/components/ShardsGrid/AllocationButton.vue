<template>
  <v-menu offset-y>
    <template v-slot:activator="{ on }">
      <v-btn small color="accent" v-on="on" :disabled="loading">
        <v-icon size="12px" dark class="mr-1">{{ icon }}</v-icon>
        Allocation
      </v-btn>
    </template>
    <v-list dense two-line>
      <div v-for="({ name, text }, i) in options" :key="name">
        <v-list-tile :disabled="name === current" @click="click(name)">
          <v-list-tile-content>
            <v-list-tile-title>{{ name }}</v-list-tile-title>
            <v-list-tile-sub-title>
              {{ text }}
            </v-list-tile-sub-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-divider v-if="i !== options.length - 1" />
      </div>
    </v-list>
  </v-menu>
</template>

<script>
import clusterApis from "../../mixins/clusterApis";
import { mapActions, mapState } from "vuex";

export default {
  name: "AllocationButton",
  mixins: [clusterApis],
  computed: {
    ...mapState(["cluster"]),
    current() {
      return this.cluster.settings.allocation;
    },
    icon() {
      return this.current === "all" ? "lock_open" : "lock";
    },
    loading() {
      return this.duringRequest || !this.current;
    }
  },
  methods: {
    ...mapActions(["shardsGrid"]),
    async click(name) {
      this.duringRequest = true;
      await this.setAllocation(name);
      await this.shardsGrid();
      this.duringRequest = false;
    }
  },
  data() {
    return {
      duringRequest: false,
      options: [
        {
          name: "all",
          text: "(default) Allows shard allocation for all kinds of shards"
        },
        {
          name: "primaries",
          text: "Allows shard allocation only for primary shards"
        },
        {
          name: "new_primaries",
          text:
            "Allows shard allocation only for primary shards for new indices"
        },
        {
          name: "none",
          text: "No shard allocations of any kind are allowed for any indices"
        }
      ]
    };
  }
};
</script>

<style scoped>
.v-btn--small {
  height: 18px;
  padding: 3px 7px;
  font-size: 9px !important;
  margin: 0;
}
.v-btn {
  min-width: 50px;
}
</style>

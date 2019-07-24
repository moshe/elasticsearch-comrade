<template>
  <div class="ma-2">
    <v-menu offset-y style="display: inline-block">
      <template v-slot:activator="{ on }">
        <div class="node-name ml-1" v-on="on">{{ nodeName }}</div>
      </template>
      <v-list dense>
        <v-list-item @click="$router.push(`/node/${nodeName}`)">
          <v-list-item-title>Show Info</v-list-item-title>
        </v-list-item>

        <v-list-item :disabled="!isSuitableForRelocation" @click="relocate">
          <v-list-item-title>Relocate</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    <div class="ip ml-1 mb-2">{{ nodeIp }}</div>
    <v-layout style="font-size: 8px">
      <v-flex>
        <node-stat-bar :metric="metrics.heapPercent" name="HEAP" />
      </v-flex>
      <v-flex class="pl-1">
        <node-stat-bar :metric="metrics.diskPercent" name="DISK" />
      </v-flex>
      <v-flex class="pl-1">
        <node-stat-bar :metric="metrics.CPUPercent" name="CPU" />
      </v-flex>
      <v-flex class="pl-1">
        <node-stat-bar :metric="metrics.load1Percent" name="LOAD" />
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import NodeStatBar from "../NodeStatBar.vue";
import { mapMutations, mapState } from "vuex";
import { POST } from "../../../requests";

export default {
  components: { NodeStatBar },
  props: {
    nodeName: {
      required: true,
      type: String
    },
    nodeIp: {
      required: true,
      type: String
    },
    metrics: {
      required: true,
      type: Object
    }
  },
  methods: {
    ...mapMutations(["clearRelocation", "startLoading", "stopLoading"]),
    async relocate() {
      this.startLoading();
      const res = await POST("/api/v1/cluster/reroute_shards", {
        node: this.nodeName,
        shards: this.shardsMarkedForRelocation
      });
      if (res.status === "ok") {
        this.clearRelocation();
      }
      this.stopLoading();
    }
  },
  computed: {
    ...mapState(["shardsMarkedForRelocation"]),
    isSuitableForRelocation() {
      if (this.shardsMarkedForRelocation.length === 0) {
        return false;
      }
      for (const mark of this.shardsMarkedForRelocation) {
        if (mark.nodeName === this.nodeName) {
          return false;
        }
      }
      return true;
    }
  }
};
</script>

<style scoped>
.node-name {
  font-size: 14px;
  display: inline-block;
  cursor: pointer;
}

.ip {
  font-size: 10px;
  color: #bdbdbd;
}

.relocate-here {
  font-size: 16px;
  cursor: pointer;
}

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

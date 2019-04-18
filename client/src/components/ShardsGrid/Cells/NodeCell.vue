<template>
  <div class="node-info ma-1">
    <div class="node-name ml-1">
      {{ nodeName }}
    </div>
    <v-layout style="font-size: 8px">
      <v-flex>
        <node-stat-bar :metric="metrics.heapPercent" name="HEAP" />
      </v-flex>
      <v-flex>
        <node-stat-bar :metric="metrics.heapPercent" name="DISK" />
      </v-flex>
      <!--      <v-flex class="pl-1">-->
      <!--        <node-stat-bar :metric="metrics.diskPercent" name="DISK" />-->
      <!--      </v-flex>-->
      <v-flex class="pl-1">
        <node-stat-bar :metric="metrics.CPUPercent" name="CPU" />
      </v-flex>
      <v-flex class="pl-1">
        <node-stat-bar :metric="metrics.load1Percent" name="LOAD" />
      </v-flex>
    </v-layout>
    <v-layout class="ma-2">
      <v-flex>
        <v-btn
          @click="relocate"
          :disabled="!isSuitableForRelocation"
          small
          color="primary"
          round
          >Relocate</v-btn
        >
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import NodeStatBar from "../NodeStatBar";
import store from "../../../store";
import { mapMutations } from "vuex";

export default {
  name: "NodeCell",
  components: { NodeStatBar },
  props: {
    nodeName: {
      required: true,
      type: String
    },
    metrics: {
      required: true,
      type: Object
    }
  },
  methods: {
    ...mapMutations(["clearRelocation"]),
    async relocate() {
      const res = await fetch("/api/v1/cluster/reroute_shards", {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          node: this.nodeName,
          shards: store.state.shardsMarkedForRelocation
        })
      });
      if ((await res.json()).status === "ok") {
        this.clearRelocation();
      }
    }
  },
  computed: {
    isSuitableForRelocation() {
      if (store.state.shardsMarkedForRelocation.length === 0) {
        return false;
      }
      for (const mark of store.state.shardsMarkedForRelocation) {
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
.node-info {
  /*max-width: 200px;*/
}

.node-name {
  font-size: 14px;
  display: inline-block;
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

<template>
  <v-menu offset-y>
    <template v-slot:activator="{ on }">
      <div v-on="on" class="allocation-text">
        <span>Allocation: {{ current }}</span>
        <v-icon size="16">arrow_drop_down</v-icon>
      </div>
    </template>
    <v-list dense two-line>
      <div v-for="({ name, text }, i) in options" :key="name">
        <v-list-item :disabled="name === current" @click="click(name)">
          <v-list-item-content>
            <v-list-item-title>{{ name }}</v-list-item-title>
            <v-list-item-subtitle>
              {{ text }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
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
.allocation-text {
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 2px;
  cursor: pointer;
  font-size: 12px;
  max-width: 90px;
}
</style>

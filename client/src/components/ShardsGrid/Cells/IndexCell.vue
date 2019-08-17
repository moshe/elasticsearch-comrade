<template>
  <v-layout wrap column class="index-cell">
    <v-flex>
      <v-menu offset-y style="display: inline-block">
        <template v-slot:activator="{ on }">
          <div class="index-name" :data-index-name="indexName" v-on="on">
            {{ indexName }}{{ index.status === "close" ? " (closed)" : "" }}
            <v-icon size="16">arrow_drop_down</v-icon>
          </div>
        </template>
        <v-list dense>
          <v-list-item>
            <v-list-item-title class="success--text text--lighten-2">
              <v-icon
                size="14"
                color="success lighten-2"
                class="pr-2"
                v-text="'build'"
              />
              Actions
            </v-list-item-title>
          </v-list-item>
          <v-divider />

          <list-tile
            :action="() => closeIndex(indexName)"
            title="Close"
            :disabled="isClosed"
          />
          <list-tile
            :action="() => openIndex(indexName)"
            title="Open"
            :disabled="isOpen"
          />
          <list-tile
            :action="() => flushIndex(indexName)"
            title="Flush"
            :disabled="isClosed"
          />
          <list-tile
            :action="() => clearCacheIndex(indexName)"
            title="Clear Cache"
            :disabled="isClosed"
          />
          <list-tile
            :action="() => forceMergeIndex(indexName)"
            title="Force Merge"
            :disabled="isClosed"
          />
          <v-list-item class="success--text pt-2 pb-1">
            <v-list-item-title class="success--text text--lighten-2">
              <v-icon
                size="14"
                color="success lighten-2"
                class="pr-2"
                v-text="'visibility'"
              />
              Inspect
            </v-list-item-title>
          </v-list-item>
          <v-divider />
          <list-tile :action="showMapping" title="Show Mapping" />
          <list-tile :action="showSettings" title="Show Settings" />
          <list-tile :action="showHead" title="Head" :disabled="isClosed" />
          <v-list-item class="success--text pt-2 pb-1">
            <v-list-item-title class="success--text text--lighten-2">
              <v-icon
                size="14"
                color="success lighten-2"
                class="pr-2"
                v-text="'settings'"
              />
              Configure
            </v-list-item-title>
          </v-list-item>
          <v-divider />
          <list-tile
            :action="() => $router.push(`/indexSettings/${indexName}`)"
            title="Edit Settings"
            :disabled="isClosed"
          />
          <v-list-item class="success--text pt-2 pb-1">
            <v-list-item-title class="error--text text--lighten-2">
              <v-icon
                size="14"
                color="error lighten-2"
                class="pr-2"
                v-text="'error_outline'"
              />
              Danger
            </v-list-item-title>
          </v-list-item>
          <v-divider />
          <list-tile
            :action="() => deleteIndex(indexName)"
            title="Delete Index"
          />
        </v-list>
      </v-menu>
    </v-flex>
    <v-flex>
      <v-layout justify-start align-start wrap>
        <v-flex shrink v-for="alias in index.aliases" :key="alias">
          <v-chip
            x-small
            label
            style="margin-right: 6px"
            color="blue-grey lighten-4"
            text-color="grey darken-3"
          >
            <v-icon size="12" class="mr-1" v-text="'bookmark'" />
            {{ alias }}
          </v-chip>
        </v-flex>
      </v-layout>
    </v-flex>

    <v-flex>
      <div v-if="isOpen">
        <v-chip
          color="grey darken-3"
          text-color="white"
          x-small
          label
          style="margin-right: 6px"
        >
          shards: {{ index.primaries }} * {{ index.replicas + 1 }}
        </v-chip>
        <v-chip
          color="grey darken-3"
          text-color="white"
          x-small
          label
          style="margin-right: 6px"
        >
          docs: {{ index.docsCount.toLocaleString() }}
        </v-chip>
        <v-chip color="grey darken-3" text-color="white" x-small label>
          size:{{ index.storeSize }}</v-chip
        >
      </div>
    </v-flex>
    <v-flex style="text-align: left" v-if="index.unassignedShards" class="mt-2">
      <shard-square
        v-for="(shard, index) in index.unassignedShards.replicas"
        :key="index"
        :index="indexName"
        :state="shard.state"
        :id="shard.shard"
        :primary="false"
      />
    </v-flex>
  </v-layout>
</template>

<script>
import indexAPIs from "../../../mixins/indexApis";
import { mapMutations, mapState } from "vuex";
import ListTile from "./ListTile.vue";
import ShardSquare from "../ShardSquare.vue";
export default {
  props: {
    indexName: {
      required: true,
      type: String
    }
  },
  components: { ShardSquare, ListTile },
  mixins: [indexAPIs],
  methods: {
    ...mapMutations(["startJsonModal"]),
    async showMapping() {
      const content = await this.getMapping(this.indexName);
      this.startJsonModal(content);
    },
    async showSettings() {
      const content = await this.getSettings(this.indexName);
      this.startJsonModal(content);
    },
    async showHead() {
      const content = await this.getHead(this.indexName);
      this.startJsonModal(content);
    }
  },
  computed: {
    ...mapState(["indices"]),
    index() {
      return this.indices[this.indexName];
    },
    isOpen() {
      return this.index.status === "open";
    },
    isClosed() {
      return this.index.status === "close";
    }
  }
};
</script>

<style>
.index-cell .v-chip {
  padding: 0 4px;
}
.index-name {
  font-size: 16px;
  cursor: pointer;
  word-wrap: break-word;
  word-break: break-all;
}
</style>

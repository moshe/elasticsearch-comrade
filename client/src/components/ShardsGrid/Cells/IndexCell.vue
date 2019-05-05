<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-layout column fill-height class="index-cell">
    <v-flex grow>
      <v-menu offset-y style="display: inline-block">
        <template v-slot:activator="{ on }">
          <div class="index-name" v-on="on">{{ indexName }}</div>
        </template>
        <v-list dense>
          <list-tile
            :action="() => closeIndex(indexName)"
            icon="close"
            title="Close"
            :disabled="index.status === 'close'"
          />

          <list-tile
            :action="() => openIndex(indexName)"
            icon="loop"
            title="Open"
            :disabled="index.status === 'open'"
          />

          <list-tile
            :action="showMapping"
            icon="view_compact"
            title="Mapping"
          />

          <list-tile :action="showSettings" icon="settings" title="Settings" />

          <list-tile
            :action="showHead"
            icon="visibility"
            title="Head"
            :disabled="index.status !== 'open'"
          />

          <list-tile
            :action="() => flushIndex(indexName)"
            icon="sync"
            title="Flush"
          />

          <list-tile
            :action="() => forceMergeIndex(indexName)"
            icon="call_merge"
            title="Force Merge"
          />
        </v-list>
      </v-menu>
    </v-flex>
    <v-flex shrink>
      <v-layout
        v-if="index.status === 'open'"
        class="index-info"
        justify-space-between
        fill-height
        wrap
      >
        <v-flex shrink>
          <v-chip small label>
            shards: {{ index.primaries }} * {{ index.replicas }}
          </v-chip>
        </v-flex>
        <v-flex shrink>
          <v-chip small label>
            docs: {{ index.docsCount.toLocaleString() }}
          </v-chip>
        </v-flex>
        <v-flex shrink>
          <v-chip small label> size: {{ index.storeSize }} </v-chip>
        </v-flex>
      </v-layout>
    </v-flex>
    <v-flex style="text-align: left" v-if="index.unassignedShards" class="mt-2">
      <shard-square
        v-for="shard in index.unassignedShards.replicas"
        :key="shard.shard"
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
  name: "IndexCell",
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
  props: {
    indexName: {
      required: true,
      type: String
    }
  },
  computed: {
    ...mapState(["indices"]),
    index() {
      return this.indices[this.indexName];
    }
  }
};
</script>

<style>
.index-cell {
  max-width: 15vw;
  user-select: text;
}
.index-name {
  font-size: 14px;
  cursor: pointer;
  text-align: left;
}

.index-cell .v-chip--small {
  font-size: 9px;
  height: 16px !important;
}

.index-cell .v-chip .v-chip__content {
  padding: 0 3px;
}
.index-cell .v-chip {
  margin: 0;
}
</style>

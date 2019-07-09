<template>
  <v-layout wrap column class="index-cell">
    <v-flex>
      <v-menu offset-y style="display: inline-block">
        <template v-slot:activator="{ on }">
          <!-- eslint-disable-next-line prettier/prettier -->
          <div class="index-name" v-on="on">{{ indexName }}{{ index.status === "close" ? " (closed)" : "" }}</div>
        </template>
        <v-list dense>
          <list-tile
            :action="() => closeIndex(indexName)"
            icon="close"
            title="Close"
            :disabled="isClosed"
          />

          <list-tile
            :action="() => openIndex(indexName)"
            icon="loop"
            title="Open"
            :disabled="isOpen"
          />

          <list-tile
            :action="showMapping"
            icon="view_compact"
            title="Show Mapping"
          />

          <list-tile
            :action="showSettings"
            icon="settings"
            title="Show Settings"
          />

          <list-tile
            :action="showHead"
            icon="visibility"
            title="Head"
            :disabled="isClosed"
          />

          <list-tile
            :action="() => flushIndex(indexName)"
            icon="storage"
            title="Flush"
            :disabled="isClosed"
          />

          <list-tile
            :action="() => forceMergeIndex(indexName)"
            icon="call_merge"
            title="Force Merge"
            :disabled="isClosed"
          />

          <list-tile
            :action="() => clearCacheIndex(indexName)"
            icon="sync_disabled"
            title="Clear Cache"
            :disabled="isClosed"
          />

          <list-tile
            :action="() => deleteIndex(indexName)"
            icon="delete"
            title="Delete Index"
            color="red lighten-2"
          />
        </v-list>
      </v-menu>
    </v-flex>
    <v-flex>
      <v-layout justify-start align-start>
        <v-flex v-for="alias in index.aliases" :key="alias" shrink>
          <v-chip
            small
            label
            style="margin-right: 6px"
            color="blue-grey lighten-4"
            text-color="grey darken-3"
          >
            <v-icon size="12" class="mr-1">bookmark</v-icon>
            {{ alias }}
          </v-chip>
        </v-flex>
      </v-layout>
    </v-flex>

    <v-flex>
      <v-layout v-if="isOpen" row>
        <v-flex shrink>
          <v-chip small label style="margin-right: 6px">
            shards: {{ index.primaries }} * {{ index.replicas }}
          </v-chip>
        </v-flex>
        <v-flex shrink>
          <v-chip small label style="margin-right: 6px">
            docs: {{ index.docsCount.toLocaleString() }}
          </v-chip>
        </v-flex>
        <v-flex shrink>
          <v-chip small label> size:{{ index.storeSize }}</v-chip>
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
.index-cell {
  max-width: 15vw;
  min-height: 90px;
  user-select: text;
}
.index-name {
  font-size: 16px;
  cursor: pointer;
  text-align: left;
  word-wrap: break-word;
  white-space: pre-wrap;
  white-space: -o-pre-wrap;
  white-space: -moz-pre-wrap;
  white-space: -pre-wrap;
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

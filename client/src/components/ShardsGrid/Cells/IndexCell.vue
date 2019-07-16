<template>
  <v-layout wrap column class="index-cell">
    <v-flex>
      <v-menu offset-y style="display: inline-block">
        <template v-slot:activator="{ on }">
          <!-- eslint-disable-next-line prettier/prettier -->
          <div class="index-name" v-on="on">{{ indexName }}{{ index.status === "close" ? " (closed)" : "" }}</div>
        </template>
        <v-list dense>
          <v-list-tile class="success--text pt-1">
            <v-list-tile-action style="min-width: 24px" class="pr-2">
              <v-icon size="14">build</v-icon>
            </v-list-tile-action>
            <v-list-tile-title>Actions</v-list-tile-title>
          </v-list-tile>
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
          <v-list-tile class="success--text pt-1">
            <v-list-tile-action style="min-width: 24px" class="pr-2">
              <v-icon size="14">visibility</v-icon>
            </v-list-tile-action>
            <v-list-tile-title>Inspect</v-list-tile-title>
          </v-list-tile>
          <v-divider />
          <list-tile :action="showMapping" title="Show Mapping" />
          <list-tile :action="showSettings" title="Show Settings" />
          <list-tile :action="showHead" title="Head" :disabled="isClosed" />
          <v-list-tile class="success--text pt-1">
            <v-list-tile-action style="min-width: 24px" class="pr-2">
              <v-icon size="14">settings</v-icon>
            </v-list-tile-action>
            <v-list-tile-title>Configure</v-list-tile-title>
          </v-list-tile>
          <v-divider />
          <list-tile
            :action="() => $router.push(`/indexSettings/${indexName}`)"
            title="Edit Settings"
            :disabled="isClosed"
          />
          <v-list-tile class="success--text pt-1">
            <v-list-tile-action style="min-width: 24px" class="pr-2">
              <v-icon size="14">error_outline</v-icon>
            </v-list-tile-action>
            <v-list-tile-title>Danger</v-list-tile-title>
          </v-list-tile>
          <v-divider />
          <list-tile
            :action="() => deleteIndex(indexName)"
            title="Delete Index"
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

.v-list--dense .v-subheader {
  height: 28px !important;
}
</style>

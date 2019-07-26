<template>
  <v-layout wrap column class="index-cell">
    <v-flex>
      <v-menu offset-y style="display: inline-block">
        <template v-slot:activator="{ on }">
          <div class="index-name" v-on="on">
            <v-icon size="14">menu</v-icon> {{ indexName
            }}{{ index.status === "close" ? " (closed)" : "" }}
          </div>
        </template>
        <v-list dense>
          <v-list-item>
            <v-list-item-action>
              <v-icon size="14" color="success lighten-2">build</v-icon>
            </v-list-item-action>
            <v-list-item-title class="success--text text--lighten-2">
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
          <v-list-item class="success--text pt-1">
            <v-list-item-action class="pr-2">
              <v-icon size="14" color="success lighten-2">visibility</v-icon>
            </v-list-item-action>
            <v-list-item-title class="success--text text--lighten-2">
              Inspect
            </v-list-item-title>
          </v-list-item>
          <v-divider />
          <list-tile :action="showMapping" title="Show Mapping" />
          <list-tile :action="showSettings" title="Show Settings" />
          <list-tile :action="showHead" title="Head" :disabled="isClosed" />
          <v-list-item class="success--text pt-1">
            <v-list-item-action class="pr-2">
              <v-icon size="14" color="success lighten-2">settings</v-icon>
            </v-list-item-action>
            <v-list-item-title class="success--text text--lighten-2">
              Configure
            </v-list-item-title>
          </v-list-item>
          <v-divider />
          <list-tile
            :action="() => $router.push(`/indexSettings/${indexName}`)"
            title="Edit Settings"
            :disabled="isClosed"
          />
          <v-list-item class="success--text pt-1">
            <v-list-item-action class="pr-2">
              <v-icon size="14" color="error lighten-2">error_outline</v-icon>
            </v-list-item-action>
            <v-list-item-title class="error--text text--lighten-2">
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
            <v-icon size="12" class="mr-1">bookmark</v-icon>
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
.index-cell .v-chip {
  padding: 0 4px;
}
.index-name {
  font-size: 16px;
  cursor: pointer;
  text-align: left;
  white-space: -moz-pre-wrap; /* Mozilla */
  white-space: -hp-pre-wrap; /* HP printers */
  white-space: -o-pre-wrap; /* Opera 7 */
  white-space: -pre-wrap; /* Opera 4-6 */
  white-space: pre-wrap; /* CSS 2.1 */
  white-space: pre-line; /* CSS 3 (and 2.1 as well, actually) */
  word-wrap: break-word; /* IE */
  word-break: break-all;
}

.v-list-item--dense,
.v-list--dense .v-list-item {
  min-height: 28px;
}
.v-list-item__action:first-child,
.v-list-item__icon:first-child {
  margin-right: 0;
}
</style>

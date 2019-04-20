<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-layout column fill-height class="index-cell">
    <v-flex grow>
      <v-menu offset-y style="display: inline-block">
        <template v-slot:activator="{ on }">
          <div class="index-name" v-on="on">{{ indexName }}</div>
        </template>
        <v-list dense>
          <v-list-tile
            @click="closeIndex(indexName)"
            :disabled="index.status === 'close'"
          >
            <v-list-tile-action style="min-width: unset" class="pr-2">
              <v-icon
                :disabled="index.status === 'open'"
                style="font-size: 16px"
                >close</v-icon
              >
            </v-list-tile-action>
            <v-list-tile-title>Close</v-list-tile-title>
          </v-list-tile>

          <v-list-tile
            @click="openIndex(indexName)"
            :disabled="index.status === 'open'"
          >
            <v-list-tile-action style="min-width: unset" class="pr-2">
              <v-icon
                :disabled="index.status === 'open'"
                style="font-size: 16px"
                >loop</v-icon
              >
            </v-list-tile-action>
            <v-list-tile-title>Open</v-list-tile-title>
          </v-list-tile>

          <v-list-tile @click="showMapping">
            <v-list-tile-action style="min-width: unset" class="pr-2">
              <v-icon style="font-size: 16px">view_compact</v-icon>
            </v-list-tile-action>
            <v-list-tile-title>Mapping</v-list-tile-title>
          </v-list-tile>

          <v-list-tile @click="showSettings">
            <v-list-tile-action style="min-width: unset" class="pr-2">
              <v-icon style="font-size: 16px">settings</v-icon>
            </v-list-tile-action>
            <v-list-tile-title>Settings</v-list-tile-title>
          </v-list-tile>

          <v-list-tile @click="showHead">
            <v-list-tile-action style="min-width: unset" class="pr-2">
              <v-icon style="font-size: 16px">visibility</v-icon>
            </v-list-tile-action>
            <v-list-tile-title>Head</v-list-tile-title>
          </v-list-tile>
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
  </v-layout>
</template>

<script>
import indexAPIs from "../../../mixins/indexApis";
import { mapMutations, mapState } from "vuex";
export default {
  name: "IndexCell",
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

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
              <v-icon style="font-size: 16px">close</v-icon>
            </v-list-tile-action>
            <v-list-tile-title>Close index</v-list-tile-title>
          </v-list-tile>

          <v-list-tile
            @click="openIndex(indexName)"
            :disabled="index.status === 'open'"
          >
            <v-list-tile-action style="min-width: unset" class="pr-2">
              <v-icon style="font-size: 16px">loop</v-icon>
            </v-list-tile-action>
            <v-list-tile-title>Reopen index</v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-menu>
    </v-flex>
    <v-flex shrink>
      <!--      eslint-disable-next-line -->
      <div v-if="index.status === 'open'" class="index-info">shards {{index.primaries}} * {{index.replicas}} | docs: {{index.docsCount.toLocaleString()}} | size: {{index.storeSize}}</div>
    </v-flex>
  </v-layout>
</template>

<script>
import indexAPIs from "../../../mixins/indexApis";
import { mapState } from "vuex";
export default {
  name: "IndexCell",
  mixins: [indexAPIs],
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

<style scoped>
.index-cell {
  text-align: left;
  height: 80px;
}
.index-name {
  font-size: 14px;
  cursor: pointer;
}
.index-info {
  max-width: 13vw;
  white-space: pre-wrap;
  font-size: 11px;
}
</style>

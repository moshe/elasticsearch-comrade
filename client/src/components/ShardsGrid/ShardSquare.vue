<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-menu offset-y style="display: inline-block">
    <template v-slot:activator="{ on }">
      <div style="display: inline-block; margin-right: 3px; height: 25px">
        <div
          class="shard-square"
          v-bind:class="{
            'primary-shard': primary,
            'replica-shard': !primary,
            marked: isMarkedForRelocation
          }"
          v-on="on"
        >
          {{ id }}
        </div>
        <v-progress-linear
          height="2px"
          v-model="progress"
          class="ma-0"
          color="white"
          style="width: 20px;"
          v-if="progress != null"
        />
      </div>
    </template>
    <v-list dense>
      <v-list-tile
        :disabled="isRelocating"
        @click="toggleShardForRelocation({ index, id, nodeName })"
      >
        <v-list-tile-action style="min-width: unset" class="pr-2">
          <v-icon :disabled="isRelocating" style="font-size: 16px">input</v-icon>
        </v-list-tile-action>
        <v-list-tile-title v-if="isMarkedForRelocation">
          Deselect for relocation
        </v-list-tile-title>
        <v-list-tile-title v-else>Select for relocation</v-list-tile-title>
      </v-list-tile>

      <v-list-tile>
        <v-list-tile-action style="min-width: unset" class="pr-2">
          <v-icon style="font-size: 16px">trending_up</v-icon>
        </v-list-tile-action>
        <v-list-tile-title>Show stats</v-list-tile-title>
      </v-list-tile>
    </v-list>
  </v-menu>
</template>

<script>
import store from "../../store";
import { mapMutations } from "vuex";

export default {
  name: "ShardSquare",
  props: {
    id: {
      required: true,
      type: Number
    },
    index: {
      required: true,
      type: String
    },
    nodeName: {
      required: true,
      type: String
    },
    state: {
      required: true,
      type: String
    },
    primary: {
      required: true,
      type: Boolean
    },
    progress: {
      required: false,
      type: Number
    }
  },
  methods: {
    ...mapMutations(["toggleShardForRelocation"])
  },
  computed: {
    isMarkedForRelocation() {
      for (const mark of store.state.shardsMarkedForRelocation) {
        if (
          mark.index === this.index &&
          mark.nodeName === this.nodeName &&
          mark.id === this.id
        ) {
          return true;
        }
      }
      return false;
    },
    isRelocating() {
      return this.state === "RELOCATING";
    }
  }
};
</script>

<style>
.shard-square {
  display: inline-block;
  height: 20px;
  width: 20px;
  text-align: center;
  cursor: pointer;
}

.primary-shard {
  background-color: #72a164;
  border: 1px solid #4e6e44;
}

.replica-shard {
  background-color: rgba(60, 83, 54, 0.67);
  border: 1px solid rgba(54, 75, 49, 0.67);
}

.marked {
  border-style: dashed;
  border-color: white;
}

.v-list--dense .v-list__tile:not(.v-list__tile--avatar) {
  height: unset;
}
.v-progress-linear {
  overflow: unset;
}
</style>

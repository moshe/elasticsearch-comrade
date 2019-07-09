<template>
  <v-menu offset-y style="display: inline-block" :disabled="isUnassigned">
    <template v-slot:activator="{ on }">
      <div style="display: inline-block; margin-right: 3px; height: 25px">
        <div
          class="shard-square"
          v-bind:class="{
            'primary-shard': primary,
            'replica-shard': !primary,
            'initializing-shard': isInitializing,
            'unassigned-shard': isUnassigned,
            marked: isMarkedForRelocation
          }"
          v-on="on"
        >
          {{ id }}
        </div>
        <v-progress-linear
          height="3px"
          v-model="progress"
          class="ma-0"
          color="white"
          style="width: 20px"
          v-if="progress != null"
        />
      </div>
    </template>
    <v-list dense>
      <v-list-tile disabled v-if="isRelocating">
        <v-list-tile-action style="min-width: unset" class="pr-2">
          <v-icon style="font-size: 16px" disabled>computer</v-icon>
        </v-list-tile-action>
        <v-list-tile-action> From {{ fromNode }} </v-list-tile-action>
      </v-list-tile>
      <v-list-tile
        :disabled="isRelocating"
        @click="toggleShardForRelocation({ index, id, nodeName })"
      >
        <v-list-tile-action style="min-width: unset" class="pr-2">
          <v-icon :disabled="isRelocating" style="font-size: 16px">
            input
          </v-icon>
        </v-list-tile-action>
        <v-list-tile-title v-if="isMarkedForRelocation">
          Deselect for relocation
        </v-list-tile-title>
        <v-list-tile-title v-else>Select for relocation</v-list-tile-title>
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
      required: false,
      type: String
    },
    state: {
      required: true,
      type: String
    },
    fromNode: {
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
    },
    isUnassigned() {
      return this.state === "UNASSIGNED";
    },
    isInitializing() {
      return this.state === "INITIALIZING";
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
  background-color: #43a047;
  border: 1px solid #43a047;
  color: white;
}

.replica-shard {
  background-color: #38524f;
  border: 1px solid #38524f;
  color: lightgray;
}

.marked {
  border-style: dashed;
  border-color: white;
}

.initializing-shard {
  background-color: #f57f17;
  border-color: #f57f17;
}

.unassigned-shard {
  background-color: gray;
  border-color: gray;
  cursor: unset;
}

.v-list--dense .v-list__tile:not(.v-list__tile--avatar) {
  height: unset;
}
.v-progress-linear {
  overflow: unset;
}
</style>

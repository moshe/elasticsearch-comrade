<template>
  <div style="display: inline-block; margin-right: 3px; height: 25px">
    <div
      class="shard-square"
      :data-index="index"
      :data-shard="id"
      :data-node="nodeName"
      v-bind:class="{
        'primary-shard': primary,
        'replica-shard': !primary,
        'initializing-shard': isInitializing,
        'unassigned-shard': isUnassigned,
        marked: isMarkedForRelocation
      }"
      @click="toggle({ index, id, nodeName })"
    >
      {{ id }}
    </div>
    <v-progress-linear
      height="3px"
      v-model="progress"
      color="white"
      v-if="progress != null"
    />
  </div>
</template>

<script>
import store from "../../store";
import { mapMutations } from "vuex";

export default {
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
      default: false,
      type: Boolean
    },
    progress: {
      required: false,
      type: Number
    }
  },
  methods: {
    ...mapMutations(["toggleShardForRelocation"]),
    toggle(args) {
      if (this.isRelocating || this.isInitializing) {
        return;
      }
      this.toggleShardForRelocation(args);
    }
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
  line-height: 19px;
  width: 20px;
  text-align: center;
  cursor: pointer;
  font-size: 14px;
}

.primary-shard {
  background-color: #43a047;
  border: 1px solid #43a047;
  color: white;
}

.replica-shard {
  background-color: rgba(67, 160, 71, 0.3);
  border: 1px solid rgba(67, 160, 71, 0.1);
  color: rgba(255, 255, 255, 0.5);
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

.shard-list .v-list-item {
  min-height: 0;
  height: 24px;
}
</style>

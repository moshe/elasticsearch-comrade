<template>
  <div>
    <v-header sub>Manage Aliases</v-header>
    <v-text-field solo label="Filter Aliases / Indices" v-model="filter" />
    <div v-for="index in indicesWithAlias" :key="index">
      <div style="font-size:15px">
        <v-btn icon x-small @click="handleRemoveIndex(index)">
          <v-icon size="18">clear</v-icon>
        </v-btn>
        {{ index }}
      </div>
      <span class="pl-8" />
      <alias-chip
        v-for="alias in indices[index].aliases"
        :key="alias"
        :alias="alias"
        :removed="isRemoved(index, alias)"
        @remove="handleRemove(index, alias)"
        class="ma-1"
      />
      <alias-chip
        v-for="(action, i) in added.filter(x => x.index === index)"
        :key="i"
        :alias="action.alias"
        added
        @remove="handleRemove(action.index, action.alias)"
        class="ma-1"
      />
      <v-menu offset-y>
        <template v-slot:activator="{ on }">
          <v-btn small icon color="orange" v-on="on">
            <v-icon>add</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item
            v-for="alias in aliases"
            :key="alias"
            @click="handleAddition(index, alias)"
          >
            <v-list-item-title>{{ alias }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
      <v-divider class="mb-1 mt-1" />
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import AliasChip from "./AliasChip.vue";
import VHeader from "../Base/Header.vue";

export default {
  components: { AliasChip, VHeader },
  data() {
    return { filter: "" };
  },
  props: {
    pendingActions: {
      type: Array
    }
  },
  computed: {
    ...mapState(["indices"]),
    removed() {
      return this.pendingActions.filter(x => x.action === "remove");
    },
    added() {
      return this.pendingActions.filter(x => x.action === "add");
    },
    aliases() {
      return [...new Set(Object.values(this.indices).flatMap(x => x.aliases))];
    },
    indicesWithAlias() {
      return Object.keys(this.indices).filter(
        index =>
          index.includes(this.filter || "") &&
          (this.indices[index].aliases.length > 0 ||
            this.added.filter(x => x.index === index).length)
      );
    }
  },
  methods: {
    isRemoved(index, alias) {
      return (
        this.removed.filter(x => x.index === index && x.alias === alias)
          .length === 1
      );
    },
    isAdded(index, alias) {
      return (
        this.added.filter(x => x.index === index && x.alias === alias)
          .length === 1
      );
    },
    handleRemove(index, alias) {
      this.$emit("action", { index, alias, action: "remove" });
    },
    handleRemoveIndex(index) {
      this.indices[index].aliases.forEach(x => this.handleRemove(index, x));
    },
    handleAddition(index, alias) {
      this.$emit("action", { index, alias, action: "add" });
    }
  }
};
</script>

<style scoped></style>

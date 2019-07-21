<template>
  <div>
    <v-flex><v-header sub>Manage Aliases</v-header></v-flex>
    <v-text-field solo label="Filter Aliases / Indices"></v-text-field>
    <div v-for="index in Object.keys(indices)" :key="index">
      <div
        v-if="
          indices[index].aliases || added.filter(x => x.index === index).length
        "
      >
        <div style="font-size:15px">
          <v-btn flat icon small class="ma-0" @click="handleRemoveIndex(index)">
            <v-icon size="18">clear</v-icon>
          </v-btn>
          {{ index }}
        </div>
        <div style="display: inline-block">
          <alias-chip
            v-for="alias in indices[index].aliases"
            :key="alias"
            :alias="alias"
            :removed="isRemoved(index, alias)"
            @remove="handleRemove(index, alias)"
          />
          <alias-chip
            v-for="(action, i) in added.filter(x => x.index === index)"
            :key="i"
            :alias="action.alias"
            added
            @remove="handleRemove(action.index, action.alias)"
          />
        </div>
        <div style="display: inline-block">
          <v-menu offset-y>
            <template v-slot:activator="{ on }">
              <v-btn flat icon color="orange" class="ma-0" v-on="on">
                <v-icon>add</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-tile
                v-for="alias in aliases"
                :key="alias"
                @click="handleAddition(index, alias)"
              >
                <v-list-tile-title>{{ alias }}</v-list-tile-title>
              </v-list-tile>
            </v-list>
          </v-menu>
        </div>
        <v-divider class="mb-1 mt-1" />
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import AliasChip from "./AliasChip.vue";
import VHeader from "../Base/Header.vue";

export default {
  components: { AliasChip, VHeader },
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

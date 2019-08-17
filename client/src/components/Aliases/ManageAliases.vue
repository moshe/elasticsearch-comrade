<template>
  <div>
    <v-header sub>Manage Aliases</v-header>
    <v-text-field solo label="Filter Aliases / Indices" v-model="filter" />
    <div v-for="alias in aliases" :key="alias">
      <div style="font-size:15px">
        <v-icon size="18" class="mr-1" v-text="'bookmark'" />
        {{ alias }}
        <v-btn icon x-small @click="handleRemoveIndex(alias)">
          <v-icon size="18" v-text="'clear'" />
        </v-btn>
      </div>
      <div class="pl-6">
        <alias-chip
          v-for="index in aliasToindex[alias] || []"
          :key="index"
          :alias="index"
          :removed="isRemoved(index, alias)"
          @remove="handleRemove(index, alias)"
          class="ma-1"
        />
        <alias-chip
          v-for="(action, i) in added.filter(x => x.alias === alias)"
          :key="i"
          :alias="action.index"
          added
          @remove="handleRemove(action.index, action.alias)"
          class="ma-1"
        />
        <v-menu offset-y>
          <template v-slot:activator="{ on }">
            <v-btn
              small
              icon
              :color="`primary ${$vuetify.theme.dark ? 'lighten' : 'darken'}-1`"
              v-on="on"
            >
              <v-icon v-text="'add'" />
            </v-btn>
          </template>
          <v-list>
            <v-list-item
              v-for="index in Object.keys(indices)"
              :key="index"
              @click="handleAddition(index, alias)"
            >
              <v-list-item-title v-text="index" />
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
      <v-divider class="mb-4 mt-4" />
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
    },
    aliasToindex: {
      type: Object
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
      return Object.keys(this.aliasToindex);
    }
  },
  methods: {
    isRemoved(index, alias) {
      return (
        this.removed.filter(x => x.index === index && x.alias === alias)
          .length === 1
      );
    },
    handleRemove(index, alias) {
      this.$emit("action", { index, alias, action: "remove" });
    },
    handleRemoveIndex(alias) {
      this.aliasToindex[alias].forEach(index =>
        this.handleRemove(index, alias)
      );
    },
    handleAddition(index, alias) {
      this.$emit("action", { index, alias, action: "add" });
    }
  }
};
</script>

<style scoped></style>

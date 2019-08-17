<template>
  <v-layout row>
    <v-flex class="pr-4" xs7>
      <create-alias @action="onAction" :pending-actions="pendingActions" />
    </v-flex>
    <v-flex xs5 class="pl-4">
      <manage-aliases
        @action="onAction"
        :pending-actions="pendingActions"
        :aliasToindex="aliasToindex"
      />
      <pending-actions
        :pending-actions="pendingActions"
        @removeAction="removeAction"
      />
      <v-btn
        color="success"
        class="mt-4"
        :disabled="pendingActions.length == 0"
        @click="commit"
      >
        Commit
      </v-btn>
    </v-flex>
  </v-layout>
</template>

<script>
import CreateAlias from "../components/Aliases/CreateAlias.vue";
import ManageAliases from "../components/Aliases/ManageAliases.vue";
import PendingActions from "../components/Aliases/PendingActions.vue";
import aliasApis from "../mixins/aliasApis";
import { mapState } from "vuex";
export default {
  components: { CreateAlias, ManageAliases, PendingActions },
  mixins: [aliasApis],
  created() {
    this.getAliases();
  },
  data() {
    return { pendingActions: [], aliasToindex: {} };
  },
  computed: {
    ...mapState(["indices"])
  },
  methods: {
    async commit() {
      this.$store.commit("startLoading");
      await this.updateAliases(this.pendingActions);
      await this.getAliases();
      this.pendingActions = [];
      this.$store.commit("stopLoading");
    },
    async getAliases() {
      this.$store.commit("startLoading");
      this.aliasToindex = await this.listAliases();
      this.$store.commit("stopLoading");
    },
    onAction(action) {
      this.removeAction(action);
      if (
        action.action === "add" &&
        this.indices[action.index].aliases.filter(x => x === action.alias)
          .length === 1
      ) {
        return;
      }
      if (
        action.action === "remove" &&
        this.indices[action.index].aliases.filter(x => x === action.alias)
          .length === 0
      ) {
        return;
      }
      this.pendingActions.push(action);
    },
    removeAction(action) {
      this.pendingActions = this.pendingActions.filter(
        x => !(x.index === action.index && x.alias === action.alias)
      );
    }
  }
};
</script>

<style scoped></style>

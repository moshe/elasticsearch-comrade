<template>
  <v-layout row>
    <v-flex class="mr-5" xs7>
      <create-alias @action="onAction" :pending-actions="pendingActions" />
    </v-flex>
    <v-flex xs5>
      <manage-aliases @action="onAction" :pending-actions="pendingActions" />
      <pending-actions
        :pending-actions="pendingActions"
        @removeAction="removeAction"
      />
      <v-btn
        color="success"
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
  data() {
    return {
      pendingActions: []
    };
  },
  computed: {
    ...mapState(["indices"])
  },
  methods: {
    async commit() {
      await this.updateAliases(this.pendingActions);
      this.pendingActions = [];
    },
    onAction(action) {
      this.removeAction(action);
      if (
        action.action === "add" &&
        (this.indices[action.index].aliases || []).filter(
          x => x === action.alias
        ).length === 1
      ) {
        return;
      }
      if (
        action.action === "remove" &&
        (this.indices[action.index].aliases || []).filter(
          x => x === action.alias
        ).length === 0
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

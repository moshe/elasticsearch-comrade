<template>
  <v-layout row>
    <v-flex style="margin-right: 20px" xs8>
      <create-alias @action="onAction" :pending-actions="pendingActions" />
    </v-flex>
    <v-flex xs4>
      <manage-aliases @action="onAction" :pending-actions="pendingActions" />
      <pending-actions
        :pending-actions="pendingActions"
        @removeAction="removeAction"
      />
    </v-flex>
  </v-layout>
</template>

<script>
import CreateAlias from "../components/Aliases/CreateAlias.vue";
import ManageAliases from "../components/Aliases/ManageAliases.vue";
import PendingActions from "../components/Aliases/PendingActions.vue";
import { mapState } from "vuex";
export default {
  components: { CreateAlias, ManageAliases, PendingActions },
  data() {
    return {
      pendingActions: []
    };
  },
  computed: {
    ...mapState(["indices"])
  },
  methods: {
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

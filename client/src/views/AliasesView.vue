<template>
  <v-layout row wrap>
    <v-flex style="margin-right: 20px" xs8>
      <create-alias @action="onAction" />
    </v-flex>
    <v-flex>
      <manage-aliases @action="onAction" />
      <pending-actions :actions="pendingActions" />
    </v-flex>
  </v-layout>
</template>

<script>
import CreateAlias from "../components/Aliases/CreateAlias.vue";
import ManageAliases from "../components/Aliases/ManageAliases.vue";
import PendingActions from "../components/Aliases/PendingActions.vue";
export default {
  components: { CreateAlias, ManageAliases, PendingActions },
  data() {
    return {
      pendingActions: []
    };
  },
  methods: {
    onAction(action) {
      this.pendingActions = this.pendingActions.filter(
        x => !(x.index === action.index && x.alias === action.alias)
      );
      this.pendingActions.push(action);
    }
  }
};
</script>

<style scoped></style>

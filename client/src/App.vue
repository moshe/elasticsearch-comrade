<template>
  <v-app dark>
    <json-modal />
    <v-navigation-drawer v-model="drawer" absolute temporary>
      <drawer-content />
    </v-navigation-drawer>
    <v-toolbar app>
      <v-toolbar-side-icon @click="drawer = true" />
      <v-toolbar-title class="headline text-uppercase">
        <status-dot />
        <span @click="$router.push('/')" style="cursor: pointer">
          <span class="font-weight-bold">Elasticsearch</span>
          <span class="font-weight-light">ops</span>
        </span>
      </v-toolbar-title>
      <v-spacer />
      <refresh-selector />
    </v-toolbar>

    <v-content>
      <v-dialog v-model="loading" persistent width="500">
        <v-card>
          <v-card-text>
            <v-progress-linear indeterminate color="green" class="mb-0" />
          </v-card-text>
        </v-card>
      </v-dialog>
      <v-container fluid>
        <router-view />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { mapActions, mapState } from "vuex";
import StatusDot from "./components/StatusDot.vue";
import JsonModal from "./components/Modals/JsonModal.vue";
import DrawerContent from "./components/Navigation/DrawerContent.vue";
import RefreshSelector from "./components/RefreshSelector.vue";

export default {
  name: "App",
  components: {
    DrawerContent,
    JsonModal,
    StatusDot,
    RefreshSelector
  },
  async created() {
    await this.updateData();
  },
  data() {
    return {
      drawer: null
    };
  },
  methods: {
    ...mapActions(["shardsGrid"]),
    async updateData() {
      if (this.settingsRefreshEnabled) {
        await this.shardsGrid();
      }
      setTimeout(this.updateData, this.settingsRefreshEvery);
    }
  },
  computed: {
    ...mapState(["loading", "settingsRefreshEvery", "settingsRefreshEnabled"])
  }
};
</script>

<style scoped></style>

<template>
  <v-app dark>
    <json-modal />
    <error-bar />
    <v-navigation-drawer v-model="drawer" absolute temporary>
      <drawer-content />
    </v-navigation-drawer>
    <v-toolbar app v-if="connectedCluster">
      <v-toolbar-side-icon @click="drawer = true" />
      <v-toolbar-title class="headline text-uppercase">
        <status-dot :status="this.cluster.clusterStatus" class="mr-3" />
        <span @click="$router.push('/')" style="cursor: pointer">
          <span class="font-weight-bold">Elasticsearch</span>
          <span class="font-weight-light">ops</span>
        </span>
      </v-toolbar-title>
      <v-spacer />
      <refresh-selector />
      <v-btn icon flat @click="selectCluster(null)">
        <v-icon>logout</v-icon>
      </v-btn>
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
        <router-view v-if="connectedCluster" />
        <login v-else />
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { mapActions, mapState, mapMutations } from "vuex";
import StatusDot from "./components/StatusDot.vue";
import JsonModal from "./components/Modals/JsonModal.vue";
import ErrorBar from "./components/Modals/ErrorBar.vue";
import DrawerContent from "./components/Navigation/DrawerContent.vue";
import RefreshSelector from "./components/RefreshSelector.vue";
import Login from "./components/Login/Login.vue";

export default {
  name: "App",
  components: {
    DrawerContent,
    JsonModal,
    StatusDot,
    RefreshSelector,
    Login,
    ErrorBar
  },
  async created() {
    await this.updateData();
  },
  data() {
    return {
      drawer: null,
      timer: setTimeout(() => {}, 0)
    };
  },
  methods: {
    ...mapActions(["shardsGrid"]),
    ...mapMutations(["selectCluster", "startLoading"]),
    async updateData() {
      if (this.settingsRefreshEnabled && this.connectedCluster) {
        await this.shardsGrid();
      }
      this.timer = setTimeout(this.updateData, this.settingsRefreshEvery);
    }
  },
  watch: {
    connectedCluster(newValue) {
      clearTimeout(this.timer);
      if (newValue) {
        this.startLoading();
        this.updateData();
      }
    }
  },
  computed: {
    ...mapState([
      "connectedCluster",
      "cluster",
      "loading",
      "settingsRefreshEvery",
      "settingsRefreshEnabled"
    ])
  }
};
</script>

<style scoped></style>

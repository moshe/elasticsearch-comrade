<template>
  <v-app>
    <json-modal />
    <error-bar />
    <v-navigation-drawer v-model="drawer" app class="accent" temporary>
      <drawer-content />
      <template v-slot:append>
        <div class="pa-2">
          <v-btn
            block
            @click="
              selectCluster(null);
              drawer = false;
            "
          >
            Logout
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>
    <v-app-bar app v-if="connectedCluster">
      <v-app-bar-nav-icon @click="drawer = true" />
      <v-toolbar-title class="headline text-uppercase">
        <status-dot :status="this.cluster.clusterStatus" class="mr-4" />
        <span @click="$router.push('/')" style="cursor: pointer">
          <span class="font-weight-light">Elasticsearch</span>
          <span class="font-weight-bold">Comrade</span>
        </span>
      </v-toolbar-title>
      <v-spacer />
      <refresh-selector />
    </v-app-bar>

    <v-content>
      <v-dialog v-model="loading" persistent width="500">
        <v-card>
          <v-card-text>
            <v-progress-linear indeterminate color="green" class="mb-0" />
          </v-card-text>
        </v-card>
      </v-dialog>
      <v-container fluid class="pl-10 pr-10">
        <v-switch
          label="Dark"
          v-model="$vuetify.theme.dark"
          style="display: inline-block"
          class="mr-4"
        />
        <!-- <v-btn
          :color="color"
          v-for="color in [
            'primary',
            'secondary',
            'accent',
            'info',
            'warning',
            'error',
            'success'
          ]"
          :key="color"
        >
          {{ color }}
        </v-btn> -->
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

<style></style>

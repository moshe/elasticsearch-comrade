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
      <span>
        <v-select
          dense
          v-model="refreshEvery"
          @change="setRefreshEvery"
          :items="times"
          item-text="text"
          item-value="value"
          label="Refresh Every"
        ></v-select>
      </span>
    </v-toolbar>

    <v-content>
      <v-dialog v-model="loading" hide-overlay persistent width="300">
        <v-card>
          <v-card-text>
            <v-progress-linear indeterminate color="white" class="mb-0" />
          </v-card-text>
        </v-card>
      </v-dialog>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
import { mapActions, mapMutations, mapState } from "vuex";
import StatusDot from "./components/StatusDot.vue";
import JsonModal from "./components/Modals/JsonModal.vue";
import DrawerContent from "./components/Navigation/DrawerContent.vue";

export default {
  name: "App",
  components: {
    DrawerContent,
    JsonModal,
    StatusDot
  },
  async created() {
    await this.updateData();
  },
  data() {
    return {
      drawer: null,
      times: [1, 5, 10, 30, 60].map(value => {
        return {
          value: value * 1000,
          text: `${value} second${value > 1 ? "s" : ""}`
        };
      }),
      refreshEvery: 5000
    };
  },
  methods: {
    ...mapMutations(["setRefreshEvery"]),
    ...mapActions(["shardsGrid"]),
    async updateData() {
      await this.shardsGrid();
      setTimeout(this.updateData, this.settingsRefreshEvery);
    }
  },
  computed: {
    ...mapState(["loading", "settingsRefreshEvery"])
  }
};
</script>

<style scoped></style>

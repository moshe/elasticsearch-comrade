<template>
  <v-app dark>
    <v-toolbar app>
      <v-toolbar-title class="headline text-uppercase">
        <status-dot />
        <span class="font-weight-bold">Elasticsearch</span>
        <span class="font-weight-light">ops</span>
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
      <HelloWorld />
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from "./components/HelloWorld";

import { mapMutations, mapState } from "vuex";
import StatusDot from "./components/StatusDot";

export default {
  name: "App",
  components: {
    StatusDot,
    HelloWorld
  },
  data() {
    return {
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
    ...mapMutations(["setRefreshEvery"])
  },
  computed: {
    ...mapState(["loading"])
  }
};
</script>

<style scoped></style>

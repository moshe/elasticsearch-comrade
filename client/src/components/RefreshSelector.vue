<template>
  <span>
    <v-btn
      icon
      text
      style="display:inline-block"
      @click="setRefreshEnabled(!settingsRefreshEnabled)"
    >
      <v-icon>{{ settingsRefreshEnabled ? "stop" : "play_arrow" }}</v-icon>
    </v-btn>
    <v-select
      style="display:inline-block; width: 200px"
      :value="{ value: settingsRefreshEvery }"
      @change="setRefreshEvery"
      :items="times"
      item-text="text"
      item-value="value"
      label="Refresh Every"
    />
  </span>
</template>

<script>
import { mapMutations, mapState } from "vuex";
export default {
  data() {
    return {
      times: [1, 5, 10, 30, 60].map(value => {
        return {
          value: value * 1000,
          text: `${value} second${value > 1 ? "s" : ""}`
        };
      })
    };
  },
  methods: {
    ...mapMutations(["setRefreshEvery", "setRefreshEnabled"])
  },
  computed: {
    ...mapState(["settingsRefreshEvery", "settingsRefreshEnabled"])
  }
};
</script>

<style scoped></style>

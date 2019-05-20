<template>
  <div class="text-sm-center">
    <div>{{ name }} ({{ metric }}%)</div>
    <v-sparkline
      :value="histogram"
      :line-width="6"
      :height="100"
      :gradient="outH"
      color="light-green darken-1"
    />
    <v-progress-linear
      height="2"
      v-model="metric"
      class="ma-0"
      :color="color"
    />
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "NodeStatBar",
  props: {
    name: {
      type: String,
      required: true
    },
    metric: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      histogram: [0, 0],
      gradient: []
    };
  },
  methods: {
    measure() {
      if (this.settingsRefreshEnabled) {
        this.histogram.push(this.metric);
        this.gradient.push(this.color);
      }
      if (
        this.histogram.length === 3 &&
        this.histogram[0] === 0 &&
        this.histogram.length < 4
      ) {
        this.histogram.shift();
      }
      if (this.histogram.length > 20) {
        this.histogram.shift();
        this.gradient.shift();
      }
      setTimeout(this.measure, this.settingsRefreshEvery);
    }
  },
  created() {
    setTimeout(this.measure, this.settingsRefreshEvery);
  },
  computed: {
    ...mapState(["settingsRefreshEvery", "settingsRefreshEnabled"]),
    outH() {
      return this.gradient.reduceRight((a, c) => (a.push(c), a), []);
    },
    color() {
      if (this.metric < 60) {
        return "#7CB342";
      }
      if (this.metric < 80) {
        return "#558B2F";
      }
      if (this.metric < 90) {
        return "#EF5350";
      }
      return "#B71C1C";
    }
  }
};
</script>

<style scoped></style>

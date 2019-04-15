<template>
  <div class="text-sm-center">
    <div>{{ name }}</div>
    <div>{{ metric.toFixed(1) }}%</div>
    <v-sparkline :value="histogram" :line-width="6" :height="100"></v-sparkline>
    <v-progress-linear
      height="2"
      v-model="metric"
      class="ma-0"
      :color="color"
    />
  </div>
</template>

<script>
import {mapState} from "vuex";

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
      histogram: [0, 0, 0]
    };
  },
  methods: {
    measure() {
      this.histogram.push(this.metric);
      if (this.histogram.length > 20) {
        this.histogram.shift();
      }
    }
  },
  created() {
    setInterval(this.measure, this.settingsRefreshEvery);
  },
  computed: {
    ...mapState(["settingsRefreshEvery"]),
    color() {
      if (this.metric < 60) {
        return "light-green darken-1";
      }
      if (this.metric < 80) {
        return "light-green darken-3";
      }
      if (this.metric < 90) {
        return "red lighten-1 ";
      }
      return "red darken-4";
    }
  }
};
</script>

<style scoped></style>

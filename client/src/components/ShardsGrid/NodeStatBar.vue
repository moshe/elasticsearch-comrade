<template>
  <div class="text-sm-center">
    <div>{{ name }}</div>
    <div>{{ metric }}%</div>
    <v-progress-linear
      height="2"
      v-model="metric"
      class="ma-0"
      :color="color"
    />
  </div>
</template>

<script>
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
  computed: {
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

<template>
  <v-layout wrap>
    <v-flex v-for="cluster in clusters" :key="cluster.name" xs12 md6 lg4>
      <login-box :cluster-name="cluster.name" />
    </v-flex>
  </v-layout>
</template>

<script>
import { GET } from "../../requests";
import LoginBox from "./LoginBox.vue";

export default {
  components: { LoginBox },
  async created() {
    this.clusters = await GET("/api/v1/clients");
  },
  data() {
    return { clusters: [] };
  }
};
</script>

<style scoped></style>

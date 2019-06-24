<template>
  <v-dialog v-model="jsonModalContent" width="50%">
    <code style="width: 100%">{{ jsonModalContent }}</code>
  </v-dialog>
</template>

<script>
import { mapState } from "vuex";

export default {
  computed: { ...mapState(["jsonModalContent"]) }
};
</script>

<style scoped></style>

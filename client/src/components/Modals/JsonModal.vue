<template>
  <div>
    <v-dialog v-model="jsonModalContent" width="50%">
      <code style="width: 100%">
        {{ jsonModalContent }}
      </code>
    </v-dialog>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "JsonModal",
  computed: {
    ...mapState(["jsonModalContent"])
  }
};
</script>

<style scoped></style>

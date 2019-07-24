<template>
  <v-snackbar
    top
    right
    v-model="visible"
    color="error"
    vertical
    :timeout="30000"
  >
    <div>
      <span style="font-size: 18px">
        {{ errorBarContent.type }}
      </span>
      <code>
        {{ errorBarContent.body }}
      </code>
    </div>
    <v-btn dark text @click="clearErrorBarContent">
      Close
    </v-btn>
  </v-snackbar>
</template>

<script>
import { mapState, mapMutations } from "vuex";
export default {
  computed: {
    ...mapState(["errorBarContent"]),
    visible: {
      get: function() {
        return this.errorBarContent.type;
      },
      set: function(value) {
        if (!value) {
          this.clearErrorBarContent();
        }
      }
    }
  },
  methods: {
    ...mapMutations(["clearErrorBarContent"])
  },
  data() {
    return { show: true };
  }
};
</script>

<style scoped></style>

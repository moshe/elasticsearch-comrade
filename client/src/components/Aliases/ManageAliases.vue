<template>
  <div>
    <v-flex>
      <div style="font-size: 25px" class="mb-2">
        Manage Aliases
      </div>
    </v-flex>
    <v-text-field solo label="Filter Aliases / Indices"></v-text-field>
    <div v-for="index in Object.keys(indices)" :key="index">
      <div v-if="indices[index].aliases">
        <div style="font-size:15px">
          {{ index }}
        </div>
        <v-chip
          v-for="alias in indices[index].aliases"
          :key="alias"
          close
          color="teal"
          label
          outline
          small
          @input="handleRemove(index, alias)"
        >
          {{ alias }}
        </v-chip>
        <v-btn flat icon color="teal">
          <v-icon>add</v-icon>
        </v-btn>
        <v-divider class="mb-1 mt-1"></v-divider>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState(["indices"])
  },
  methods: {
    handleRemove(index, alias) {
      this.$emit("action", { index, alias, action: "remove" });
    }
  }
};
</script>

<style lang="scss" scoped></style>

<template>
  <div>
    <v-btn
      flat
      icon
      @click="toggle('editor')"
      v-if="!(show.length === 1 && show[0] === 'editor')"
    >
      <v-icon v-if="show.length === 1 && show[0] === 'preview'"
        >arrow_forward_ios</v-icon
      >
      <v-icon v-else>arrow_back_ios</v-icon>
    </v-btn>
    <div />
    <v-btn
      flat
      icon
      @click="toggle('preview')"
      v-if="!(show.length === 1 && show[0] === 'preview')"
    >
      <v-icon v-if="show.length === 1 && show[0] === 'editor'"
        >arrow_back_ios</v-icon
      >
      <v-icon v-else>arrow_forward_ios</v-icon>
    </v-btn>
  </div>
</template>

<script>
export default {
  name: "TerminalButtons",
  props: {
    panes: {
      type: Array
    }
  },
  data() {
    return {
      show: ["preview", "editor"]
    };
  },
  methods: {
    toggle(pan) {
      if (this.show.includes(pan)) {
        this.show = this.show.filter(x => x !== pan);
      } else {
        this.show.push(pan);
      }
      this.$emit("update:panes", this.show);
    },
    includes(pan) {
      return this.show.includes(pan);
    }
  }
};
</script>

<style scoped></style>

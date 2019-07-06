<template>
  <div class="header mb-2" v-bind:class="{ 'sub-header': sub }">
    <slot></slot>
  </div>
</template>

<script>
export default {
  props: {
    sub: {
      type: Boolean,
      default: false
    }
  }
};
</script>

<style scoped>
.header {
  font-size: 30px;
}
.sub-header {
  font-size: 24px;
}
</style>

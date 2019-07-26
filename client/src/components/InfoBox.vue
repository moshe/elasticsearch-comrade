<template>
  <div class="info-square pa-2 elevation-6">{{ text }}</div>
</template>

<script>
export default {
  props: {
    text: {
      type: String,
      required: true
    }
  }
};
</script>

<style scoped>
.info-square {
  border: 8px solid var(--border-color);
  border-radius: 4px;
  text-align: center;
  font-size: 20px;
}
</style>

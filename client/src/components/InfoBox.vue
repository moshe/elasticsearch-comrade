<template>
  <div class="info-square pa-2">
    {{ text }}
  </div>
</template>

<script>
export default {
  name: "InfoBox",
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
  border: 6px solid #424242;
  text-align: center;
  font-size: 20px;
}
</style>

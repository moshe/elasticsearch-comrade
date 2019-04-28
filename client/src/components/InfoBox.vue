<template>
  <div class="info-square pa-2 elevation-6">
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
  border: 8px solid #424242;
  border-radius: 2px;
  text-align: center;
  font-size: 20px;
}
</style>

<template>
  <div>
    <div style="font-size: 25px" class="mb-2">Pending Actions</div>
    <div v-for="(action, index) in actions" :key="index">
      <div v-if="action.action === 'remove'">
        Remove alias
        <span style="font-weight:600">{{ action.alias }}</span> from
        <span style="font-weight:600">{{ action.index }}</span>
      </div>
      <div v-else-if="action.action === 'add'">
        Add alias
        <span style="font-weight:600">{{ action.alias }}</span> to
        <span style="font-weight:600">{{ action.index }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    actions: {
      type: Array
    }
  }
};
</script>

<style scoped></style>

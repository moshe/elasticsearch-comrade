<template>
  <div>
    <div style="font-size: 25px" class="mb-2">Pending Actions</div>
    <div v-for="(action, index) in pendingActions" :key="index">
      <v-btn flat icon small @click="$emit('removeAction', action)">
        <v-icon>clear</v-icon>
      </v-btn>
      <span v-if="action.action === 'remove'">
        Remove alias
        <span style="font-weight:600">{{ action.alias }}</span> from
        <span style="font-weight:600">{{ action.index }}</span>
      </span>
      <span v-else-if="action.action === 'add'">
        Add alias
        <span style="font-weight:600">{{ action.alias }}</span> to
        <span style="font-weight:600">{{ action.index }}</span>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    pendingActions: {
      type: Array
    }
  }
};
</script>

<style scoped>
.v-btn--icon.v-btn--small {
  margin: 0;
}
</style>

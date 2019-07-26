<template>
  <div>
    <v-header sub>Pending Actions</v-header>
    <div v-for="(action, index) in pendingActions" :key="index">
      <v-btn icon x-small @click="$emit('removeAction', action)">
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
import VHeader from "../Base/Header.vue";

export default {
  components: { VHeader },
  props: {
    pendingActions: {
      type: Array
    }
  }
};
</script>

<style scoped></style>

<template>
  <v-menu offset-y style="display: inline-block">
    <template v-slot:activator="{ on }">
      <div
        class="shard-square"
        v-bind:class="{ 'primary-shard': primary, 'replica-shard': !primary }"
        v-on="on"
      >
        {{ id }}
      </div>
    </template>
    <v-list dense>
      <v-list-tile @click="">
        <v-list-tile-action style="min-width: unset" class="pr-2">
          <v-icon style="font-size: 16px">phone</v-icon>
        </v-list-tile-action>
        <v-list-tile-title>Select for relocation</v-list-tile-title>
      </v-list-tile>

      <v-list-tile @click="">
        <v-list-tile-action style="min-width: unset" class="pr-2">
          <v-icon style="font-size: 16px">phone</v-icon>
        </v-list-tile-action>
        <v-list-tile-title>cake</v-list-tile-title>
      </v-list-tile>
    </v-list>
  </v-menu>
</template>

<script>
export default {
  name: "ShardSquare",
  props: {
    id: {
      required: true,
      type: Number
    },
    primary: {
      required: true,
      type: Boolean
    }
  }
};
</script>

<style>
.shard-square {
  display: inline-block;
  margin: 1px;
  height: 20px;
  width: 20px;
  text-align: center;
  cursor: pointer;
}

.primary-shard {
  background-color: #72a164;
  border: 1px solid #4e6e44;
}

.replica-shard {
  background-color: rgba(60, 83, 54, 0.67);
  border: 1px solid rgba(54, 75, 49, 0.67);
}

.v-list--dense .v-list__tile:not(.v-list__tile--avatar) {
  height: unset;
}
</style>

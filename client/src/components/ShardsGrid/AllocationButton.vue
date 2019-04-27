<template>
  <v-menu offset-y>
    <template v-slot:activator="{ on }">
      <v-btn small color="red" v-on="on">
        <v-icon size="12px" dark class="mr-1">lock</v-icon>
        Allocation
      </v-btn>
    </template>
    <v-list dense two-line>
      <div v-for="(option, i) in options" :key="option.name">
        <v-list-tile
          :disabled="option.name === current"
          @click="request(option)"
        >
          <v-list-tile-content>
            <v-list-tile-title>{{ option.name }}</v-list-tile-title>
            <v-list-tile-sub-title>
              {{ option.text }}
            </v-list-tile-sub-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-divider v-if="i !== options.length - 1" />
      </div>
    </v-list>
  </v-menu>
</template>

<script>
export default {
  name: "AllocationButton",
  data() {
    return {
      current: "all",
      options: [
        {
          name: "all",
          text: "(default) Allows shard allocation for all kinds of shards"
        },
        {
          name: "primaries",
          text: "Allows shard allocation only for primary shards"
        },
        {
          name: "new_primaries",
          text:
            "Allows shard allocation only for primary shards for new indices"
        },
        {
          name: "none",
          text: "No shard allocations of any kind are allowed for any indices"
        }
      ]
    };
  },
  methods: {
    request(option) {
      console.log(option);
    }
  }
};
</script>

<style scoped>
.v-btn--small {
  height: 18px;
  padding: 3px 7px;
  font-size: 9px !important;
  margin: 0;
}
.v-btn {
  min-width: 50px;
}
</style>

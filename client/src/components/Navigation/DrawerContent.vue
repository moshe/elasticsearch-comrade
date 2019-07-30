<template>
  <v-list dense nav>
    <v-list-item link v-for="page in pages" :key="page.to" :to="page.to">
      <v-list-item-icon class="mr-4">
        <v-icon>{{ page.icon }}</v-icon>
      </v-list-item-icon>
      <v-list-item-content>
        <v-list-item-title>{{ page.name }}</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <v-divider class="mt-6" />
    <v-list-item @click="selectCluster(null)">
      <v-list-item-icon class="mr-4">
        <v-icon>logout</v-icon>
      </v-list-item-icon>
      <v-list-item-content>
        <v-list-item-title>Logout</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
  </v-list>
</template>

<script>
import { mapMutations } from "vuex";
export default {
  data() {
    return {
      pages: [
        { to: "/", icon: "home", name: "Home" },
        { to: "/aliases", icon: "link", name: "Aliases" },
        { to: "/rest", icon: "build", name: "REST" },
        { to: "/tasks", icon: "perm_data_setting", name: "Tasks" },
        { to: "/templates", icon: "add_to_photos", name: "Index Templates" },
        { to: "/snapshots", icon: "backup", name: "Snapshots" }
      ]
    };
  },
  methods: { ...mapMutations(["selectCluster"]) }
};
</script>

<style scoped></style>

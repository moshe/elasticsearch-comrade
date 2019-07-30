<template>
  <v-list dense>
    <v-list-item link v-for="page in pages" :key="page.to" :to="page.to">
      <v-list-item-icon class="mr-4">
        <v-icon color="white" v-text="page.icon" />
      </v-list-item-icon>
      <v-list-item-content>
        <v-list-item-title style="color: white">{{
          page.name
        }}</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
  </v-list>
</template>

<script>
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
  }
};
</script>

<style scoped></style>

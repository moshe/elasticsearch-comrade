<template>
  <v-list>
    <v-list-item v-for="page in pages" :key="page.to" :to="page.to">
      <v-list-item-action>
        <v-icon>{{ page.icon }}</v-icon>
      </v-list-item-action>
      <v-list-item-title>{{ page.name }}</v-list-item-title>
    </v-list-item>
  </v-list>
</template>

<script>
export default {
  data: () => ({
    pages: [
      { to: "/", icon: "home", name: "Home" },
      { to: "/aliases", icon: "link", name: "Aliases" },
      { to: "/rest", icon: "build", name: "REST" },
      { to: "/tasks", icon: "perm_data_setting", name: "Tasks" },
      { to: "/templates", icon: "add_to_photos", name: "Index Templates" },
      { to: "/snapshots", icon: "backup", name: "Snapshots" }
    ]
  })
};
</script>

<style scoped></style>

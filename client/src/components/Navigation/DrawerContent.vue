<template>
  <v-list>
    <v-list-tile v-for="page in pages" :key="page.to" :to="page.to">
      <v-list-tile-action>
        <v-icon>{{ page.icon }}</v-icon>
      </v-list-tile-action>
      <v-list-tile-title>{{ page.name }}</v-list-tile-title>
    </v-list-tile>
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
      { to: "/snapshots", icon: "backup", name: "Snapshots" },
      { to: "/repositories", icon: "storage", name: "Repositories" }
    ]
  })
};
</script>

<style scoped></style>

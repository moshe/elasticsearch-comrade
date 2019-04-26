<template xmlns:v-slot="http://www.w3.org/1999/XSL/Transform">
  <v-list>
    <v-list-tile to="/">
      <v-list-tile-action>
        <v-icon>home</v-icon>
      </v-list-tile-action>
      <v-list-tile-title>Home</v-list-tile-title>
    </v-list-tile>
    <v-divider />
    <v-list-tile to="/terminal">
      <v-list-tile-action>
        <v-icon>build</v-icon>
      </v-list-tile-action>
      <v-list-tile-title>Terminal</v-list-tile-title>
    </v-list-tile>

    <v-list-group prepend-icon="backup">
      <template v-slot:activator>
        <v-list-tile>
          <v-list-tile-title>Snapshots</v-list-tile-title>
        </v-list-tile>
      </template>
      <v-list no-action sub-group>
        <v-list-tile v-for="([text, icon], i) in admins" :key="i" @click="">
          <v-list-tile-title v-text="text"></v-list-tile-title>
          <v-list-tile-action>
            <v-icon v-text="icon" />
          </v-list-tile-action>
        </v-list-tile>
      </v-list>
    </v-list-group>
  </v-list>
</template>

<script>
export default {
  name: "DrawerContent",
  data: () => ({
    admins: [["Management", "people_outline"], ["Settings", "settings"]]
  })
};
</script>

<style scoped></style>

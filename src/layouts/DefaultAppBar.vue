<template>
  <v-app-bar app light class="px-12">
    <v-app-bar-nav-icon @click="drawer = !drawer" class="d-md-none">
    </v-app-bar-nav-icon>

    <router-link to="/">
      <v-app-bar-title>COMPAS WebViewer</v-app-bar-title>
    </router-link>

    <v-spacer></v-spacer>
  </v-app-bar>

  <v-navigation-drawer temporary app light v-model="drawer">
  </v-navigation-drawer>
</template>

<script setup>
//
</script>

<script>
export default {
  data: () => {
    return {
      drawer: false,
    };
  },
  computed: {},
};
</script>

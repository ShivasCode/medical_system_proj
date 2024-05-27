<script setup></script>

<template>
<nav>
    <router-link to="/home">
      <img class="logo" src="../assets/images/Logo.svg" alt="Logo" />
    </router-link>
  </nav></template>

<style scoped>
nav {
  padding: 20px 10px;
  border-bottom: 2px outset rgba(0, 0, 0, 0.2);
}

.logo {
  margin-left: 5%;
  max-width: 10%;
}
</style>

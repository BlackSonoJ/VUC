<script setup lang="ts">
import Main from './pages/Main.vue';
</script>

<template>
  <div class="app-wrapper">
    <Main />
  </div>
</template>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html,
body {
  width: 100%;
  height: fit-content;
  font-family: 'Roboto', serif;
  font-optical-sizing: auto;
  font-weight: 300;
  font-style: normal;
  color: white;
  padding: 4px;
  background-color: #000040;
}

.app-wrapper {
  width: 100%;
  height: 100vh;
  padding-top: 2px;
}
</style>

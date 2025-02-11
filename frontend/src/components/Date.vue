<script setup lang="ts">
const today = new Date();
</script>
<template>
  <div
    class="flex w-full justify-center items-center bg-[#0c0c23] text-white h-[80px] border-b-2 border-[#0f0f81]"
    style="grid-area: 1 / 1 / 2 / 2"
  >
    <p class="text-[3rem]">{{ today.toLocaleDateString() }}</p>
  </div>
</template>
<style scoped></style>

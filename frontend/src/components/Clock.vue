<script setup lang="ts">
import { onBeforeUnmount, ref } from 'vue';

let time = ref(new Date());

const interval = setInterval(() => {
  time.value = new Date();
}, 1000);

onBeforeUnmount(() => {
  clearInterval(interval);
});
</script>
<template>
  <div
    class="flex justify-center items-center w-full h-[78px] border-t-2 border-[#0f0f81] bg-[#0c0c23] rounded-[3px] text-white"
    style="grid-area: 2 / 1 / 3 / 2"
  >
    <p class="text-[4rem]">{{ time.toLocaleTimeString() }}</p>
  </div>
</template>
<style scoped></style>

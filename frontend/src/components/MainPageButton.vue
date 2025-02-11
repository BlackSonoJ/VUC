<script setup lang="ts">
defineProps<{ buttonText: string }>();
</script>
<template>
  <RouterLink
    to="/"
    class="text-black w-full h-full"
    style="grid-area: 1 / 2 / 3 / 3"
  >
    <div
      class="flex justify-center items-center w-full h-full bg-[#3fd5fe] rounded-[3px]"
    >
      <p class="text-center text-lg">{{ buttonText }}</p>
    </div>
  </RouterLink>
</template>
<style scoped></style>

<script setup lang="ts">
import { defineProps } from 'vue';

const props = defineProps<{ text: string; margin?: string }>();
</script>
<template>
  <div
    :class="[
      'flex',
      'w-[170px]',
      'justify-center',
      'items-center',
      'bg-[#2b41fe]',
      props.margin,
    ]"
  >
    <p>{{ props.text }}</p>
  </div>
</template>
<style scoped></style>

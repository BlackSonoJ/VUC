<script setup lang="ts">
import Event from '../@types/eventType.type';
import { DefineProps } from 'vue';
defineProps<{
  isOpen: boolean;
  event: Event | null;
}>();

const emit = defineEmits(['close']);
</script>
<template>
  <div
    v-if="isOpen"
    class="fixed inset-0 bg-black/60 flex items-center justify-center z-50"
    @click.self="emit('close')"
  >
    <div
      class="relative w-2/5 mx-auto h-2/5 p-4 flex flex-col bg-white justify-baseline items-start rounded-2xl gap-20"
      style="padding: 24px"
    >
      <h1 class="text-5xl text-black self-center">{{ event?.name }}</h1>
      <p class="text-2xl text-black">{{ event?.description }}</p>
      <button
        class="absolute top-4 right-4 rounded-full p-2 shadow-md hover:bg-gray-200 transition cursor-pointer"
        @click="emit('close')"
      >
        <svg
          width="24"
          height="24"
          viewBox="0 0 24 24"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            clip-rule="evenodd"
            d="M6.707 5.293a1 1 0 0 0-1.414 1.414L10.586 12l-5.293 5.293a1 1 0 0 0 1.414 1.414L12 13.414l5.293 5.293a1 1 0 0 0 1.414-1.414L13.414 12l5.293-5.293a1 1 0 0 0-1.414-1.414L12 10.586 6.707 5.293Z"
            fill="black"
          />
        </svg>
      </button>
    </div>
  </div>
</template>

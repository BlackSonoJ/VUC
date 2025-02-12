<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';

const images: string[] = ['/faviconV2.png', '/mem.jpg', '/vite.svg'];

const currentIndex = ref<number>(0);
let intervalId: number | null = null;

const nextImage = (): void => {
  currentIndex.value = (currentIndex.value + 1) % images.length;
};

onMounted(() => {
  intervalId = window.setInterval(nextImage, 3000);
});

onUnmounted(() => {
  if (intervalId !== null) {
    clearInterval(intervalId);
  }
});
</script>
<template>
  <div
    class="relative flex justify-center items-center w-auto max-w-[100%] h-screen border-8 border-[#3b04c67c] shadow shadow-white rounded-[5px]"
  >
    <img
      v-for="(image, index) in images"
      :key="index"
      :src="image"
      alt="slider"
      class="absolute top-1/2 left-1/2 m-auto transform -translate-x-1/2 -translate-y-1/2 w-auto max-w-full object-cover transition-opacity duration-500 ease-in-out"
      :class="{
        'opacity-100': index === currentIndex,
        'opacity-0': index !== currentIndex,
      }"
    />
  </div>
</template>

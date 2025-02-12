<script setup lang="ts">
import GalleryImage from './GalleryImage.vue';

const images: string[] = [
  '/mem.jpg',
  '/mem.jpg',
  '/mem.jpg',
  '/mem.jpg',
  '/mem.jpg',
  '/mem.jpg',
  '/mem.jpg',
  '/mem.jpg',
  '/mem.jpg',
  '/mem.jpg',
  '/vite.svg',
  '/faviconV2.png',
];
</script>
<template>
  <div
    class="w-full mx-auto grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4"
    style="margin-top: 40px"
  >
    <GalleryImage
      v-for="(image, index) in images"
      :key="index"
      :image="image"
    />
  </div>
</template>

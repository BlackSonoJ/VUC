<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue';
import apiService from '../api/apiService';

interface ImagesType {
  id: number;
  image: string;
}

const currentIndex = ref<number>(0);
const errorMessage = ref<string | null>(null);
let intervalId: number | null = null;

const images = ref<ImagesType[]>([]);

const nextImage = (): void => {
  if (images.value.length > 0) {
    currentIndex.value = (currentIndex.value + 1) % images.value.length;
  }
};

const fetchImages = async () => {
  try {
    const response = await apiService.get<ImagesType[]>('/api/imagesMain');
    images.value = response.data;
    console.log(response);
  } catch (err) {
    errorMessage.value = 'Произошла ошибка при загрузке изображений';
  }
};

onMounted(() => {
  intervalId = window.setInterval(nextImage, 3000);
  fetchImages();
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
      :src="image.image"
      alt="slider"
      class="absolute top-1/2 left-1/2 m-auto transform -translate-x-1/2 -translate-y-1/2 w-full h-[700px] object-contain transition-opacity duration-500 ease-in-out"
      :class="{
        'opacity-100': index === currentIndex,
        'opacity-0': index !== currentIndex,
      }"
    />
  </div>

  <div
    v-if="errorMessage"
    class="text-[14px] text-red-500 mt-4 font-bold text-center"
  >
    {{ errorMessage }}
  </div>
</template>

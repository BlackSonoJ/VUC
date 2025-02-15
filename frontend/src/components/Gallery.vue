<script setup lang="ts">
import { onMounted, ref } from 'vue';
import GalleryImage from './GalleryImage.vue';
import GalleryModal from './GalleryModal.vue';
import ImagesType from '../@types/imageType.type';
import apiService from '../api/apiService';

const isOpen = ref<boolean>(false);
const selectedImage = ref<string>('');
const images = ref<ImagesType[]>([]);
const errorMessage = ref<string | null>(null);

const handleClick = (image: string) => {
  selectedImage.value = image;
  isOpen.value = true;
};

const handleClose = () => {
  isOpen.value = false;
};

const getImages = async () => {
  try {
    const response = await apiService.get<ImagesType[]>('/api/images');
    images.value = response.data;
  } catch (err) {
    errorMessage.value = 'Произошла ошибка при загрузке изображений';
  }
};

onMounted(getImages);
</script>
<template>
  <div
    class="w-full grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-4"
    style="margin-top: 40px"
  >
    <GalleryImage
      v-for="(image, index) in images"
      @click="handleClick(image.image)"
      :key="index"
      :image="image.image"
    />
  </div>
  <GalleryModal
    :isOpen="isOpen"
    :image="selectedImage"
    @close="handleClose"
  />

  <div
    v-if="errorMessage"
    class="text-[14px] text-red-500 mt-4 font-bold text-center"
  >
    {{ errorMessage }}
  </div>
</template>

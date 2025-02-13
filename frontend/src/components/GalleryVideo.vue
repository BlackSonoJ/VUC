<script setup lang="ts">
import { onMounted, ref } from 'vue';
import apiService from '../api/apiService';
import VideoType from '../@types/videoType.type';

const videos = ref<VideoType[]>([]);
const currentVideo = ref<number>(0);
const errorMessage = ref<string | null>(null);

const getVideos = async () => {
  try {
    const response = await apiService.get<VideoType[]>('/api/videos');
    videos.value = response.data;
  } catch (err) {
    errorMessage.value = 'Произошла ошибка при загрузке видео';
  }
};

onMounted(getVideos);

const nextVideo = () => {
  if (currentVideo.value < videos.value.length - 1) {
    currentVideo.value++;
  }
};

const prevVideo = () => {
  if (currentVideo.value > 0) {
    currentVideo.value--;
  }
};
</script>
<template>
  <div
    class="w-full h-fit flex justify-between items-center"
    style="margin-top: 100px"
  >
    <button
      class="w-20 h-20 cursor-pointer"
      @click="prevVideo"
      :disabled="currentVideo === 0"
    >
      <svg
        width="48"
        height="48"
        viewBox="0 0 16 16"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          fill-rule="evenodd"
          clip-rule="evenodd"
          d="M7.008 10.996L2.004 7.992l5.004-2.996v1.997h6.996v1.998H7.008v2.005z"
          fill="white"
        ></path>
      </svg>
    </button>
    <div class="w-full h-fit">
      <video
        controls
        controlslist="nodownload nofullscreen"
        disableremoteplayback
        disablepictureinpicture
        autoplay
        muted
        loop
        v-if="videos.length > 0"
        :src="videos[currentVideo].video"
      ></video>
    </div>
    <button
      class="w-20 h-20 cursor-pointer"
      @click="nextVideo"
      :disabled="currentVideo === videos.length - 1"
    >
      <svg
        width="48"
        height="48"
        viewBox="0 0 16 16"
        xmlns="http://www.w3.org/2000/svg"
      >
        <path
          fill-rule="evenodd"
          clip-rule="evenodd"
          d="M9 4.996L14.004 8 9 10.996V9H2.004V7H9V4.996z"
          fill="white"
        ></path>
      </svg>
    </button>
  </div>

  <div
    v-if="errorMessage"
    class="text-[14px] text-red-500 mt-4 font-bold text-center"
  >
    {{ errorMessage }}
  </div>
</template>

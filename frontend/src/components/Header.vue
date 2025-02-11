<script setup lang="ts">
import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';
import MainPageButton from './MainPageButton.vue';
import MenuButton from './MenuButton.vue';
import Date from './Date.vue';
import Clock from './Clock.vue';

const buttonText = ref('');
const route = useRoute();

watch(
  () => route.path,
  newPath => {
    buttonText.value = newPath === '/' ? 'Вы на главной' : 'Назад на главную';
  },
  { immediate: true }
);
</script>
<template>
  <header class="w-full h-40">
    <div
      class="grid grid-cols-[2fr_2fr_1fr_1fr] grid-rows-2 gap-1 w-full h-40 custom-margin"
    >
      <Date />
      <Clock />
      <MainPageButton :buttonText="buttonText" />
      <RouterLink
        to="/videos"
        class="bg-[#2b41fe] decoration-0 rounded-[3px] flex justify-center items-center"
        style="grid-area: 1 / 3 / 2 / 4"
      >
        <MenuButton
          text="Видеоматериалы"
          :margin="'mb-[5px] mr-[5px]'"
        />
      </RouterLink>
      <RouterLink
        to="/images"
        class="bg-[#2b41fe] decoration-0 rounded-[3px] flex justify-center items-center"
        style="grid-area: 1 / 4 / 2 / 5"
      >
        <MenuButton
          text="Фотоматериалы"
          :margin="'mb-[5px]'"
        />
      </RouterLink>
      <RouterLink
        to="/calendar"
        class="bg-[#2b41fe] decoration-0 rounded-[3px] flex justify-center items-center"
        style="grid-area: 2 / 3 / 3 / 4"
      >
        <MenuButton text="Календарь событий" />
      </RouterLink>
      <RouterLink
        to="/info"
        class="bg-[#2b41fe] decoration-0 rounded-[3px] flex justify-center items-center"
        style="grid-area: 2 / 4 / 3 / 5"
      >
        <MenuButton text="Информация" />
      </RouterLink>
    </div>
  </header>
</template>
<style scoped></style>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
import {
  getCurrentMonthAndYear,
  generateCalendar,
} from '../utils/calendarGenerate';
import apiService from '../api/apiService';

interface Event {
  id: number;
  name: string;
  description: string;
  published: string;
}

const currentMonth = ref(new Date().getMonth());
const currentYear = ref(new Date().getFullYear());
const events = ref<Event[]>([]);
const errorMessage = ref<string | null>(null);
const daysOfWeek = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'];

const currentMonthAndYear = computed(() => {
  const formatted = getCurrentMonthAndYear(
    currentMonth.value,
    currentYear.value
  );
  return formatted.charAt(0).toUpperCase() + formatted.slice(1);
});

const calendarDays = computed(() =>
  generateCalendar(currentMonth.value, currentYear.value)
);

const getEventForDay = (day: number) => {
  return events.value.find(event => {
    const eventDate = new Date(event.published);
    return (
      eventDate.getDate() === day &&
      eventDate.getMonth() === currentMonth.value &&
      eventDate.getFullYear() === currentYear.value
    );
  });
};

const fetchEvents = async () => {
  try {
    const response = await apiService.get<Event[]>('/api/events');
    events.value = response.data;
  } catch (err) {
    errorMessage.value = 'Произошла ошибка при загрузке событий';
  }
};

onMounted(fetchEvents);

const goToPreviousMonth = () => {
  if (currentMonth.value === 0) {
    currentMonth.value = 11;
    currentYear.value--;
  } else {
    currentMonth.value--;
  }
};

const goToNextMonth = () => {
  if (currentMonth.value === 11) {
    currentMonth.value = 0;
    currentYear.value++;
  } else {
    currentMonth.value++;
  }
};
</script>
<template>
  <div
    v-if="errorMessage"
    class="text-[14px] text-red-500 mb-4 font-bold text-center"
  >
    {{ errorMessage }}
  </div>

  <div class="w-full h-fit">
    <div
      class="my-5 flex justify-between items-center w-full"
      style="margin-top: 2rem"
    >
      <button
        class="cursor-pointer"
        @click="goToPreviousMonth"
      >
        ◀
      </button>
      <p class="text-2xl">{{ currentMonthAndYear }}</p>
      <button
        class="cursor-pointer"
        @click="goToNextMonth"
      >
        ▶
      </button>
    </div>
    <div
      class="flex items-center justify-center"
      style="margin-bottom: 1rem; margin-top: 2rem"
    >
      <div
        class="text-center w-full"
        v-for="(day, index) in daysOfWeek"
        :key="index"
      >
        <p class="text-lg font-bold">{{ day }}</p>
      </div>
    </div>

    <div class="grid grid-cols-7 gap-1 grid-rows-[200px_repeat(6,_200px)]">
      <div
        class="relative flex flex-col items-center p-4 w-full h-full border border-gray-300 rounded-xl shadow-md transition-all duration-300"
        :class="day ? 'bg-white hover:bg-gray-100' : 'bg-gray-200 opacity-50'"
        v-for="(day, index) in calendarDays"
        :key="index"
      >
        <span
          class="absolute top-2 left-2 text-gray-800 font-semibold text-lg"
          v-if="day"
          >{{ day }}</span
        >
        <div
          class="mt-10 flex flex-col items-center justify-center gap-4 text-center w-[50%]"
          v-if="getEventForDay(day)"
          style="margin-top: 15px"
        >
          <p
            class="text-blue-600 font-bold text-[12px] w-full break-words whitespace-pre-line"
          >
            {{ getEventForDay(day)?.name }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>
<style></style>

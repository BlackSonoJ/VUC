<script setup lang="ts">
const props = defineProps({
  image: String,
});
</script>
<template>
  <div class="w-full h-full">
    <img
      :src="props.image"
      alt="photo"
      class="w-full object-cover"
    />
  </div>
</template>
